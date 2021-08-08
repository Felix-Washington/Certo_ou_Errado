import sys
import random

from pygame import font

from controladores.AbstractControlador import AbstractControlador
from visao.Tela import Tela
from modelo.Dado import Dado
from modelo.Posicao import Posicao
from modelo.Texto import Texto

import pygame
from pygame.locals import *


class ControladorTabuleiro(AbstractControlador):
    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__tela = Tela()
        self.__dado = Dado()
        self.__texto = Texto()
        self.__imagem_tabuleiro = 'tabuleiro0.2'
        self.__jogador_da_vez = 0
        self.__controle_de_turno = 0
        self.__controle = 0
        self.__definir_primeiro = False
        self.__posicao_mouse = int
        self.__posicoes = []
        self.mapear_posicoes()
        self.__opcao_escolhida = int
        self.__pode_retirar = False

    def tabuleiro_opcoes(self):

        definir_primeiro = False
        self.__definir_primeiro = True
        while not self.__definir_primeiro:
            self.__tela.mostra_imagem('menus/decidir_primeiro', [0, 0])

            self.__tela.mostra_imagem(self.__dado.imagem, self.__dado.posicao)
            self.__definir_primeiro = self.__controlador_principal.controlador_jogadores. \
                definir_primeiro(self.__dado.rodar_dadog(), self.__dado.rect)
            # self.checar_evento()
            pygame.display.update()

        self.__dado.redefinir()
        self.__controlador_principal.controlador_jogadores.jogadores[0].vez = True
        while self.__controle >= 0:
            self.__posicao_mouse = pygame.mouse.get_pos()
            self.desenha()
            self.turno()
            # self.checar_evento()

    def turno(self):

        if self.__controlador_principal.controlador_jogadores.jogadores[self.__jogador_da_vez].vez:
            self.checar_evento()
            # self.andar_no_tabuleiro(self.__controlador_principal.controlador_jogadores.jogadores[0], self.__dado.rodar_dado())

        '''
        self.__controlador_principal.controlador_jogadores.jogadores[self.__jogador_da_vez].vez = \
            not self.__controlador_principal.controlador_jogadores.jogadores[self.__jogador_da_vez].vez

        if self.__jogador_da_vez == 0:
            self.__jogador_da_vez = 1

        elif self.__jogador_da_vez == 1:
            self.__jogador_da_vez = 0
        '''

    def desenha(self):
        self.__tela.mostra_imagem(self.__imagem_tabuleiro, [0, 0])
        self.__tela.mostra_imagem(self.__dado.imagem, self.__dado.posicao)

        for i in range(10):
            self.__tela.mostra_imagem(self.__posicoes[i].imagem, self.__posicoes[i].posicao)
        self.__tela.mostra_imagem(self.__controlador_principal.controlador_jogadores.jogadores[0].imagem,
                                  self.__controlador_principal.controlador_jogadores.jogadores[0].posicao)

        for carta in self.__controlador_principal.controlador_cartas.baralho:
            self.__tela.mostra_imagem(carta.imagem, carta.posicao)

        ultima_carta = self.__controlador_principal.controlador_cartas.ultima_carta_baralho
        self.__tela.mostra_imagem(ultima_carta.imagem, ultima_carta.posicao)

        carta_atual = self.__controlador_principal.controlador_cartas.carta_atual
        if carta_atual is not None:
            self.__tela.mostra_imagem(carta_atual.imagem, carta_atual.posicao)
            self.__controlador_principal.controlador_cartas.mostrar_opcoes()

        self.__controlador_principal.controlador_jogadores.desenhar()

        if self.__controle_de_turno == 2:
            self.__texto.editar_texto()
            self.__tela.texto(self.__texto.texto_surface, self.__texto.x_y)

            pygame.draw.rect(self.__tela.screen, self.__texto.color, self.__texto.caixa_texto, 2)
            # pygame.display.flip()

        pygame.display.update()

    def checar_evento(self):
        for evento in pygame.event.get():
            self.mouse(evento)
            self.teclado(evento)

    def mouse(self, evento):
        if evento.type == MOUSEBUTTONDOWN:

            if self.__controle_de_turno == 0:
                if self.__dado.rect.collidepoint(self.__posicao_mouse):
                    self.andar_no_tabuleiro(self.__jogador_da_vez, self.__dado.rodar_dado())
                    posicao_tabuleiro = self.__controlador_principal.controlador_jogadores.jogadores[
                        self.__jogador_da_vez].posicao_tabuleiro
                    self.verificar_icone(self.__posicoes[posicao_tabuleiro].funcao)

            if self.__pode_retirar:
                self.retirar_carta()
                self.__pode_retirar = False

            if self.__controle_de_turno == 2:
                if self.__texto.caixa_texto.collidepoint(self.__posicao_mouse):
                    self.__texto.caixa_ativa = not self.__texto.caixa_ativa
                else:
                    self.__texto.caixa_ativa = False

    def teclado(self, evento):
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                self.__controle = -1

            if self.__texto.caixa_ativa:
                if evento.key == pygame.K_BACKSPACE:
                    self.__texto.texto = self.__texto.texto[:-1]

                elif evento.key == pygame.K_RETURN:
                    self.verificar_inteiro()
                    self.__opcao_escolhida = int(self.__texto.texto)
                    self.__controle_de_turno = 1
                    self.__texto.caixa_ativa = False
                    self.__texto.texto = ''
                else:
                    self.__texto.texto += evento.unicode

    def verificar_inteiro(self):
        ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # try:
        #    inteiro =

    def andar_no_tabuleiro(self, jogador, valor_dado):
        valor = 1
        while valor <= valor_dado:
            posicao_tabuleiro = self.__controlador_principal.controlador_jogadores.jogadores[jogador].posicao_tabuleiro
            if posicao_tabuleiro + valor_dado > len(self.__posicoes) - 1:
                posicao_tabuleiro = len(self.__posicoes) - 1
                self.__controlador_principal.controlador_jogadores.jogadores[jogador].venceu = True
            else:
                self.__controlador_principal.controlador_jogadores.jogadores[jogador].posicao_tabuleiro += 1
                posicao_tabuleiro += 1
            self.__controlador_principal.controlador_jogadores.jogadores[jogador].posicao = \
                self.__posicoes[posicao_tabuleiro].posicao
            self.desenha()

            valor += 1

        self.__controle_de_turno = 1

    def verificar_icone(self, funcao):
        funcao = "simples"
        if funcao == "simples":
            self.__controle_de_turno = 2

            print("simples")
        elif funcao == "multipla":
            print("multipla")
        elif funcao == "desafio":
            print("desafio")
        elif funcao == "sdesafio":
            print("sdesafio")
        elif funcao == "pare":
            print("pare")

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
        if self.__controlador_principal.controlador_cartas.numero_cartas_total > 0:
            if self.__controlador_principal.controlador_cartas \
                    .ultima_carta_baralho.rect.collidepoint(self.__posicao_mouse):
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
