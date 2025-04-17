class Produto:


    def __init__(self, categoria, produto, quantidade):
        self.categoria = categoria
        self.produto = produto
        self.quantidade = quantidade

    def to_dict(self):
        return {
            'categoria': self.categoria,
            'tipo_produto': self.produto,
            'quantidade': self.quantidade
        }