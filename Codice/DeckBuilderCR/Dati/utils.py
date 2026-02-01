"""
Utility per mappare nomi carte italiane → URL immagini inglesi
Mapping completo e testato per Clash Royale - VERSIONE CORRETTA
"""

# Mapping completo ITA → ENG (slug URL)
MAPPING_CARTE = {
    # Spiriti
    "Spirito elettrico": "electro-spirit",
    "Spirito del fuoco": "fire-spirit",
    "Spirito della cura": "heal-spirit",
    "Spirito del ghiaccio": "ice-spirit",

    # Scheletri
    "Scheletri": "skeletons",
    "Orda di scheletri": "skeleton-army",
    "Barile d'ossa": "skeleton-barrel",
    "Gigante scheletro": "giant-skeleton",

    # Goblin
    "Goblin": "goblins",
    "Goblin lancieri": "spear-goblins",
    "Goblin cerbottaniere": "dart-goblin",
    "Gang di goblin": "goblin-gang",
    "Barile goblin": "goblin-barrel",
    "Capanna goblin": "goblin-hut",
    "Gabbia per goblin": "goblin-cage",
    "Trivella goblin": "goblin-drill",
    "Goblin demolitore": "goblin-demolisher",
    "Macchina goblin": "goblin-machine",
    "Gigante goblin": "goblin-giant",

    # Barbari/Berserker
    "Berserker": "berserker",
    "Barbari": "barbarians",
    "Barbari elite": "elite-barbarians",
    "Capanna dei barbari": "barbarian-hut",
    "Barile Barbarico": "barbarian-barrel",

    # Base
    "Bombarolo": "bomber",
    "Pipistrelli": "bats",
    "Specchio": "mirror",

    # Cavalieri
    "Cavaliere": "knight",
    "Gran cavaliere": "mega-knight",

    # Arcieri
    "Arcieri": "archers",
    "Arciere magico": "magic-archer",
    "Arciere pirotecnico": "firecracker",
    "Cespuglio sospetto": "suspicious-bush",

    # Giganti - ✅ FIX PRINCIPALE
    "Gigante": "giant",
    "Gigante royale": "royal-giant",
    "Gigante elettrico": "electro-giant",
    "Gigantessa delle rune": "rune-giant",

    # PEKKA
    "Mini pekka": "mini-pekka",
    "Pekka": "pekka",

    # Maghi/Stregoni
    "Stregone": "wizard",
    "Stregone elettrico": "electro-wizard",
    "Stregone di ghiaccio": "ice-wizard",

    # Streghe
    "Strega": "witch",
    "Strega notturna": "night-witch",
    "Strega madre": "mother-witch",

    # Draghi
    "Cucciolo di drago": "baby-dragon",
    "Drago infernale": "inferno-dragon",
    "Drago elettrico": "electro-dragon",
    "Draghi d'ossa": "skeleton-dragons",

    # Principi
    "Principe": "prince",
    "Principe nero": "dark-prince",
    "Principessa": "princess",

    # Altri personaggi
    "Valchiria": "valkyrie",
    "Cacciatore": "hunter",
    "Boscaiolo": "lumberjack",
    "Minatore": "miner",
    "Fuorilegge": "bandit",
    "Pescatore": "fisherman",
    "Boia": "executioner",
    "Bocciatore": "bowler",
    "Moschettiere": "musketeer",
    "Tre moschettieri": "three-musketeers",

    # Sgherri/Maiali -
    "Sgherri": "minions",
    "Scariccucioli": "zappies",
    "Megasgherro": "mega-minion",
    "Maiali royale": "royal-hogs",
    "Orda di sgherri": "minion-horde",
    "Domatore di cinghiali": "hog-rider",

    # Guardie e reclute
    "Guardie": "guards",
    "Reclute royale": "royal-recruits",
    "Mascalzoni": "rascals",

    # Arieti
    "Ariete da battaglia": "battle-ram",
    "Domatrice di arieti": "ram-rider",

    # Golem
    "Golem": "golem",
    "Golem del ghiaccio": "ice-golem",
    "Golem di elisir": "elixir-golem",

    # Fantasmi e spiriti
    "Fantasma royale": "royal-ghost",
    "Imperatrice degli spiriti": "spirit-empress",

    # Cani/Mastini
    "Mastino lavico": "lava-hound",

    # Varie creature
    "Guaitrice guerriera": "battle-healer",
    "Fenice": "phoenix",
    "Scintilla": "sparky",
    "Spaccamuro": "wall-breakers",

    # Edifici - Torri
    "Torre infernale": "inferno-tower",
    "Torre bombardiera": "bomb-tower",
    "Tesla": "tesla",
    "Cannone": "cannon",
    "Cannone a rotelle": "cannon-cart",  # ✅ FIX: typo corretto
    "Cannoe a rotelle": "cannon-cart",  # ✅ FIX: fallback per typo nel DB

    # Edifici - Capanne/Spawner
    "Fornace": "furnace",
    "Lapide": "tombstone",
    "Cimitero": "graveyard",

    # Edifici - Altri
    "Arco x": "x-bow",
    "Mortaio": "mortar",
    "Estrattore di elisir": "elixir-collector",

    # Macchine
    "Macchina volante": "flying-machine",

    # Incantesimi - Danni
    "Frecce": "arrows",
    "Palla di fuoco": "fireball",
    "Fulmine": "lightning",
    "Razzo": "rocket",
    "Scarica": "zap",
    "Palla di neve gigante": "giant-snowball",
    "Terremoto": "earthquake",
    "Consegna royale": "royal-delivery",

    # Incantesimi - Controllo
    "Tornado": "tornado",
    "Congelamento": "freeze",
    "Veleno": "poison",
    "Groviglio": "vines",
    "Vuoto": "void",
    "Maledizione goblin": "goblin-curse",

    # Incantesimi - Buff
    "Furia": "rage",
    "Clonazione": "clone",

    # Speciali
    "Tronco": "the-log",
    "Mongolfiera": "balloon",
}


def nome_carta_to_url(nome_carta: str) -> str:
    """
    Converte nome carta italiano in URL immagine CDN
    Args:
        nome_carta: Nome italiano della carta
    Returns:
        URL immagine da RoyaleAPI CDN
    """
    # Cerca nel mapping
    slug = MAPPING_CARTE.get(nome_carta)

    # Se non trovato, fallback a conversione automatica
    if not slug:
        slug = nome_carta.lower()
        slug = slug.replace(" ", "-")
        slug = slug.replace("'", "")
        slug = slug.replace("'", "")

    return f"https://cdn.royaleapi.com/static/img/cards-150/{slug}.png"
