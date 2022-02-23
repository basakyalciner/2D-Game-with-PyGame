# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:01:51 2020

@author: a
"""

import pygame,sys,random


#---İnitilaze Pygame---#
pygame.init()

#-----Setting---------#
window_width = 1000
window_height = 800

#-------- İmages -------#

pygame.display.set_caption("boing boing game")

Arka_plan = pygame.image.load("background.png").convert_alpha()
Karakter = pygame.image.load("bunny.png").convert_alpha()
Ball = pygame.image.load("ball.png").convert_alpha()
Mermi =  pygame.image.load("bullet.png").convert_alpha()

#------Game Window-------#

game_window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("boing boing game")

#------- Fps -----------#

clock = pygame.time.Clock()
fps = 60


# ---------  Character Sprites  Class ---------------- #

class player_sprites(pygame.sprite.Sprite):
    def __init__(self,x = 0, y= 0):
        super().__init__()
        self.image = Karakter
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
#------ Character Update --------#        
        
    def update(self,*args):
        right,left = args
        if self.rect.x + Karakter.get_size()[0] < 1000: 
            if right:
                self.rect.x += 5
        if self.rect.x  > 0: 
            if left:
                self.rect.x -= 5


# ----------- Ball Sprites Class ----------- #
class ball(pygame.sprite.Sprite):
     def __init__(self):
         super().__init__()
         self.image =  Ball
         self.rect = self.image.get_rect()
         self.rect.x = random.randrange(window_width - self.rect.width)
         self.rect.y = random.randrange(-50,-40)
         self.speedy = random.randrange(1,5)   
         
         # ---------- Ball Update ------------ #
     def update(self, *args):
         self.rect.y += self.speedy
         if self.rect.top > window_height:
            self.rect.x = random.randrange(window_width - self.rect.width)
            self.rect.y = random.randrange(-50,-40)
            self.speedy = random.randrange(1,5)   
         
             
all_sprites = pygame.sprite.Group()
for i in range(10):
    düsen_cisimler = ball()
    all_sprites.add(düsen_cisimler) 

           
bunny = player_sprites(500,689)
all_sprites.add(bunny)                
                 
#-------  Game Loop -------#

while True:
    keys = pygame.key.get_pressed()    
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        
    # ------- Key ----------#
    
    right,left = keys[pygame.K_RIGHT],keys[pygame.K_LEFT]
    all_sprites.update(right,left)
                
            
        
    
# ----------- Draw ---------------------- #
    game_window.blit(Arka_plan,(0,0))
    all_sprites.draw(game_window)
    pygame.display.update()
     
     