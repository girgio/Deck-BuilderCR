from operator import truediv

from Carta import Carta

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