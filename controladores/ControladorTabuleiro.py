import sys
import random

from controladores.AbstractControlador import AbstractControlador
from visao.Tela import Tela
from modelo.Dado import Dado
from modelo.Posicao import Posicao

import pygame
from pygame.locals import *


class ControladorTabuleiro(AbstractControlador):
    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__tela = Tela()
        self.__dado = Dado()
        self.__imagem_tabuleiro = 'tabuleiro0.2'
        self.__controle = 0
        self.__posicao_mouse = int
        self.__posicoes = []
        self.mapear_posicoes()

    def tabuleiro_opcoes(self):

        while self.__controle >= 0:
            self.__posicao_mouse = pygame.mouse.get_pos()
            self.checar_evento()
            self.desenha()

        # self.__controle = 0

    def turno(self):
        pass

    def desenha(self):
        self.__tela.mostra_imagem(self.__imagem_tabuleiro, [0, 0])
        self.__tela.mostra_imagem(self.__dado.imagem, self.__dado.posicao)
        for i in range(10):
            self.__tela.mostra_imagem(self.__posicoes[i].imagem,
                                      [self.__posicoes[i].posicao[0], self.__posicoes[i].posicao[1]])

        for carta in self.__controlador_principal.controlador_cartas.baralho:
            self.__tela.mostra_imagem(carta.imagem, carta.posicao)

        carta_atual = self.__controlador_principal.controlador_cartas.carta_atual
        if carta_atual is not None:
            self.__tela.mostra_imagem(carta_atual.imagem, carta_atual.posicao)

        pygame.display.update()

    def checar_evento(self):
        for evento in pygame.event.get():
            self.mouse(evento)
            self.teclado(evento)

    def mouse(self, evento):
        if evento.type == MOUSEBUTTONDOWN:
            if self.__controlador_principal.controlador_cartas.numero_cartas_total > 0:
                if self.__controlador_principal.controlador_cartas.ultima_carta_baralho.rect.collidepoint(
                        self.__posicao_mouse):
                    self.retirar_carta()

            if self.__dado.rect.collidepoint(self.__posicao_mouse):
                self.__dado.rodar_dado()

            for posicao in self.__posicoes:
                if posicao.rect.collidepoint(self.__posicao_mouse):
                    pass
                    print(self.__posicoes.index(posicao))

    def teclado(self, evento):
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                self.__controle = -1

    def mapear_posicoes(self):
        x = 100
        y = 420
        aumento_x = 0
        aumento_y = -80
        funcoes = ["simples", "multipla", "desafio", "sdesafio", "pare"]
        ultimo = 10

        for i in range(ultimo):
            funcao = ''
            if i == 0:
                funcao = "inicio"
            elif i == ultimo:
                funcao = "fim"
            else:
                repetido = True

                while repetido:

                    funcao = random.choice(funcoes)
                    if funcao != self.__posicoes[i - 1].funcao:
                        repetido = False

            self.__posicoes.append(Posicao(x, y, funcao))

            if i == random.choice([3, 4]) or i > 4:
                aumento_x = 80
                aumento_y = 0

            y += aumento_y
            x += aumento_x

    def retirar_carta(self):
        self.__controlador_principal.controlador_cartas.virar_carta()

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
