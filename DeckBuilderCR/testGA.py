import random
import time
import os

from Dati.DatabaseCarte import DatabaseCarte
from Algoritmi.GA.Algoritmo import algoritmo_genetico

def mainGA():
    # Seed forte per evitare qualsiasi ripetibilità accidentale
    random.seed(time.time_ns() ^ os.getpid())

    db = DatabaseCarte("Dati/database_carte.json")
    print("Carte disponibili:", len(db.database))

    raw = input(
        "Inserisci da 1 a 4 carte fisse (nomi separati da virgola), "
        "oppure premi Invio per nessuna: "
    ).strip()

    fisse = set()
    if raw:
        fisse = {x.strip() for x in raw.split(",") if x.strip()}
        if not (1 <= len(fisse) <= 4):
            raise ValueError("Devi inserire da 1 a 4 carte fisse.")

    best, fit = algoritmo_genetico(
        size_popolazione = 10,
        size_mating_pool = 10,
        p_mutazione = 0.6,
        p_crossover = 1,
        db = db,
        fisse = fisse,
        seed = None
    )

    print("---MAZZO FINALE---")
    best.stampa_mazzo()

if __name__ == "__main__":
    mainGA()