import random
import pygame


class Dado:
    def __init__(self):
        self.__posicao = [400, 300]  # 0 = x/ 1 = y
        self.__tamanho = [256, 256]  # 0 = largura / 1 = altura
        self.__numero_atual = 0
        self.__imagem = 'faces_dado/n_0'
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)

    def redefinir(self):
        self.__posicao = [20, 20]
        self.__tamanho = [50, 50]
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)

    def rodar_dadog(self):
        self.__numero_atual = random.choice([1, 2, 3, 4, 5, 6])
        self.__imagem = 'faces_dado/n_' + str(self.__numero_atual) + "g"
        return self.__numero_atual

    def rodar_dado(self):
        self.__numero_atual = random.choice([1, 2, 3, 4, 5, 6])
        self.__imagem = 'faces_dado/n_' + str(self.__numero_atual)
        return self.__numero_atual

    @property
    def imagem(self):
        return self.__imagem

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def rect(self):
        return self.__rect
