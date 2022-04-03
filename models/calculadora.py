from .operacao_fabrica import OperacaoFabrica

class Calculadora():

    def calcular(self, operacao, num1, num2):
        operFab = OperacaoFabrica()
        oper = operFab.criar(operacao)
        return oper.executar(num1, num2)