"""
Test per la classe DatabaseCarte
"""
import sys
import os

# Trova la directory root del progetto
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Dati.DatabaseCarte import DatabaseCarte


def test_caricamento_database():
    """Test caricamento database"""
    print("🧪 Test 1: Caricamento database...")

    db_path = os.path.join(parent_dir, 'Dati', 'database_carte.json')

    if not os.path.exists(db_path):
        print(f"  ⚠️  File non trovato: {db_path}")
        return False

    db = DatabaseCarte(db_path)

    assert db.database is not None
    assert isinstance(db.database, dict)

    print(f"  ✅ Database caricato con {len(db.database)} carte")
    return len(db.database) > 0


def test_get_tutte_carte():
    """Test recupero tutte le carte"""
    print("\n🧪 Test 2: Recupero tutte le carte...")

    db_path = os.path.join(parent_dir, 'Dati', 'database_carte.json')
    db = DatabaseCarte(db_path)
    carte = db.get_tutte_le_carte()

    if len(carte) == 0:
        print("  ⚠️  Nessuna carta trovata nel database!")
        return False

    assert len(carte) > 0
    assert hasattr(carte[0], 'nome')
    assert hasattr(carte[0], 'image_url')

    print(f"  ✅ Recuperate {len(carte)} carte")
    return True


def test_get_carta():
    """Test recupero carta singola"""
    print("\n🧪 Test 3: Recupero carta singola...")

    try:
        db_path = os.path.join(parent_dir, 'Dati', 'database_carte.json')
        db = DatabaseCarte(db_path)

        nomi = db.get_nomi_carte()
        if not nomi:
            print("  ⚠️  Database vuoto")
            return False

        primo_nome = nomi[0]
        print(f"  🔍 Cercando carta: {primo_nome}")

        carta = db.get_carta(primo_nome)

        if carta is None:
            print(f"  ❌ Carta '{primo_nome}' non trovata!")
            return False

        print(f"  ✅ Carta trovata: {carta.nome}")
        print(f"     Costo: {carta.costo}")
        print(f"     Tipologia: {carta.tipologia}")
        print(f"     URL: {carta.image_url}")

        assert carta.nome == primo_nome

        return True

    except Exception as e:
        print(f"  ❌ Errore: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_statistiche():
    """Test statistiche database"""
    print("\n🧪 Test 4: Statistiche database...")

    try:
        db_path = os.path.join(parent_dir, 'Dati', 'database_carte.json')
        db = DatabaseCarte(db_path)
        stats = db.get_statistiche()

        assert 'totale' in stats

        if 'costo_medio' in stats:
            print(f"  📊 Totale carte: {stats['totale']}")
            print(f"  📊 Costo medio: {stats['costo_medio']:.2f}")
            print(f"  📊 Truppe: {stats['truppe']}")
            print(f"  📊 Incantesimi: {stats['incantesimi']}")
            print(f"  📊 Edifici: {stats['edifici']}")

        print("  ✅ Statistiche generate")
        return True

    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return False


def test_immagini_prime_10_carte():
    """Test URL immagini delle prime 10 carte"""
    print("\n🧪 Test 5: URL immagini prime 112 carte...")

    try:
        db_path = os.path.join(parent_dir, 'Dati', 'database_carte.json')
        db = DatabaseCarte(db_path)
        carte = db.get_tutte_carte()[:112]

        if not carte:
            print("  ⚠️  Nessuna carta disponibile")
            return False

        print("\n  🖼️  Anteprima immagini:")
        for carta in carte:
            print(f"  • {carta.nome:25s} → {carta.image_url}")

        print("  ✅ URL generati per tutte le carte")
        return True

    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return False


def run_all_tests():
    """Esegue tutti i test"""
    print("=" * 60)
    print("🚀 TEST DATABASE CARTE")
    print("=" * 60)
    print(f"📂 Working directory: {os.getcwd()}")
    print(f"📂 Parent directory: {parent_dir}")
    print(f"📂 Database path: {os.path.join(parent_dir, 'Dati', 'database_carte.json')}")
    print("=" * 60)

    risultati = []

    # Test 1
    risultati.append(("Caricamento", test_caricamento_database()))

    if risultati[0][1]:  # Se il caricamento ha successo
        # Test 2
        risultati.append(("Recupero carte", test_get_tutte_carte()))

        # Test 3
        risultati.append(("Get carta", test_get_carta()))

        # Test 4
        risultati.append(("Statistiche", test_statistiche()))

        # Test 5
        risultati.append(("Immagini", test_immagini_prime_10_carte()))

    print("\n" + "=" * 60)
    print("📊 RIEPILOGO TEST")
    print("=" * 60)

    for nome, risultato in risultati:
        stato = "✅" if risultato else "❌"
        print(f"{stato} {nome}")

    tutti_passati = all(r[1] for r in risultati)

    print("=" * 60)
    if tutti_passati:
        print("✅ TUTTI I TEST PASSATI!")
    else:
        print("⚠️  ALCUNI TEST FALLITI")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
