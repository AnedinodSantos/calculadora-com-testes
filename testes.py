from models.calculadora import Calculadora
from unittest import TestCase, main


class Testes_operacoes(TestCase):


    def teste_soma(self):
        """
        Verifica se o retorno do método calcular está correto quando a operação
        é soma.
        """
        calculadora = Calculadora()

        self.assertEqual(calculadora.calcular("soma", 1, 2), 3)
        self.assertEqual(calculadora.calcular("soma", 10, 5), 15)
        self.assertEqual(calculadora.calcular("soma", 31, 3), 34)


    def teste_subtracao(self):
        """
        Verifica se o retorno do método calcular está correto quando a operação
        é subtração.
        """
        calculadora = Calculadora()
        
        self.assertEqual(calculadora.calcular("subtração", 10, 5), 5)
        self.assertEqual(calculadora.calcular("subtração", 5, 5), 0)
        self.assertEqual(calculadora.calcular("subtração", 5, 10), -5)


    def teste_multiplicacao(self):
        """
        Verifica se o retorno do método calcular está correto quando a operação
        é multiplicação
        """
        calculadora = Calculadora()

        self.assertEqual(calculadora.calcular("multiplicação", 2, 3), 6)
        self.assertEqual(calculadora.calcular("multiplicação", 5, 0), 0)
        self.assertEqual(calculadora.calcular("multiplicação", 1, 1), 1)


    def teste_divisao(self):
        """
        Verifica se o retorno do método calcular está correto quando a operação
        é divisão
        """
        calculadora = Calculadora()

        self.assertEqual(calculadora.calcular("divisão", 10, 5), 2)
        self.assertEqual(calculadora.calcular("divisão", 15, 2), 7.5)
        self.assertEqual(calculadora.calcular("divisão", 2, 1), 2)

    # para esse teste é preciso comentar a proteção com try/except feita no arquivo divisao.py
    # def teste_divisao_por_zero(self):
    #     """
    #     Verificar se o método lança o erro ZeroDivisionError quando passamos 
    #     zero como denominador da divisão.
    #     """
    #     calculadora = Calculadora()

    #     self.assertRaises(ZeroDivisionError, calculadora.calcular, 
    #                       "divisão", 5, 0)


    def teste_tipo_de_dados(self):
        """
        Verificar se o método lança o erro TypeError quando passamos um tipo de
        dados diferente de numeros (int, float, etc).
        """
        calculadora = Calculadora()

        self.assertRaises(TypeError, calculadora.calcular,"soma", "g", 1)
        self.assertRaises(TypeError, calculadora.calcular,"subtração", "g", 1)
        self.assertRaises(TypeError, calculadora.calcular,"multiplicação", "g", 1)
        self.assertRaises(TypeError, calculadora.calcular,"divisão", "g", 1)


if __name__ == "__main__":
    main()
