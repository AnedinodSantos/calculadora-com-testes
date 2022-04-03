from abc import ABC, abstractmethod


class Operacao(ABC):

    @abstractmethod
    def executar(self, num1, num2):
        pass