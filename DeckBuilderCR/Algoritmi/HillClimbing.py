from __future__ import annotations

import random
from typing import Set, Tuple, Optional, List

from Dati.Mazzo import Mazzo
from Dati.DatabaseCarte import DatabaseCarte


def _conteggio_incantesimi_da_nomi(db: DatabaseCarte, nomi: List[str]) -> int:
    cnt = 0
    for n in nomi:
        c = db.get_carta(n)
        if c is None:
            continue
        if str(c.tipologia).casefold() == "incantesimo":
            cnt += 1
    return cnt


def costruisci_mazzo_random_valido(
    db: DatabaseCarte,
    fisse: Set[str],
    max_tentativi: int = 2000
) -> Mazzo:
    """
    Costruisce un mazzo valido casuale che contiene tutte le carte fisse.
    Vincoli: 8 carte, no doppioni, max 2 incantesimi.
    """
    nomi_db = db.get_nomi_carte()
    if len(nomi_db) < 8:
        raise ValueError("Database carte troppo piccolo: servono almeno 8 carte.")

    # Validazione fisse
    fisse = {n.strip() for n in fisse if n and n.strip()}
    for n in fisse:
        if db.get_carta(n) is None:
            raise ValueError(f"Carta fissa non trovata nel database: '{n}'")

    if len(fisse) > 4:
        raise ValueError("Puoi fissare al massimo 4 carte.")
    if len(fisse) > 8:
        raise ValueError("Troppe carte fisse: un mazzo ha solo 8 carte.")

    fisse_list = list(fisse)
    inc_fisse = _conteggio_incantesimi_da_nomi(db, fisse_list)
    if inc_fisse > 2:
        raise ValueError("Le carte fisse contengono più di 2 incantesimi: impossibile rispettare il vincolo.")

    # Prova a completare il mazzo random
    disponibili = [n for n in nomi_db if n not in fisse]
    for _ in range(max_tentativi):
        scelti = list(fisse_list)

        # completamento con vincolo incantesimi
        random.shuffle(disponibili)
        inc = inc_fisse

        for candidato_nome in disponibili:
            if len(scelti) == 8:
                break

            carta = db.get_carta(candidato_nome)
            if carta is None:
                continue

            # controlla vincolo incantesimi
            if str(carta.tipologia).casefold() == "incantesimo":
                if inc >= 2:
                    continue
                inc += 1

            scelti.append(candidato_nome)

        if len(scelti) == 8:
            carte = [db.get_carta(n) for n in scelti]
            if any(c is None for c in carte):
                continue
            mazzo = Mazzo(carte)  # is_valido dentro lo controlli dopo
            if mazzo.is_valido():
                return mazzo

    raise RuntimeError("Non sono riuscito a costruire un mazzo valido casuale (troppi vincoli o dataset incoerente).")


def _stampa_mazzo(mazzo: Mazzo, titolo: str = "Mazzo") -> None:
    print(f"\n=== {titolo} ===")
    print(f"Fitness: {mazzo.caclola_fitness():.4f}")
    print("Carte:")
    for c in mazzo.carte:
        print(f"- {c.nome} ({c.tipologia}, costo={c.costo})")


def hill_climbing(
    mazzo_iniziale: Mazzo,
    db: DatabaseCarte,
    fisse: Set[str],
    max_iter: int = 200,
    neighbors_per_iter: int = 60,
    max_stalli: int = 30,
    usa_restart: bool = True,
    seed: Optional[int] = None,
    stampa_finale: bool = True
) -> Tuple[Mazzo, float]:
    if seed is not None:
        random.seed(seed)

    fisse = {n.strip() for n in fisse if n and n.strip()}

    nomi_iniziali = {c.nome for c in mazzo_iniziale.carte}
    mancanti = [n for n in fisse if n not in nomi_iniziali]
    if mancanti:
        raise ValueError(
            "Hai fissato carte che non sono nel mazzo iniziale: "
            + ", ".join(mancanti)
        )

    if not mazzo_iniziale.is_valido():
        raise ValueError("Il mazzo iniziale non è valido.")

    nomi_db = db.get_nomi_carte()
    if len(nomi_db) < 8:
        raise ValueError("Database carte troppo piccolo: servono almeno 8 carte.")

    corrente = mazzo_iniziale
    best = mazzo_iniziale
    best_fit = best.caclola_fitness()

    stall = 0

    for step in range(1, max_iter + 1):
        corrente_fit = corrente.caclola_fitness()

        deck_nomi = [c.nome for c in corrente.carte]
        deck_set = set(deck_nomi)

        sostituibili = [n for n in deck_nomi if n not in fisse]
        if not sostituibili:
            break

        inseribili = [n for n in nomi_db if n not in deck_set]
        if not inseribili:
            break

        best_neighbor = None
        best_neighbor_fit = corrente_fit

        for _ in range(neighbors_per_iter):
            out_nome = random.choice(sostituibili)
            in_nome = random.choice(inseribili)

            candidato = corrente.sostituisci_carta(out_nome, in_nome, db)
            if not candidato:
                continue

            fit = candidato.caclola_fitness()
            if fit > best_neighbor_fit:
                best_neighbor_fit = fit
                best_neighbor = candidato

        if best_neighbor is not None:
            corrente = best_neighbor
            stall = 0

            if best_neighbor_fit > best_fit:
                best = best_neighbor
                best_fit = best_neighbor_fit
        else:
            stall += 1

        if usa_restart and stall >= max_stalli:
            corrente = costruisci_mazzo_random_valido(db, fisse)
            stall = 0

    if stampa_finale:
        _stampa_mazzo(best, titolo=f"Best finale dopo {max_iter} iterazioni")

    return best, best_fit
