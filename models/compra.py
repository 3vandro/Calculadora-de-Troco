class Compra:
    def __init__(self, total_compra, valor_recebido):
        self.total_compra = total_compra
        self.valor_recebido = valor_recebido



    def __str__(self):
        """
        ToString representante da classe
        :return: str
        """
        return f"Total dos itens: R$ {self.total_compra}\nValor recebido: R$ {self.valor_recebido}"

