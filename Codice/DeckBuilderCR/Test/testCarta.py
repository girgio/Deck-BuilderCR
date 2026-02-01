"""
Test per la classe Carta
"""
import sys
import os

# Aggiungi la directory parent al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dati.Carta import Carta


def test_creazione_carta():
    """Test creazione base di una carta"""
    print("🧪 Test 1: Creazione carta...")

    carta = Carta(
        nome="Cavaliere",
        danno_s=170,
        punti_vita=1800,
        costo=3,
        volante=False,
        tipologia="truppa",
        velocita=1,
        portata=False,
        tipo_bersaglio=False,
        effetti_aggiuntivi=0
    )

    assert carta.nome == "Cavaliere"
    assert carta.costo == 3
    assert carta.tipologia == "truppa"
    print(f"  ✅ Carta creata: {carta.nome}")


def test_image_url():
    """Test generazione URL immagine"""
    print("\n🧪 Test 2: URL immagine...")

    carte_test = [
        ("Cavaliere", "knight"),
        ("Baby Dragon", "baby-dragon"),
        ("P.E.K.K.A", "pekka"),
        ("Spirito del fuoco", "fire-spirit")
    ]

    for nome, slug_atteso in carte_test:
        carta = Carta(nome, 100, 500, 3, False, "truppa", 1, False, False, 0)
        url = carta.image_url
        print(f"  {nome} → {url}")
        assert "cdn.royaleapi.com" in url
        assert slug_atteso in url

    print("  ✅ URL generati correttamente")


def test_proprieta():
    """Test proprietà aggiuntive"""
    print("\n🧪 Test 3: Proprietà (elixir, rarità)...")

    carta = Carta("Test", 100, 500, 4, False, "truppa", 1, False, False, 0)

    assert carta.elixir == carta.costo
    assert carta.rarita in ["Common", "Rare", "Epic", "Legendary"]

    print(f"  Elixir: {carta.elixir}")
    print(f"  Rarità: {carta.rarita}")
    print("  ✅ Proprietà funzionanti")


def test_to_dict():
    """Test conversione a dizionario"""
    print("\n🧪 Test 4: Conversione to_dict()...")

    carta = Carta("Goblin", 150, 300, 2, False, "truppa", 3, False, False, 0)
    dati = carta.to_dict()

    assert isinstance(dati, dict)
    assert dati['nome'] == "Goblin"
    assert dati['costo'] == 2

    print(f"  ✅ Dizionario: {dati}")


def test_carta_da_dict():
    """Test creazione carta da dizionario"""
    print("\n🧪 Test 5: Carta da dizionario...")

    dati = {
        'nome': 'Arcieri',
        'danno_s': 120,
        'punti_vita': 252,
        'costo': 3,
        'volante': False,
        'tipologia': 'truppa',
        'velocita': 1,
        'portata': True,
        'tipo_bersaglio': False,
        'effetti_aggiuntivi': 0
    }

    carta = Carta.carta_da_dict(dati)

    assert carta.nome == "Arcieri"
    assert carta.costo == 3
    assert carta.portata == True

    print(f"  ✅ Carta ricostruita: {carta.nome}")


def run_all_tests():
    """Esegue tutti i test"""
    print("=" * 60)
    print("🚀 TEST CLASSE CARTA")
    print("=" * 60)

    try:
        test_creazione_carta()
        test_image_url()
        test_proprieta()
        test_to_dict()
        test_carta_da_dict()

        print("\n" + "=" * 60)
        print("✅ TUTTI I TEST PASSATI!")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n❌ TEST FALLITO: {e}")
    except Exception as e:
        print(f"\n❌ ERRORE: {e}")


if __name__ == "__main__":
    run_all_tests()
