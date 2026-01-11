import math

from Carta import Carta
from Carta import DatabaseCarte

class Mazzo:
    def __init__(self,carte):
        if len(carte) != 8:
            raise ValueError("Il mazzo deve contenere esattamente 8 carte")

        for carta in carte:
            if not isinstance(carta, Carta):
                raise TypeError("Tutti gli elementi devono essere di tipo Carta")

        self.carte = carte

    def get_danno_medio(self):
        danno_totale = 0
        carte_contate = 8

        for i in self.carte:
            if i.danno_s >= 0:
                danno_totale += i.danno_s
            else:
                carte_contate -= 1
        danno_medio = danno_totale/carte_contate

        return danno_medio

    def get_vita_medio(self):
        vita_totale = 0
        carte_contate = 8

        for i in self.carte:
            if i.punti_vita >= 0:
                vita_totale += i.punti_vita
            else:
                carte_contate -= 1


        vita_medio = vita_totale/carte_contate
        return vita_medio

    def get_costo_medio(self):
        costo_totale = 0
        carte_contate = 8

        for i in self.carte:
            if i.costo >= 0:
                costo_totale += i.costo
            else:
                carte_contate -= 1

        costo_medio = costo_totale/carte_contate
        return costo_medio

    def get_velocita_medio(self):
        velocita_totale = 0
        carte_contate = 8

        for i in self.carte:
            if i.velocita >= 0:
                velocita_totale += i.velocita
            else:
                carte_contate -= 1
        velocita_medio = velocita_totale/carte_contate
        return velocita_medio

    def get_volante(self):
        count = 0

        for i in self.carte:
            if i.volante:
                count += 1

        return count

    def get_incantesimi(self):
        count = 0

        for i in self.carte:
            if i.tipologia.casefold() == 'incantesimo':
                count += 1

        return count

    def get_edifici(self):
        count = 0
        for i in self.carte:
            if i.tipologia.casefold() == 'edificio':
                count += 1

        return count

    def get_portata(self):
        count = 0
        for i in self.carte:
            if i.portata:
                count += 1
        return count

    def get_bersaglio(self ):
        count = 0
        for i in self.carte:
            if i.tipo_bersaglio:
                count += 1
        return count

    def get_effetti(self):
        tot = 0
        for i in self.carte:
            tot += i.effetti_aggiuntivi
        return tot

    #Controlla se il deck rispetta i vincoli
    def is_valido(self):
        l= len(self.carte)
        i = 0
        if(self.get_incantesimi()>2):
            return False
        while i< l - 1:
            j = i + 1
            while j < l:
                if self.carte[i].nome==self.carte[j].nome:
                    return False
                j+=1
            i += 1

        return True

    def caclola_fitness(self):
        atk = math.sqrt(self.get_danno_medio()) * (1+self.get_bersaglio()*0.3) * (1+self.get_velocita_medio()*0.2)
        dif = math.sqrt(self.get_vita_medio()/6) * (1+self.get_portata()*0.2) * (1+self.get_effetti()*0.1)
        p = 0

        if(self.get_costo_medio() > 3):
            p += math.pow(self.get_costo_medio() - 3,3)

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

    #Restiuisce un nuovo mazzo a partire dal mazzo corrente, ma con nome_carta sostituito da nome_carta_sotitutiva, restituisce false se non trova la carta da sostituire
    def sostituisci_carta(self,nome_carta,nome_carta_sostituiva):
        db = DatabaseCarte()
        carta_sostituiva = db.get_carta(nome_carta_sostituiva)
        carte_deck = self.carte
        nuovo_mazzo = self.carte.copy()
        esito = False
        i = 0

        while(i < len(carte_deck) - 1):
            if(carte_deck[i].nome==nome_carta):
                carte_deck.remove(carte_deck[i])
                esito = True
                break;
            i += 1

        if(esito):
            carte_deck.append(carta_sostituiva)
        else:
            return esito




