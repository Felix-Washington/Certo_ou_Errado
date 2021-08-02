import pygame


class Posicao:

    def __init__(self, x, y, funcao):
        self.__posicao = [x, y]
        self.__tamanho = [80, 80]
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)
        self.__funcao = funcao
        self.__imagem = 'tiles_tabuleiro/' + funcao

    @property
    def posicao(self):
        return self.__posicao

    @property
    def funcao(self):
        return self.__funcao

    @property
    def imagem(self):
        return self.__imagem

    @property
    def rect(self):
        return self.__rect
