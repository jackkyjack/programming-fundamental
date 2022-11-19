import pygame as pg
import sys
from setting import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *
from button import *

pg.init()

SCREEN = pg.display.set_mode(RES)
pg.display.set_caption("VALODANT")

BG = pg.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/spaceranger.ttf", size)

def play():
    class Game():
        def __init__(self):
            pg.init()
            pg.mouse.set_visible(False)
            self.screen = pg.display.set_mode(RES)
            self.clock = pg.time.Clock()
            self.delta_time = 1
            self.global_trigger = False
            self.global_event = pg.USEREVENT + 0
            pg.time.set_timer(self.global_event, 40)
            self.new_game()
            
        def new_game(self):
            self.map = Map(self)
            self.player = Player(self)
            self.object_renderer = ObjectRenderer(self)
            self.raycasting = RayCasting(self)
            # self.static_sprite = SpriteObject(self)
            # self.animated_sprtie = AnimatedSprite(self)
            self.object_handler = ObjectHandler(self)
            self.weapon = Weapon(self)
            self.sound = Sound(self)
            self.pathfinding = PathFinding(self)
            
        def update(self):
            self.player.update()
            self.raycasting.update()
            # self.static_sprite.update()
            # self.animated_sprtie.update()
            self.object_handler.update()
            self.weapon.update()
            pg.display.flip()
            self.delta_time = self.clock.tick(FPS)
            pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

        def draw(self):
            # self.screen.fill('black')
            self.object_renderer.draw()
            self.weapon.draw()
            # self.map.draw()
            # self.player.draw()
            pg.draw.rect(game.screen, 'white', (639,355,2,10))
            pg.draw.rect(game.screen, 'white', (635,359,10,2))
            
        def check_events(self):
            self.global_trigger = False
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.mouse.set_visible(True)
                    main_menu()
                elif event.type == self.global_event:
                    self.global_trigger = True
                self.player.single_fire_event(event)
        
        def run(self):
            while True:
                self.check_events()
                self.update()
                self.draw()


    if __name__ == '__main__':
        game = Game()
        game.run()

    
    
def ranking():
    while True:
        RANKING_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("white")

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        RANKING_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        RANKING_BACK.changeColor(RANKING_MOUSE_POS)
        RANKING_BACK.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.mouse.set_visible(True)
                    main_menu()
            if event.type == pg.MOUSEBUTTONDOWN :
                if RANKING_BACK.checkForInput(RANKING_MOUSE_POS):
                    main_menu()

        pg.display.update()

def game_over(self):
    pass

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        NAME_TEXT = get_font(20).render("65011174 ANUCHA KAEOMAMUEANG", True, "white")
        SCREEN.blit(NAME_TEXT, (0, 0))
        
        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Valodant", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        RANKING_BUTTON = Button(image=pg.image.load("assets/Ranking_Rect.png"), pos=(640, 400), 
                            text_input="RANKING", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Quit_Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, RANKING_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ranking()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

main_menu()