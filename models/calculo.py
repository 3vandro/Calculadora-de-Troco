from models.compra import Compra
from models.troco import Troco
import math
from decimal import Decimal, getcontext
### Criação da classe ###

class Atividade:
    def real_para_float(self, real: str) -> float:
        """
        Converte da escrita em real (1,00) para float (1.00)
        :param real: string com o valor no formato real
        :return: o valor no formato float
        """
        return float(real.replace(',', '.'))

    def ler_dados(self) -> Compra:
        valor = input('Informe o valor total das compras: R$ ')
        self.total_compra = self.real_para_float(valor)
        valor = input('Informe o valor recebido: R$ ')
        self.valor_recebido = self.real_para_float(valor)
        return Compra(self.total_compra, self.valor_recebido)

    def troco_real(self) -> Compra:
        return self.valor_recebido - self.total_compra

    def calculo_dinheiro(self) -> Compra:
        getcontext().prec = 6
        troco = Decimal(self.troco_real())
        dinheiro = {}
        if troco > 0:

            while troco > 0:
                if (troco / Decimal(100)) > 0:
                    n100 = troco / Decimal(100)
                    if n100 >= 1:
                        dinheiro["Nota(s) de R$ 100: "] = math.floor(n100)
                        troco = troco - Decimal(100) * math.floor(n100)
                if (troco / 50) > 0:
                    n50 = troco / 50
                    if n50 >= 1:
                        dinheiro["Nota(s) de R$ 50: "] = math.floor(n50)
                        troco = troco - Decimal(50) * math.floor(n50)
                if (troco / 20) > 0:
                    n20 = troco / 20
                    if n20 >= 1:
                        dinheiro["Nota(s) de R$ 20: "] = math.floor(n20)
                        troco = troco - Decimal(20) * math.floor(n20)
                if (troco / 10) > 0:
                    n10 = troco / 10
                    if n10 >= 1:
                        dinheiro["Nota(s) de R$ 10: "] = math.floor(n10)
                        troco = troco - Decimal(10) * math.floor(n10)
                if (troco / 5) > 0:
                    n5 = troco / 5
                    if n5 >= 1:
                        dinheiro["Nota(s) de R$ 5: "] = math.floor(n5)
                        troco = troco - Decimal(5) * math.floor(n5)
                if (troco / 2) > 0:
                    n2 = troco / 2
                    if n2 >= 1:
                        dinheiro["Nota(s) de R$ 2: "] = math.floor(n2)
                        troco = troco - Decimal(2) * math.floor(n2)
                if (troco / 1) > 0:
                    n1 = troco / 1
                    if n1 >= 1:
                        dinheiro["Moeda(s) de R$ 1: "] = math.floor(n1)
                        troco = troco - Decimal(1) * math.floor(n1)
                if (troco / Decimal(0.5) )> 0:
                    n050 = troco / Decimal(0.5)
                    if n050 >= 1:
                        dinheiro["Moeda(s) de R$ 0,50: "] = math.floor(n050)
                        troco = troco - Decimal(0.5) * math.floor(n050)
                if (troco / Decimal(0.25)) > 0:
                    n025 = troco / Decimal(0.25)
                    if n025 >= 1:
                        dinheiro["Moeda(s) de R$ 0,25: "] = math.floor(n025)
                        troco = troco - Decimal(0.25) * math.floor(n025)
                if (troco / Decimal(0.10)) > 0:
                    n010 = troco / Decimal(0.10)
                    if n010 >= 1:
                        dinheiro["Moeda(s) de R$ 0,10: "] = math.floor(n010)
                        troco = troco - Decimal(0.10) * math.floor(n010)
                if (troco / Decimal(0.05)) > 0:
                    n005 = troco / Decimal(0.05)
                    if n005 >= 1:
                        dinheiro["Moeda(s) de R$ 0,05: "] = math.floor(n005)
                        troco = troco - Decimal(0.05) * math.floor(n005)
                if (troco / Decimal(0.01)) >= 0:
                    n001 = troco / Decimal(0.01)
                    if n001 >= 1:
                        dinheiro["Bala(s) (doce): "] = math.floor(n001)
                        troco = troco - Decimal(0.01) * math.floor(n001)
                resultado = [f"{key} {value}" for key, value in dinheiro.items()]
            return resultado
        else:
            dinheiro["Dinheiro a receber"] = 0

    def execute(self) -> None:
        """Responsável por executar o programa da atividade
        """
        compra = self.ler_dados()
        troco = self.troco_real()
        dinheiro = self.calculo_dinheiro()

        print("")
        print("==============RECIBO==============")
        print(compra)
        print("==================================")

        if troco > 0:
            print("O seu troco é de R$", troco)
            print("==================================")
            for item in dinheiro:
                print(item)
        elif troco < 0:
            print(f'FALTA PAGAR R$ {(-1) * troco}')
        elif troco == 0:
            print("Você não tem troco para receber")
        else:
            print("")

