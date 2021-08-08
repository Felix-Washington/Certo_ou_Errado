from pygame import QUIT

from controladores.AbstractControlador import AbstractControlador
from visao.Tela import Tela
from modelo.Menu import Menu
import pygame
import sys
from pygame.locals import *


class ControladorMenu(AbstractControlador):
    def __init__(self):
        super().__init__()

        self.__tela = Tela()
        self.__posicao_ponteiro = [200, 100]
        self.__ponteiro_max = 575
        self.__ponteiro_imagem = 'ufo.png'
        self.__controle_menu = 0
        self.__posicao_mouse = pygame.mouse.get_pos()
        self.__menus = {}
        self.__rects = {}
        self.criar_menus()
        self.__menu_selecionado = 0

    def criar_menus(self):
        caminho = 'menus/'
        imagens = {0: caminho + 'menu', 1: caminho + 'creditos', 2: caminho + 'opcoes', 3: 'ufo'}
        rect_pos = [240, 80]
        rect_tam = [343, 79]

        for i in range(4):
            self.__menus[i] = Menu(imagens[i])
            self.__rects[i] = pygame.Rect([rect_pos[0], rect_pos[1]], [rect_tam[0], rect_tam[1]])

            rect_pos[1] += 25 + rect_tam[1]

    def menu_opcoes(self):
        while self.__controle_menu >= 0:
            self.checar_evento()

            if self.__controle_menu == 1:
                print("tes")
                self.opcoes()

            self.desenhar()
            pygame.display.update()

    def checar_evento(self):
        for evento in pygame.event.get():
            self.teclado(evento)
            self.mouse(evento)

    def desenhar(self):
        self.__tela.mostra_imagem(self.__menus[self.__menu_selecionado].imagem, [0, 0])

    def opcoes(self):
        pass

    def teclado(self, evento):
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                self.__menu_selecionado = 0
                if self.__controle_menu == 1 or self.__controle_menu == 2:
                    self.__controle_menu = 0

    def mouse(self, evento):
        self.__posicao_mouse = pygame.mouse.get_pos()
        if evento.type == MOUSEBUTTONDOWN:

            if self.__controle_menu == 0:
                for c, rect in self.__rects.items():
                    if rect.collidepoint(self.__posicao_mouse):
                        if c == 0:
                            self.__controle_menu = -1
                        elif c == 3:
                            self.__controle_menu = -2
                        elif c == 1:
                            self.__controle_menu = 1
                        elif c == 2:
                            # self.__controle_menu = 2
                            pass
                            # self.__menu_selecionado = c
            elif self.__controle_menu > 0:
                pass

    def adiciona(self, dados):
        pass

    def remover(self, dados):
        pass

    @property
    def controle_menu(self):
        return self.__controle_menu

    @controle_menu.setter
    def controle_menu(self, valor):
        self.__controle_menu = valor
