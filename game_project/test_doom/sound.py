import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'sound/'
        self.vandal = pg.mixer.Sound(self.path + 'vandal/oneshot.wav')
        self.duck_walk = pg.mixer.Sound(self.path + 'duck/duck_walk.wav')
        self.duck_hit = pg.mixer.Sound(self.path + 'duck/duck_hit.wav')
        self.duck_attack = pg.mixer.Sound(self.path + 'duck/duck_attack.wav')
        self.duck_death = pg.mixer.Sound(self.path + 'duck/duck_death.wav')