from .compra import Compra
#criar uma nova classe para troco e qu importe os dados de compra

class Troco:
    def __init__(self, total, recebido):
        self.total = self.total_compra
        self.recebido = self.valor_recebido

    def troco_real(self) -> Compra:
        if self.recebido > self.total:
            return self.recebido - self.total
        elif self.recebido == self.total:
            return f'Sem troco a receber'
        elif self.recebido < self.total:
            return f'Valor incompleto, faltam {self.total - self.recebido}'



