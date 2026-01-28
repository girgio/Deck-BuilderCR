import random
from typing import Set, Tuple, Optional
from Algoritmi.GA.Operatori import selezione, crossover, mutazione
from Dati.DatabaseCarte import DatabaseCarte
from Dati.Mazzo import Mazzo
from Algoritmi.HillClimbing.HillClimbing import costruisci_mazzo_random_valido

def algoritmo_genetico(
    size_popolazione:int,
    size_mating_pool:int,
    p_mutazione:float,
    p_crossover:float,
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
    n_fisse = len(fisse)
    numero_generazione = 1
    generazione = []

    while i < size_popolazione:
        generazione.append(costruisci_mazzo_random_valido(db, fisse))
        i += 1



    print("---GENERAZIONE INIZIALE----")
    for m in generazione:
        m.stampa_mazzo()
    print()
    new_best_mazzo = max(generazione, key=lambda x: x.calcola_fitness())
    new_best_fitness = new_best_mazzo.calcola_fitness()
    best_fitness = new_best_fitness - 1 #per far in modo che la condizione del while sia vera
    best_mazzo = None

    while best_fitness <= new_best_fitness:
        i = 0
        best_mazzo = new_best_mazzo
        best_fitness = new_best_fitness
        mating_pool = list(selezione(generazione,size_mating_pool))
        generazione.clear()

        while i < size_popolazione:
            genitore1 = mating_pool[i % size_mating_pool] #il primo genitore lo sceglie in ordine
            genitore2 = random.choice(mating_pool) #il secondo genitore viene scelto a caso
            print("genitore1:")
            genitore1.stampa_mazzo()
            print("genitore2:")
            genitore2.stampa_mazzo()
            figlio = crossover(genitore1,genitore2,p_crossover,100,n_fisse)
            print("figlio:")
            figlio.stampa_mazzo()
            figlio = mutazione(figlio,p_mutazione,n_fisse,db)
            print("figlio mutato:")
            figlio.stampa_mazzo()
            print()
            generazione.append(figlio)
            i += 1
        numero_generazione += 1

        new_best_mazzo = max(generazione,key=lambda x: x.calcola_fitness())
        new_best_fitness = new_best_mazzo.calcola_fitness()

        print("---GENERAZIONE NUMERO ",numero_generazione,"---")
        for m in generazione:
            m.stampa_mazzo()
        print()


    return best_mazzo, best_fitness










