import math
from Dati.Carta import Carta
from jinja2.nodes import List
from Dati.DatabaseCarte import DatabaseCarte

class Mazzo:
    def __init__(self,carte):
        if len(carte) != 8:
            raise ValueError("Il mazzo deve contenere esattamente 8 carte")
        for carta in carte:
            if not isinstance(carta, Carta):
                raise TypeError("Tutti gli elementi devono essere di tipo Carta")
        self.carte = list(carte)

    # --- medie: protette da divisione per zero ---
    def _media_sicura(self, valori):
        valori_validi = [v for v in valori if v >= 0]
        if not valori_validi:
            return 0
        return sum(valori_validi) / len(valori_validi)

    def get_danno_medio(self):
        return self._media_sicura([c.danno_s for c in self.carte])

    def get_vita_medio(self):
        return self._media_sicura([c.punti_vita for c in self.carte])

    def get_costo_medio(self):
        return self._media_sicura([c.costo for c in self.carte])

    def get_velocita_medio(self):
        return self._media_sicura([c.velocita for c in self.carte])

    def get_volante(self):
        return sum(1 for c in self.carte if c.volante)

    def get_incantesimi(self):
        return sum(1 for c in self.carte if str(c.tipologia).casefold() == "incantesimo")

    def get_edifici(self):
        return sum(1 for c in self.carte if str(c.tipologia).casefold() == "edificio")

    def get_portata(self):
        return sum(1 for c in self.carte if c.portata)

    def get_bersaglio(self):
        return sum(1 for c in self.carte if c.tipo_bersaglio)

    def get_effetti(self):
        return sum(c.effetti_aggiuntivi for c in self.carte)

    #Controlla se il deck rispetta i vincoli
    def is_valido(self):
        if self.get_incantesimi() > 2:
            return False
        nomi = [c.nome for c in self.carte]
        return len(set(nomi)) == len(nomi)  # no doppioni

    def calcola_fitness(self):
        atk = math.sqrt(self.get_danno_medio()) * (1+self.get_bersaglio()*0.2) * (1+self.get_velocita_medio()*0.2)
        dif = math.sqrt(self.get_vita_medio()/6) * (1+self.get_portata()*0.1) * (1+self.get_effetti()*0.05)
        p = 0

        if(self.get_costo_medio() > 1):
            p += math.pow(self.get_costo_medio() - 1,2.5)

        if(self.get_bersaglio()>2):
            p += self.get_bersaglio()*3

        if(self.get_portata() == 0):
            p += 15

        if(self.get_incantesimi()==0):
            p += 12

        if(self.get_volante()==0):
            p += 10
        elif(self.get_volante()>3):
            p += 4

        if(self.get_edifici()==0):
            p += 5
        elif(self.get_edifici()>2):
            p += 12

        return atk + dif - p

    # Restituisce un nuovo mazzo sostituendo una carta; ritorna False se non possibile
    def sostituisci_carta(self, nome_carta, nome_carta_sostitutiva, db):
        carta_sostitutiva = db.get_carta(nome_carta_sostitutiva)
        if carta_sostitutiva is None:
            return False

        nuovo_mazzo = self.carte.copy()

        # trova la carta da sostituire (ora controlla anche l'ultima)
        idx = next((i for i, c in enumerate(nuovo_mazzo) if c.nome == nome_carta), None)
        if idx is None:
            return False

        # evita doppioni "in ingresso"
        if any(c.nome == nome_carta_sostitutiva for c in nuovo_mazzo):
            return False
        nuovo_mazzo[idx] = carta_sostitutiva
        candidato = Mazzo(nuovo_mazzo)

        # scarta se viola vincoli (incantesimi ecc.)
        if not candidato.is_valido():
            return False

        return candidato

    @staticmethod
    def mazzo_random():
        i = 0
        num_incantesimi = 0
        deck = []
        db = DatabaseCarte()
        test = True

        while(i<8):
            carta = db.estraizione_casuale()

            for item in deck:
                if item.nome==carta.nome:
                    test = False
                if carta.tipologia == "incantesimo":
                    num_incantesimi += 1
                    if num_incantesimi > 2:
                        num_incantesimi -= 1
                        test = False
            if(not test):
               test = True
               continue
            deck.append(carta)
            i += 1

        return Mazzo(deck)

    def stampa_mazzo(self):
        print([c.nome for c in self.carte])

    # utile per hill climbing: chiave canonica (ordine irrilevante)
    def key(self):
        return tuple(sorted(c.nome for c in self.carte))