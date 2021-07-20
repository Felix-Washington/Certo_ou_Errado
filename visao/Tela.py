import pygame


class Tela:
    def __init__(self):
        pygame.display.set_caption("Certo ou Errado")
        icon = pygame.image.load('imagens/interrogaçao_icone.png')
        pygame.display.set_icon(icon)
        self.__screen = pygame.display.set_mode((800, 600))

    def mostra_imagem(self, caminho, x, y):
        img = pygame.image.load(caminho)
        self.__screen.blit(img, (x, y))
