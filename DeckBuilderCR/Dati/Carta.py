class Carta:
    def __init__(self, nome, danno_s, punti_vita, costo, volante, tipologia, velocita, portata, tipo_bersaglio, effetti_aggiuntivi):
        self.nome = nome
        self.danno_s = danno_s
        self.punti_vita = punti_vita
        self.costo = costo
        self.volante = volante
        self.tipologia = tipologia #truppa,edificio o incantesimo
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

    def carta_da_dict (dati: dict):
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







