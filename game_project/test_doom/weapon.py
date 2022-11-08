from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='sprites/weapon/1.png', scale=0.75, animation_time=20):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = ((WIDTH * 3 // 4) - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.shotting = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50
        
    def animated_shot(self):
        if self.shotting:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.shotting = False
                    self.frame_counter = 0
                    
        
    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        
    def update(self):
        self.check_animation_time()
        self.animated_shot()