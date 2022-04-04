from abstract_models.operacao_abc import Operacao


class Divisao(Operacao):

    def executar(self, num1, num2):
        #return num1 / num2 
        try: 
            resultado = num1 / num2 
        except ZeroDivisionError:
            return "Divisao por zero"
        return resultado