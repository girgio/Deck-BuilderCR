import random
from Dati.DatabaseCarte import DatabaseCarte
from Dati.Carta import Carta
from Dati.Mazzo import Mazzo

#Rank selection
def selezione(generazione:list[Mazzo],pool_size:int):

    #Ordina la generazione in ordine decrescente
    generazione.sort(key=lambda x: x.caclola_fitness(),reverse=True)
    probabilita = []
    i = len(generazione)

    while i > 0:
        probabilita.append(i)
        i -= 1

    estratti = random.choices(generazione, weights=probabilita, k=pool_size)

    return estratti



#Random resetting
def mutazione(mazzo:Mazzo,p:float):
    esito = random.uniform(0,1)

    #Probabilita di mutazione
    if esito < p:
        return False

    db = DatabaseCarte()
    mazzo_mutato = False

    while mazzo_mutato == False:
        indice_carta_da_mutare = int(random.uniform(0, 8))  # Sceglie un numero casuale da 0 a 7
        carta_da_mutare = Carta(mazzo.carte[indice_carta_da_mutare])
        carta_random = Carta(db.estraizione_casuale())
        mazzo_mutato = mazzo.sostituisci_carta(
            carta_da_mutare.nome,
            carta_random.nome,
            db
        )
    return mazzo_mutato





