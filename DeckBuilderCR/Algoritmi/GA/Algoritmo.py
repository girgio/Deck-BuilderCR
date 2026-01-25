import random
from typing import Set, Tuple, Optional, List
from Operatori import *
from Dati.Mazzo import Mazzo
from Dati.Carta import Carta
from Algoritmi.HillClimbing import costruisci_mazzo_random_valido

def algoritmo_genetico(
    size_popolazione:int,
    size_mating_pool:int,
    p_mutazione:int,
    db: DatabaseCarte,
    fisse: Set[str],
    seed: Optional[int] = None
)-> Tuple[Mazzo, float]:

    if seed is not None:
        random.seed(seed)

    fisse = {n.strip() for n in fisse if n and n.strip()}

    nomi_db = db.get_nomi_carte()
    if len(nomi_db) < 8:
        raise ValueError("Database carte troppo piccolo: servono almeno 8 carte.")
    i = 0
    numero_generazione = 1
    generazione = []

    while i < size_popolazione:
        generazione.append(costruisci_mazzo_random_valido(db, fisse))
        i += 1

    i = 0

    print("---GENERAZIONE INIZIALE----")
    for m in generazione:
        m.stampa_mazzo()

    new_best_mazzo = max(generazione, key=lambda x: x.calcola_fitness())
    new_best_fitness = new_best_mazzo.calcola_fitness()
    best_fitness = new_best_fitness - 1 #per far in modo che la condizione del while sia vera
    best_mazzo = None

    while best_fitness < new_best_fitness:
        best_mazzo = new_best_mazzo
        best_fitness = new_best_fitness
        mating_pool = selezione(generazione,size_mating_pool)
        generazione.clear()

        while i < size_popolazione:
            genitore1 = mating_pool[i % 4] #il primo genitore lo sceglie in ordine
            genitore2 = random.choice(mating_pool) #il secondo genitore viene scelto a caso
            figlio = crossover(genitore1,genitore2)
            figlio = mutazione(figlio,p_mutazione)
            generazione.append(figlio)
            i += 1
        numero_generazione += 1

        new_best_mazzo = max(generazione,key=lambda x: x.calcola_fitness())
        new_best_fitness = new_best_mazzo.calcola_fitness()

        print("---GENERAZIONE NUMERO ",numero_generazione,"---")
        for m in generazione:
            m.stampa_mazzo()


    return best_mazzo, best_fitness










