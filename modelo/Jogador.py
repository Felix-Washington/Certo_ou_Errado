import pygame


class Jogador:
    def __init__(self):
        self.__imagem = ""
        self.__posicao = [100, 420]
        self.__tamanho = [50, 50]
        self.__nome = ""
        self.__rodou_dado = 0
        self.__vez = False
        self.__posicao_tabuleiro = 0
        self.__venceu = False
        self.__rect = pygame.Rect(self.__posicao, self.__tamanho)

    @property
    def imagem(self):
        return self.__imagem

    @property
    def posicao(self):
        return self.__posicao

    @property
    def rodou_dado(self):
        return self.__rodou_dado

    @property
    def vez(self):
        return self.__vez

    @property
    def venceu(self):
        return self.__venceu

    @venceu.setter
    def venceu(self, venceu):
        self.__venceu = venceu

    @property
    def posicao_tabuleiro(self):
        return self.__posicao_tabuleiro

    @posicao_tabuleiro.setter
    def posicao_tabuleiro(self, posicao):
        self.__posicao_tabuleiro = posicao

    @vez.setter
    def vez(self, vez):
        self.__vez = vez

    @rodou_dado.setter
    def rodou_dado(self, rodou):
        self.__rodou_dado = rodou

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem
