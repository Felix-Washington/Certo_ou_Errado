from pygame import QUIT

from controladores.AbstractControlador import AbstractControlador
from visao.Tela import Tela
import pygame
import sys
from pygame.locals import *


class ControladorMenu(AbstractControlador):
    def __init__(self):
        super().__init__()
        self.__tela = Tela()
        self.__ponteiro_x = 200
        self.__ponteiro_y = 100
        self.__ponteiro_max = 575
        self.__menu_imagem = 'imagens/menu.png'
        self.__creditos_imagem = 'imagens/tela_creditos.png'
        self.__opcoes_imagem = 'imagens/tela_opcoes.png'
        self.__ponteiro_imagem = 'imagens/ufo.png'
        self.__controle_menu = 0

    def menu_opcoes(self):

        while self.__controle_menu >= 0:
            self.teclado()

            if self.__ponteiro_y > self.__ponteiro_max:
                self.__ponteiro_y = 100
            elif self.__ponteiro_y < 100:
                self.__ponteiro_y = self.__ponteiro_max - 100

            if self.__controle_menu == 0:
                self.__tela.mostra_imagem(self.__menu_imagem, 0, 0)
                self.__tela.mostra_imagem(self.__ponteiro_imagem, self.__ponteiro_x, self.__ponteiro_y)

            elif self.__controle_menu == 1:
                self.creditos()
                self.__tela.mostra_imagem(self.__creditos_imagem, 0, 0)

            elif self.__controle_menu == 2:
                self.__tela.mostra_imagem(self.__opcoes_imagem, 0, 0)

            pygame.display.update()

    def teclado(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.__ponteiro_y += 125
                elif event.key == K_UP:
                    self.__ponteiro_y -= 125

                elif event.key == K_SPACE:
                    if self.__ponteiro_y == 100:
                        self.__controle_menu = -1
                    elif self.__ponteiro_y == 225:
                        self.__controle_menu = 1
                    elif self.__ponteiro_y == 350:
                        self.__controle_menu = 2
                    elif self.__ponteiro_y == 475:
                        self.__controle_menu = -2

                elif event.key == K_ESCAPE:
                    if self.__controle_menu == 1 or self.__controle_menu == 2:
                        self.__controle_menu = 0

    def creditos(self):
        pass

    def adiciona(self, dados):
        return 0
        pass

    def remover(self, dados):
        pass

    def atualiza(self, dados):
        pass

    @property
    def controle_menu(self):
        return self.__controle_menu

    @controle_menu.setter
    def controle_menu(self, valor):
        self.__controle_menu = valor
