import sys

from controladores.ControladorMenu import ControladorMenu
from controladores.ControladorTabuleiro import ControladorTabuleiro
from visao.Tela import Tela

import pygame
from visao.JogoTela import JogoTela

pygame.init()


class ControladorPrincipal:
    def __init__(self):
        self.__controlador_menu = ControladorMenu()
        self.__controlador_tabuleiro = ControladorTabuleiro()
        self.__tela = Tela()
        self.__tela_menu = JogoTela()
        self.__display = pygame.display.set_mode((800, 600))
        self.__background = pygame.image.load('imagens/tabuleiro0.1.png')
        self.__contagem_tela = 0

    def inicia(self):
        while True:
            if self.__contagem_tela == 0:
                self.__controlador_menu.menu_opcoes()
                if self.__controlador_menu.controle_menu == -1:
                    self.__contagem_tela = 1
                    self.__controlador_menu.controle_menu = 0
                elif self.__controlador_menu.controle_menu == -2:
                    sys.exit()

            elif self.__contagem_tela == 1:
                self.__controlador_tabuleiro.tabuleiro_opcoes()
                self.__contagem_tela = 0

    def inicia_menu(self):
        pass
