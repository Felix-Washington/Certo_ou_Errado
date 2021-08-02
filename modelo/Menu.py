import pygame


class Menu:
    def __init__(self, imagem):
        self.__imagem = imagem
        self.__posicao = [0, 0]
        self.__tamanho = [800, 600]
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)
        self.__ativo = False

    @property
    def rect(self):
        return self.__rect

    @property
    def imagem(self):
        return self.__imagem

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, condicao):
        self.__ativo = condicao
