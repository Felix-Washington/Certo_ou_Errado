from abc import ABC
from abc import abstractmethod
import pygame


class AbstractControlador():
    def __init__(self):
        self.__posicao_mouse = pygame.mouse.get_pos()

    @abstractmethod
    def adiciona(self, dados):
        pass

    @abstractmethod
    def remover(self, dados):
        pass

    def atualiza(self, dados):
        pass

    def posicao_mouse(self):
        return self.__posicao_mouse
