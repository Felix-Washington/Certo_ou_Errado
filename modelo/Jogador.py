import pygame


class Jogador:
    def __init__(self):
        self.__imagem = ""
        self.__posicao = [0, 0]
        self.__tamanho = [50, 50]
        self.__nome = ""
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem
