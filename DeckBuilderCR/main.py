from Dati.Carta import DatabaseCarte
from Dati.PopolaDB import PopolaDatabase


db = DatabaseCarte()
popolate = PopolaDatabase(db,"Dati/Carte.csv")
PopolaDatabase.popola_database(popolate)