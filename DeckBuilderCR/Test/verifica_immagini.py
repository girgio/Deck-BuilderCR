"""
Script per verificare quali carte hanno problemi con le immagini
"""
import json
import requests
from Dati.utils import nome_carta_to_url


def verifica_url(url, timeout=3):
    """Verifica se un URL è raggiungibile"""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code == 200
    except:
        return False


def main():
    # Carica database
    with open('../Dati/database_carte.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    print("=" * 80)
    print("🔍 VERIFICA IMMAGINI CARTE")
    print("=" * 80)
    print(f"Totale carte da controllare: {len(db)}\n")

    carte_ok = []
    carte_ko = []

    for nome, carta_data in db.items():
        url = nome_carta_to_url(nome)

        print(f"Verifica: {nome:30s} → ", end="")

        if verifica_url(url):
            print("✅ OK")
            carte_ok.append(nome)
        else:
            print(f"❌ FAIL")
            print(f"         URL: {url}")
            carte_ko.append((nome, url))

    # Riepilogo
    print("\n" + "=" * 80)
    print("📊 RIEPILOGO")
    print("=" * 80)
    print(f"✅ Carte OK: {len(carte_ok)}/{len(db)}")
    print(f"❌ Carte con problemi: {len(carte_ko)}/{len(db)}")

    if carte_ko:
        print("\n" + "=" * 80)
        print("❌ CARTE DA CORREGGERE:")
        print("=" * 80)
        for nome, url in carte_ko:
            print(f"• {nome}")
            print(f"  URL attuale: {url}\n")


if __name__ == "__main__":
    main()
