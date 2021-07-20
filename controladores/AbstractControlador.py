from abc import ABC
from abc import abstractmethod


class AbstractControlador(ABC):

    @abstractmethod
    def adiciona(self, dados):
        pass

    @abstractmethod
    def remover(self, dados):
        pass

    def atualiza(self, dados):
        pass
