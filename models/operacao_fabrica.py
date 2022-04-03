from .soma import Soma
from .subtracao import Subtracao
from .multiplicacao import Multiplicacao
from .divisao import Divisao

class OperacaoFabrica():

    def criar(self, operacao):
        if operacao == "soma":
            return Soma()
        if operacao == "subtração":
            return Subtracao()
        if operacao == "multiplicação":
            return Multiplicacao()
        if operacao == "divisão":
            return Divisao()