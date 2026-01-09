from Mazzo import Mazzo
from Carta import Carta
from Carta import DatabaseCarte

db = DatabaseCarte()
carte = [db.get_carta("Boscaiolo"),db.get_carta("Mongolfiera"),db.get_carta("Scarica"),db.get_carta("Orda di scheletri"),db.get_carta("Moschettiere"),
         db.get_carta("Stregone elletrico"),db.get_carta("Gran cavaliere"),db.get_carta("Spirito del ghiaccio")]
deck = Mazzo(carte)
print(deck.get_costo_medio())
print(deck.get_danno_medio())
print(deck.get_vita_medio())
print(deck.get_velocita_medio())
print(deck.get_edifici())
print(deck.get_incantesimi())
print(deck.is_valido())

