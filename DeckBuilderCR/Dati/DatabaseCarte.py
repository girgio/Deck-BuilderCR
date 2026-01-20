import json
from Carta import Carta
import random

class DatabaseCarte:
    def __init__(self, file_name='database_carte.json'):
        self.file_name = file_name
        self.database = self.carica_database()

    def carica_database(self):
        # Carica il database da un file JSON
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def salva_database(self):
        # Salva il database su un file JSON
        with open(self.file_name, 'w') as file:
            json.dump(self.database, file, indent=4)

    def aggiungi_carta(self, carta):
        # Aggiunge una nuova carta al database
        self.database[carta.nome] = carta.to_dict()
        self.salva_database()

    def get_carta(self, nome):
        # Restituisce la carta dal database dato il nome
        return Carta.carta_da_dict(self.database.get(nome))

    def mostra_database(self):
        # Mostra tutte le carte nel database
        for nome, carta in self.database.items():
            print(f"{nome}: {carta}")

    def estraizione_casuale(self):
        return Carta.carta_da_dict(random.choice(list(self.database.values())))
