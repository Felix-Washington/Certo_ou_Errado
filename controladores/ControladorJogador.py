from modelo.Jogador import Jogador
from visao.Tela import Tela
import pygame


class ControladorJogador:

    def __init__(self):
        self.__tela = Tela()
        self.__jogador_um = Jogador()
        self.__jogador_dois = Jogador()
        self.__caixa_nome = 'imagens/caixa_nome.png'
        self.carregar_imagens()

    def definir_nome(self):
        pass
        while not self.__jogador_um.escolheu:
            self.__tela.mostra_imagem(self.__caixa_nome, [200, 200])
            pygame.display.update()

    def definir_primeiro(self):
        pass

    def carregar_imagens(self):
        self.__jogador_um.imagem = 'imagens/jogador_um.png'
        self.__jogador_dois.imagem = 'imagens/jogador_dois.png'

    @property
    def jogadores(self):
        jogadores = [self.__jogador_um, self.__jogador_dois]
        return jogadores

    @property
    def escolha(self):
        return self.__escolha

    @escolha.setter
    def escolha(self, escolha):
        self.__escolha = escolha

    # def jogadores(self):
    #    return self.__jogador_um, self.__jogador_dois
