import sys

from controladores.ControladorMenu import ControladorMenu
from controladores.ControladorTabuleiro import ControladorTabuleiro
from controladores.ControladorJogador import ControladorJogador
from controladores.ControladorCartas import ControladorCartas
from visao.Tela import Tela

import pygame

pygame.init()


class ControladorPrincipal:
    def __init__(self):
        self.__controlador_menu = ControladorMenu()
        self.__controlador_jogador = None
        self.__controlador_tabuleiro = None
        self.__controlador_cartas = None
        self.__tela = Tela()
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
                self.novo_jogo()
                self.__controlador_tabuleiro.tabuleiro_opcoes()

                self.__contagem_tela = 0

    def novo_jogo(self):
        self.__controlador_jogador = ControladorJogador()
        self.__controlador_tabuleiro = ControladorTabuleiro(self)
        self.__controlador_cartas = ControladorCartas()

        # print("teste")
        # self.__controlador_cartas.cr

    @property
    def controlador_jogadores(self):
        return self.__controlador_jogador

    @property
    def controlador_cartas(self):
        return self.__controlador_cartas

    @property
    def controlador_principal(self):
        return self
