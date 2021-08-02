import random
import pygame


class Dado:
    def __init__(self):
        self.__posicao = [20, 20]  # 0 = x/ 1 = y
        self.__tamanho = [50, 50]  # 0 = largura / 1 = altura
        self.__numero_atual = 6
        self.__imagem = 'faces_dado/n_6'
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)

    def rodar_dado(self):
        self.__numero_atual = random.choice([1, 2, 3, 4, 5, 6])
        self.__imagem = 'faces_dado/n_' + str(self.__numero_atual)

    @property
    def imagem(self):
        return self.__imagem

    @property
    def posicao(self):
        return self.__posicao

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def rect(self):
        return self.__rect
