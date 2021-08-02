from modelo.Carta import Carta


class ControladorCartas:

    def __init__(self):
        self.__baralho = []
        self.__numero_cartas_baralho = 3
        self.__numero_cartas_total = 3
        self.__carta_atual = None
        self.criar_cartas()
        self.__ultima_carta_baralho = self.__baralho[-1]
        self.__perguntas = {}

    def criar_cartas(self):
        for i in range(self.__numero_cartas_total):
            self.__baralho.append(Carta(""))

        self.__ultima_carta_baralho = self.__baralho[-1]

    def virar_carta(self):
        self.__carta_atual = self.__baralho[-1]
        self.__carta_atual.imagem = 'carta_cima'
        print(self.__carta_atual.tamanho)
        self.__carta_atual.tamanho = [240, 320]
        self.__carta_atual.posicao = [400 - (self.__carta_atual.tamanho[0] / 2), 600 - self.__carta_atual.tamanho[1]]

        self.__carta_atual.rect = [self.__carta_atual.posicao]
        del self.__baralho[-1]

        self.__numero_cartas_total -= 1

        if self.__numero_cartas_total == 0:
            self.__ultima_carta_baralho = self.__baralho
        else:
            self.__ultima_carta_baralho = self.__baralho[-1]

    def organizar_perguntas(self):

        pass

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
