import pygame


class Tela:
    def __init__(self):
        pygame.display.set_caption("Certo ou Errado")
        icon = pygame.image.load('imagens/interrogaçao_icone.png')
        pygame.display.set_icon(icon)
        self.__screen = pygame.display.set_mode((800, 600))

    def mostra_imagem(self, caminho, tuplas):
        pasta = 'imagens/'
        img = pygame.image.load(pasta + caminho + '.png')
        self.__screen.blit(img, tuplas)

    def texto(self, img, pos):
        self.__screen.blit(img, pos)

    def redimensionar_imagem(self, objeto):
        pasta = 'imagens/'
        img = pygame.image.load(pasta + objeto.imagem + '.png')
        print(objeto.tamanho)
        pygame.transform.scale(img, [300, 300])
        self.__screen.blit(img, objeto.posicao)

    @property
    def screen(self):
        return self.__screen
