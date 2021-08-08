from modelo.Carta import Carta
from visao.Tela import Tela
import pygame
import random


class ControladorCartas:

    def __init__(self):
        self.__tela = Tela()
        self.__baralho = []
        self.__texto_pos = []
        self.__numero_cartas_total = 3
        self.__perguntas = self.pool_de_perguntas()
        self.__carta_atual = None
        self.criar_cartas()
        pygame.font.init()
        self.__myfont = pygame.font.SysFont(None, 30)

    def criar_cartas(self):
        for i in range(self.__numero_cartas_total):
            self.__baralho.append(Carta({}))

        self.__ultima_carta_baralho = self.__baralho[-1]

    def virar_carta(self):
        if self.__numero_cartas_total > 0:
            self.__carta_atual = self.__baralho[-1]
            self.definir_perguntas()
            self.__carta_atual.imagem = 'carta_cima'

            self.__carta_atual.tamanho = [240, 320]
            self.__carta_atual.posicao = [int(400 - (self.__carta_atual.tamanho[0] / 2)),
                                          600 - self.__carta_atual.tamanho[1]]

            self.__carta_atual.rect = [self.__carta_atual.posicao]
            del self.__baralho[-1]

            self.__numero_cartas_total -= 1

            if self.__numero_cartas_total == 0:
                self.__ultima_carta_baralho = self.__baralho
            else:
                self.__ultima_carta_baralho = self.__baralho[-1]

    def definir_perguntas(self):
        i = 0
        text_y = 280
        while i <= 3:
            chave = random.randint(0, 12)
            if self.__perguntas[chave] != "":
                self.__carta_atual.perguntas[i] = self.__perguntas[chave]
                self.__perguntas[chave] = ""
                i += 1

                # posição texto
                self.__texto_pos.append(text_y)
                text_y += 20

    def mostrar_opcoes(self):
        for i in range(4):
            img = self.__myfont.render(self.__carta_atual.perguntas[i], True, (255, 20, 30))
            self.__tela.texto(img, [285, self.__texto_pos[i]])

    def pool_de_perguntas(self):
        perguntas = {
            0: "O Brasil se tornou idependente no ano de 1815.",
            1: "Um dado é composto de 4 quadrados.",
            2: "A Terra é uma geóide.",
            3: "De acordo com a física, a cor preta significa a ausencia de luz.",
            4: "O estado do Pará pertence ao Nordeste.",
            5: "O siri é o único caranguejo capaz de nadar.",
            6: "A água contém hidrogênio.",
            7: "A Amazônia fica apenas no Brasil.",
            8: "Um quilo equivale a um litro de água em massa.",
            9: "O arco íris possui infinitas cores.",
            10: "Entre os número 1 e 10, existem 9 números.",
            11: "Teste",
            12: "Teste2"
        }

        return perguntas

    @property
    def carta_atual(self):
        return self.__carta_atual

    @property
    def baralho(self):
        return self.__baralho

    @property
    def numero_cartas_total(self):
        return self.__numero_cartas_total

    @numero_cartas_total.setter
    def numero_cartas_total(self, numero):
        self.__numero_cartas_total = numero

    @property
    def ultima_carta_baralho(self):
        return self.__ultima_carta_baralho
