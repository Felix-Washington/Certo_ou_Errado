import pygame


class Texto:
    def __init__(self):
        self.__texto = ''
        self.__caixa_ativa = False
        self.__caixa_texto = pygame.Rect(300, 350, 50, 50)
        self.__texto_surface = None
        self.__x_y = [300, 350]

        self.__color_inactive = pygame.Color('lightskyblue3')
        self.__color_active = pygame.Color('dodgerblue2')
        self.__color = self.__color_inactive
        self.__font = pygame.font.Font(None, 32)

    def editar_texto(self):
        self.__color = self.__color_active if self.__caixa_ativa else self.__color_inactive
        self.__texto_surface = self.__font.render(self.__texto, True, self.__color)
        width = max(200, self.__texto_surface.get_width() + 10)
        self.__caixa_texto.w = width

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @property
    def color(self):
        return self.__color

    @property
    def x_y(self):
        return self.__x_y

    @property
    def caixa_texto(self):
        return self.__caixa_texto

    @property
    def caixa_ativa(self):
        return self.__caixa_ativa

    @property
    def texto_surface(self):
        return self.__texto_surface

    @caixa_ativa.setter
    def caixa_ativa(self, ativa):
        self.__caixa_ativa = ativa
