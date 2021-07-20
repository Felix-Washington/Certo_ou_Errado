import sys

from controladores.AbstractControlador import AbstractControlador
from visao.Tela import Tela
import pygame
from pygame.locals import *


class ControladorTabuleiro(AbstractControlador):
    def __init__(self):
        self.__tela = Tela()
        self.__imagem_tabuleiro = 'imagens/tabuleiro0.1.png'
        self.__controle = 0

    def tabuleiro_opcoes(self):
        while self.__controle >= 0:
            self.teclado()

            self.__tela.mostra_imagem(self.__imagem_tabuleiro, 0, 0)
            pygame.display.update()

        self.__controle = 0

    def teclado(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.__controle = -1

    def adiciona(self, dados):
        pass

    def remover(self, dados):
        pass

    @property
    def controle(self):
        return self.__controle

    @controle.setter
    def controle(self, valor):
        self.__controle = valor
