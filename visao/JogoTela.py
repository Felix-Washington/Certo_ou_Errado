import pygame


class JogoTela:
    def __init__(self):
        self.__screenX = 800
        self.__screenY = 600
        # self.menu_image = pygame.image.load()
        self.__screen = pygame.display.set_mode((self.__screenX, self.__screenY))
        # self.__background = pygame.image.load('background_space.jpg')

    def screen_att(self, image, x, y):
        self.__screen.blit(image, (x, y))
