import random
import time
import os

from Dati.DatabaseCarte import DatabaseCarte
from Algoritmi.HillClimbing.HillClimbing import hill_climbing, costruisci_mazzo_random_valido


def main():
    # Seed forte per evitare qualsiasi ripetibilità accidentale
        random.seed(time.time_ns() ^ os.getpid())

        db = DatabaseCarte("../Dati/database_carte.json")

        raw = input(
            "Inserisci da 1 a 4 carte fisse (nomi separati da virgola), "
            "oppure premi Invio per nessuna: "
        ).strip()

        fisse = set()
        if raw:
            fisse = {x.strip() for x in raw.split(",") if x.strip()}
            if not (1 <= len(fisse) <= 4):
                raise ValueError("Devi inserire da 1 a 4 carte fisse.")

        #MAZZO INIZIALE CASUALE
        mazzo_iniziale = costruisci_mazzo_random_valido(db, fisse)

        print("\n==============================")
        print("MAZZO INIZIALE")
        print("==============================")
        print([c.nome for c in mazzo_iniziale.carte])

        best, fit = hill_climbing(
            mazzo_iniziale=mazzo_iniziale,
            db=db,
            fisse=fisse,
            max_iter=200,
            neighbors_per_iter=60,
            max_stalli=30,
            usa_restart=True,
            seed=None,
            stampa_finale=False
        )

        print("\n==============================")
        print("MAZZO FINALE")
        print("==============================")
        print([c.nome for c in best.carte])
        print("FITNESS:", fit)


if __name__ == "__main__":
    main()