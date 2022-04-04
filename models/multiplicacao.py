from abstract_models.operacao_abc import Operacao


class Multiplicacao(Operacao):

    def executar(self, num1, num2):

        # essa verificação é necessária pois o operador de multiplicação pode
        # se usado para repetir strings.
        if type(num1) != int or type(num2) != int:
            raise TypeError
        return num1 * num2