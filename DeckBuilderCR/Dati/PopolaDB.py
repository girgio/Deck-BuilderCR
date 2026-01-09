import csv
from .Carta import Carta
from .Carta import DatabaseCarte

class PopolaDatabase:
    def __init__(self, db: DatabaseCarte, file_csv: str):
        self.db = db
        self.file_csv = file_csv

    def popola_database(self):
        # Apri il file CSV e leggi le righe
        with open(self.file_csv, 'r',encoding='utf-8-sig') as file:
            reader = csv.DictReader(file,delimiter=';')
            for row in reader:
                # Sostituisci la riga del danno_s con questa logica:
                danno_valore = row.get('danno_s', '-1')  # Prende il valore, se manca usa '-1'
                if danno_valore == '':  # Se il campo esiste ma è vuoto
                    danno_valore = '-1'


                vita_valore = row.get('punti_vita', '-1')  # Prende il valore, se manca usa '-1'
                if vita_valore == '':  # Se il campo esiste ma è vuoto
                    vita_valore = '-1'

                velocita_valore = row.get('velocita', '-1')  # Prende il valore, se manca usa '-1'
                if velocita_valore == '':  # Se il campo esiste ma è vuoto
                    velocita_valore = '-1'

                costo_valore = row.get('costo', '-1')  # Prende il valore, se manca usa '-1'
                if costo_valore == '':  # Se il campo esiste ma è vuoto
                    costo_valore = '-1'

                # Crea un'istanza della carta con i dati letti
                carta = Carta(
                    nome=row['nome'],
                    danno_s=int(danno_valore),
                    punti_vita=int(vita_valore),
                    costo=int(costo_valore),
                    volante=row['volante'] == 'True',  # Converti la stringa 'True' in un booleano
                    tipologia=row['tipologia'],
                    velocita=int(velocita_valore),
                    portata=(row['portata']) == 'True',
                    tipo_bersaglio=(row['tipo_bersaglio']) == 'True',
                    effetti_aggiuntivi=int(row['effetti_aggiuntivi'])
                )
                # Aggiungi la carta al database
                self.db.aggiungi_carta(carta)

        print("Database popolato con successo!")