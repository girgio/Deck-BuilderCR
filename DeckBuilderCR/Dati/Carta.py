import json

class Carta:
    def __init__(self, nome, danno_s, punti_vita, costo, volante, tipologia, velocita, portata, tipo_bersaglio, effetti_aggiuntivi):
        self.nome = nome
        self.danno_s = danno_s
        self.punti_vita = punti_vita
        self.costo = costo
        self.volante = volante
        self.tipologia = tipologia #truppa,edificio o incantersimo
        self.velocita = velocita
        self.portata = portata
        self.tipo_bersaglio = tipo_bersaglio
        self.effetti_aggiuntivi = effetti_aggiuntivi

    def to_dict(self):
        # Converte l'oggetto carta in un dizionario
        return {
            'nome': self.nome,
            'danno_s': self.danno_s,
            'punti_vita': self.punti_vita,
            'costo': self.costo,
            'volante': self.volante,
            'tipologia': self.tipologia,
            'velocita': self.velocita,
            'portata': self.portata,
            'tipo_bersaglio': self.tipo_bersaglio,
            'effetti_aggiuntivi': self.effetti_aggiuntivi
        }

    def carta_da_dict(dati: dict):
        return Carta(
            nome=dati['nome'],
            danno_s=dati['danno_s'],
            punti_vita=dati['punti_vita'],
            costo=dati['costo'],
            volante=dati['volante'],
            tipologia=dati['tipologia'],
            velocita=dati['velocita'],
            portata=dati['portata'],
            tipo_bersaglio=dati['tipo_bersaglio'],
            effetti_aggiuntivi=dati['effetti_aggiuntivi'])

    def __repr__(self):
        return f"Carta(nome={self.nome}, danno_s={self.danno_s}, punti_vita={self.punti_vita}, costo={self.costo}, volante={self.volante}, tipologia={self.tipologia}, velocita={self.velocita}, portata={self.portata}, tipo_bersaglio={self.tipo_bersaglio}, effetti_aggiuntivi={self.effetti_aggiuntivi})"

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





