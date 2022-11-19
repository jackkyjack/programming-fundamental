from setting import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
       
        
    def get_damage(self, damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        
    
    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.shotting:
                self.shot = True
                self.game.sound.vandal.play()
                self.game.weapon.shotting = True
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)
        
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
    
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
    
    def draw(self):
        # pg.draw.line(self.game.screen, 'yellow', (self.x * 40, self.y * 40),
        #            (self.x * 40 + WIDTH * math.cos(self.angle),
        #              self.y * 40 + WIDTH * math.sin(self.angle)), 2)
        # pg.draw.circle(self.game.screen, 'green', (self.x * 40, self.y * 40), 15)
        if self.health == 20:
           self.game.screen.blit(pg.image.load('assets/hp/20.png'), (0, 600))
        elif self.health == 19:
           self.game.screen.blit(pg.image.load('assets/hp/19.png'), (0, 600))
        elif self.health == 18:
           self.game.screen.blit(pg.image.load('assets/hp/18.png'), (0, 600))
        elif self.health == 17:
           self.game.screen.blit(pg.image.load('assets/hp/17.png'), (0, 600))
        elif self.health == 16:
           self.game.screen.blit(pg.image.load('assets/hp/16.png'), (0, 600))
        elif self.health == 15:
           self.game.screen.blit(pg.image.load('assets/hp/15.png'), (0, 600))
        elif self.health == 14:
           self.game.screen.blit(pg.image.load('assets/hp/14.png'), (0, 600))
        elif self.health == 13:
           self.game.screen.blit(pg.image.load('assets/hp/13.png'), (0, 600))
        elif self.health == 12:
           self.game.screen.blit(pg.image.load('assets/hp/12.png'), (0, 600))
        elif self.health == 11:
           self.game.screen.blit(pg.image.load('assets/hp/11.png'), (0, 600))
        elif self.health == 10:
           self.game.screen.blit(pg.image.load('assets/hp/10.png'), (0, 600))
        elif self.health == 9:
           self.game.screen.blit(pg.image.load('assets/hp/9.png'), (0, 600))
        elif self.health == 8:
           self.game.screen.blit(pg.image.load('assets/hp/8.png'), (0, 600))
        elif self.health == 7:
           self.game.screen.blit(pg.image.load('assets/hp/7.png'), (0, 600))
        elif self.health == 6:
           self.game.screen.blit(pg.image.load('assets/hp/6.png'), (0, 600))
        elif self.health == 5:
           self.game.screen.blit(pg.image.load('assets/hp/5.png'), (0, 600))
        elif self.health == 4:
           self.game.screen.blit(pg.image.load('assets/hp/4.png'), (0, 600))
        elif self.health == 3:
           self.game.screen.blit(pg.image.load('assets/hp/3.png'), (0, 600))
        elif self.health == 2:
           self.game.screen.blit(pg.image.load('assets/hp/2.png'), (0, 600))
        elif self.health == 1:
           self.game.screen.blit(pg.image.load('assets/hp/1.png'), (0, 600))
        
        pg.display.update()
    
    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
       
        pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time
    
    def update(self):
        self.movement()
        self.mouse_control()
        self.draw()
        
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)