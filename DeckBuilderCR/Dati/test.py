import time

from Mazzo import Mazzo
from DatabaseCarte import DatabaseCarte

db = DatabaseCarte()
carte1 = [db.get_carta("Cavaliere"),db.get_carta("Capanna goblin"),db.get_carta("Razzo"),db.get_carta("Scheletri"),db.get_carta("Minatore"),
         db.get_carta("Megasgherro"),db.get_carta("Gigante"),db.get_carta("Arciere magico")]
carte2 = [db.get_carta("Golem"),db.get_carta("Mastino lavico"),db.get_carta("Pekka"),db.get_carta("Reclute royale"),db.get_carta("Scintilla"),
         db.get_carta("Gigante elletrico"),db.get_carta("Gran cavaliere"),db.get_carta("Imperatrice degli spiriti")]
carte3 = [db.get_carta("Fulmine"),db.get_carta("Mastino lavico"),db.get_carta("Pekka"),db.get_carta("Reclute royale"),db.get_carta("Scintilla"),
         db.get_carta("Gigante elletrico"),db.get_carta("Gigante scheletro"),db.get_carta("Imperatrice degli spiriti")]
carte4 = [db.get_carta("Scheletri"),db.get_carta("Spirito del ghiaccio"),db.get_carta("Spirito del fuoco"),db.get_carta("Spirito elletrico"),db.get_carta("Goblin"),
         db.get_carta("Spirito della cura"),db.get_carta("Scarica"),db.get_carta("Guardie")]
carte5 = [db.get_carta("Domatrice di arieti"),db.get_carta("Stregone di ghiaccio"),db.get_carta("Gigante elletrico"),db.get_carta("Mascalzoni"),db.get_carta("Palla di neve gigante"),
         db.get_carta("Torre infernale"),db.get_carta("Drago elletrico"),db.get_carta("Strega madre")]
carte6 = [db.get_carta("Gigante royale"),db.get_carta("Barile goblin"),db.get_carta("Sgherri"),db.get_carta("Strega"),db.get_carta("Stregone"),
         db.get_carta("Scarica"),db.get_carta("Tesla"),db.get_carta("Orda di scheletri")]
deck = Mazzo(carte1)
deck2 = Mazzo(carte2)
deck3 = Mazzo(carte3)
deck4 = Mazzo(carte4)
deck5 = Mazzo(carte5)
deck6 = Mazzo(carte6)
print(deck.calcola_fitness())
print(deck2.calcola_fitness())
print(deck3.calcola_fitness())
print(deck4.calcola_fitness())
print(deck5.calcola_fitness())
print(deck6.calcola_fitness())

start = time.perf_counter()
while(True):
    mazzo_random = Mazzo.mazzo_random()
    lista= []
    lista = mazzo_random.carte

    if (mazzo_random.calcola_fitness() > 60):
        break
print()
print("Carte nel mazzo random:")

for carta in lista:
    print(carta.nome)

print(mazzo_random.calcola_fitness())
end = time.perf_counter()
print(end - start)