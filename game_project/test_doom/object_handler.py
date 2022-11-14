from sprite_object import *
from npc import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list =[]
        self.npc_sprite_path = 'sprites/npc/'
        self.static_sprtie_path = 'sprites/static_sprites/'
        self.anim_sprite_path = 'sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        
        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(SpriteObject(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game))
        
        #npc map
        add_npc(NPC(game))
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
    def add_npc(self, npc):
        self.npc_list.append(npc)
    
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)