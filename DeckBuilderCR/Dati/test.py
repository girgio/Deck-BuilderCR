from Mazzo import Mazzo
from Carta import Carta
from Carta import DatabaseCarte

db = DatabaseCarte()
carte1 = [db.get_carta("Cavaliere"),db.get_carta("Capanna goblin"),db.get_carta("Razzo"),db.get_carta("Scheletri"),db.get_carta("Minatore"),
         db.get_carta("Megasgherro"),db.get_carta("Gigante"),db.get_carta("Arciere magico")]
carte2 = [db.get_carta("Golem"),db.get_carta("Mastino lavico"),db.get_carta("Pekka"),db.get_carta("Reclute royale"),db.get_carta("Scintilla"),
         db.get_carta("Gigante elletrico"),db.get_carta("Gran cavaliere"),db.get_carta("Imperatrice degli spiriti")]
carte3 = [db.get_carta("Fulmine"),db.get_carta("Mastino lavico"),db.get_carta("Pekka"),db.get_carta("Reclute royale"),db.get_carta("Scintilla"),
         db.get_carta("Gigante elletrico"),db.get_carta("Gigante scheletro"),db.get_carta("Imperatrice degli spiriti")]
carte4 = [db.get_carta("Scheletri"),db.get_carta("Spirito del ghiaccio"),db.get_carta("Spirito del fuoco"),db.get_carta("Spirito elletrico"),db.get_carta("Goblin"),
         db.get_carta("Spirito della cura"),db.get_carta("Scarica"),db.get_carta("Guardie")]
deck = Mazzo(carte1)
deck2 = Mazzo(carte2)
deck3 = Mazzo(carte3)
deck4 = Mazzo(carte4)
print(deck.caclola_fitness())
print(deck2.caclola_fitness())
print(deck3.caclola_fitness())
print(deck4.caclola_fitness())
