import time

from Mazzo import Mazzo
from DatabaseCarte import DatabaseCarte

db = DatabaseCarte()
carte1 = [db.get_carta("Cavaliere"),db.get_carta("Principe"),db.get_carta("Stregone elletrico"),db.get_carta("Spirito della cura"),db.get_carta("Golem"),
         db.get_carta("Cannone"),db.get_carta("Gigante"),db.get_carta("Scarica")]
carte2 = [db.get_carta("Golem del ghiaccio"),db.get_carta("Berserker"),db.get_carta("Cannone"),db.get_carta("Tesla"),db.get_carta("Arco x"),
         db.get_carta("Gigante elletrico"),db.get_carta("Arciere magico"),db.get_carta("Barile goblin")]
carte3 = [db.get_carta("Strega"),db.get_carta("Cavaliere"),db.get_carta("Pekka"),db.get_carta("Frecce"),db.get_carta("Lapide"),
         db.get_carta("Cacciatore"),db.get_carta("Valchiria"),db.get_carta("Tronco")]
carte4 = [db.get_carta("Scheletri"),db.get_carta("Spirito del ghiaccio"),db.get_carta("Spirito del fuoco"),db.get_carta("Spirito elletrico"),db.get_carta("Goblin"),
         db.get_carta("Spirito della cura"),db.get_carta("Scarica"),db.get_carta("Guardie")]
carte5 = [db.get_carta("Domatrice di arieti"),db.get_carta("Stregone di ghiaccio"),db.get_carta("Gigante elletrico"),db.get_carta("Mascalzoni"),db.get_carta("Palla di neve gigante"),
         db.get_carta("Torre infernale"),db.get_carta("Drago elletrico"),db.get_carta("Strega madre")]
carte6 = [db.get_carta("Tronco"),db.get_carta("Macchina volante"),db.get_carta("Sgherri"),db.get_carta("Spirito del ghiaccio"),db.get_carta("Cacciatore"),
         db.get_carta("Strega"),db.get_carta("Domatore di cinghiali"),db.get_carta("Gran cavaliere")]
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