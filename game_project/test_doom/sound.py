import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'sound/'
        self.vandal = pg.mixer.Sound(self.path + 'vandal/oneshot.wav')