from modelo.Jogador import Jogador
from visao.Tela import Tela
import pygame
from pygame.locals import *


class ControladorJogador:

    def __init__(self):
        self.__tela = Tela()
        self.__jogadores = [Jogador(), Jogador()]
        self.__caixa_nome = 'caixa_nome'
        self.carregar_imagens()
        self.__posicao_mouse = pygame.mouse.get_pos()

    def definir_nome(self):
        pass
        while not self.__jogador_um.escolheu:
            self.__tela.mostra_imagem(self.__caixa_nome, [200, 200])
            pygame.display.update()

    def definir_primeiro(self, valor_dado, dado_rect):
        self.mouse(dado_rect)
        if self.__jogadores[0].rodou_dado == 0:
            self.__jogadores[0].rodou_dado = valor_dado

        elif self.__jogadores[1].rodou_dado == 0:
            self.__jogadores[1].rodou_dado = valor_dado
        elif self.__jogadores[0].rodou_dado > 0 and self.__jogadores[1].rodou_dado > 0:
            if self.__jogadores[0].rodou_dado == self.__jogadores[1].rodou_dado:
                return False
            else:
                return True

        else:
            return False

    def carregar_imagens(self):
        self.__jogadores[0].imagem = 'jogador_um'
        self.__jogadores[1].imagem = 'jogador_dois'

    def mudar_jogador(self, jogador):
        if self.__jogadores[0].vez:
            self.__jogadores[0].vez = False
            self.__jogadores[1].vez = True

        elif self.__jogadores[1].vez:
            self.__jogadores[0].vez = True
            self.__jogadores[1].vez = False

    def desenhar(self):
        self.__tela.mostra_imagem(self.__jogadores[0].imagem, self.__jogadores[0].posicao)
        self.__tela.mostra_imagem(self.__jogadores[1].imagem, self.__jogadores[1].posicao)

    @property
    def jogadores(self):
        return self.__jogadores
