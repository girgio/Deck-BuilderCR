import json
from Dati.Carta import Carta

class DatabaseCarte:
    def __init__(self, file_name='database_carte.json'):
        self.file_name = file_name
        self.database = self.carica_database()

    def carica_database(self):
        # Carica il database da un file JSON
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
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

    def get_carta(self, nome: str):
        dati = self.database.get(nome)
        if dati is None:
            return None
        return Carta.carta_da_dict(dati)

    # --- NUOVI METODI UTILI PER HILL CLIMBING ---
    def get_nomi_carte(self):
        return list(self.database.keys())

    def get_tutte_le_carte(self):
        return [Carta.carta_da_dict(d) for d in self.database.values()]

    def mostra_database(self):
        # Mostra tutte le carte nel database
        for nome, carta in self.database.items():
            print(f"{nome}: {carta}")