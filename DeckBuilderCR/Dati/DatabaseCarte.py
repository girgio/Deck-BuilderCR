import json
import random

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

    def get_tutte_carte(self):
        """Alias per get_tutte_le_carte() - per compatibilità con GUI"""
        return self.get_tutte_le_carte()

    def get_carta_by_nome(self, nome: str):
        """Alias per get_carta() - per compatibilità con GUI"""
        return self.get_carta(nome)

    def mostra_database(self):
        # Mostra tutte le carte nel database
        for nome, carta in self.database.items():
            print(f"{nome}: {carta}")

    def estraizione_casuale(self):
        if not self.database:
            raise ValueError("DatabaseCarte è vuoto: impossibile estrarre una carta casuale")
        return Carta.carta_da_dict(random.choice(list(self.database.values())))

        # --- METODI AGGIUNTIVI UTILI PER GUI ---
    def get_carte_by_costo(self, costo: int):
            """Filtra carte per costo elixir"""
            return [c for c in self.get_tutte_le_carte() if c.costo == costo]

    def get_carte_by_tipologia(self, tipologia: str):
            """Filtra carte per tipologia (truppa, incantesimo, edificio)"""
            return [c for c in self.get_tutte_le_carte() if c.tipologia == tipologia]

    def get_statistiche(self):
            """Restituisce statistiche sul database"""
            carte = self.get_tutte_le_carte()
            if not carte:
                return {}

            return {
                'totale': len(carte),
                'costo_medio': sum(c.costo for c in carte if c.costo > 0) / len([c for c in carte if c.costo > 0]),
                'truppe': len([c for c in carte if c.tipologia == 'truppa']),
                'incantesimi': len([c for c in carte if c.tipologia == 'incantesimo']),
                'edifici': len([c for c in carte if c.tipologia == 'edificio'])
            }