import copy
import random
from Dati.DatabaseCarte import DatabaseCarte
from Dati.Carta import Carta
from Dati.Mazzo import Mazzo

#Rank selection
def selezione(generazione:list[Mazzo],pool_size:int):

    #Ordina la generazione in ordine decrescente
    generazione.sort(key=lambda x: x.calcola_fitness(),reverse=True)
    probabilita = []
    i = len(generazione)

    while i > 0:
        probabilita.append(i)
        i -= 1

    estratti = random.choices(generazione, weights=probabilita, k=pool_size)
    estratti = [copy.deepcopy(m) for m in estratti]

    return estratti



#Random resetting
def mutazione(mazzo:Mazzo,p:float,n_fisse:int,db):
    esito = random.uniform(0,1)

    #Probabilita di mutazione
    if esito > p:
        return mazzo

    mazzo_mutato = False

    while mazzo_mutato == False:
        indice_carta_da_mutare = int(random.uniform(n_fisse, 8))  # Sceglie un numero casuale da 0 a 7
        carta_da_mutare = mazzo.carte[indice_carta_da_mutare]
        carta_random = db.estraizione_casuale()
        mazzo_mutato = mazzo.sostituisci_carta(
            carta_da_mutare.nome,
            carta_random.nome,
            db
        )
    return mazzo_mutato

#Uniform
def crossover(genitore1:Mazzo,genitore2:Mazzo,p:float,n:int,n_fisse:int):
    esito = random.uniform(0, 1)
    j = 0 #per tenere conto dell'iterazioni massime che può fare l'algoritmo

    #Probabilita di crossover
    if esito > p:
        esito = random.uniform(0, 1)

        if esito < 0.5:
            return genitore1
        return genitore2

    nuovo_mazzo = []
    figlio = False

    while figlio == False and j < n:
        i = n_fisse
        #inizializzo le carte fisse
        while i > 0:
            nuovo_mazzo.append(genitore1.carte[i-1])
            i -= 1
        i = n_fisse

        while i < len(genitore1.carte):
            esito = random.uniform(0, 1)

            if esito < 0.5:
                carta_figlio = genitore1.carte[i]
            else:
                carta_figlio = genitore2.carte[i]

            nuovo_mazzo.append(carta_figlio)
            i += 1

        figlio = Mazzo(nuovo_mazzo)

        if not figlio.is_valido():
            figlio = False
            nuovo_mazzo.clear()
        j += 1

    if not figlio or not figlio.is_valido():
        esito = random.uniform(0, 1)

        if esito < 0.5:
            return genitore1
        return genitore2

    return figlio









