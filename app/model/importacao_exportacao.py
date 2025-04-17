class importacao_exportacao:


    def __init__(self, pais, quantidade_kg, valor_usd):
        self.pais = pais
        self.quantidade_kg = quantidade_kg
        self.valor_usd = valor_usd

    def to_dict(self):
        return {
            'pais': self.pais,
            'quantidade_kg': self.quantidade_kg,
            'valor_usd': self.valor_usd
        }