import pygame


class Carta:

    def __init__(self, perguntas):
        self.__posicao = [680, 200]
        self.__tamanho = [120, 160]
        self.__imagem = "carta_baixo"
        self.__imagem_fechar = "fechar_carta"
        self.__perguntas = perguntas
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)
        # self.__rect_fechar = pygame.Rect()

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho
