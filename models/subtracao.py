from abstract_models.operacao_abc import Operacao


class Subtracao(Operacao):

    def executar(self, num1, num2):
        return num1 - num2