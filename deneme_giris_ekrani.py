# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:26:59 2020

@author: a
"""

import pygame,sys,random


#---İnitilaze Pygame------------ #
pygame.init()

#-----Setting------------------- #
window_width = 1000
window_height = 800

#-------- İmages and Sounds ------------------- #

pygame.display.set_caption("boing boing game")

Arka_plan = pygame.image.load("background.png").convert_alpha()
Karakter = pygame.image.load("bunny.png").convert_alpha()
Ball = pygame.image.load("ball.png").convert_alpha()
Mermi =  pygame.image.load("bullett.png").convert_alpha()

#pygame.mixer.music.load("efect.mp3")

#------Game Window-----------------------------  #

game_window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("boing boing game")

#------- Fps ------------------------------------ #

clock = pygame.time.Clock()
fps = 60

#------- Skor Tablosu --------------------------  #
font =  pygame.font.SysFont("Helvatica",40)

score = 0


# ---------  Character Sprites  Class ----------- #

class player_sprites(pygame.sprite.Sprite):
    def __init__(self,x = 0, y= 0):
        super().__init__()
        self.image = Karakter
        self.rect = self.image.get_rect()
        self.radius = int(65 / 2)
        self.rect.topleft = (x,y)
        
#------ Character Update ------------------------ #        
        
    def update(self,*args):
        right,left = args
        if self.rect.x + Karakter.get_size()[0] < 1000: 
            if right:
                self.rect.x += 5
        if self.rect.x  > 0: 
            if left:
                self.rect.x -= 5
                
    def shoot(self):
        mermi = Bullet(self.rect.x)
        all_sprites.add(mermi)
        mermiler.add(mermi)
        
        


# ----------- Ball Sprites Class ---------------- #

class ball(pygame.sprite.Sprite):
     def __init__(self):
         super().__init__()
         self.image =  Ball
         self.rect = self.image.get_rect()
         self.radius = int((self.rect.width *0.80 )/ 2)
    
         self.rect.x = random.randrange(window_width - self.rect.width)
         self.rect.y = random.randrange(-30,-40,-10)
         self.speedy = random.randrange(5,10) 
         self.speedx = random.randrange(-2,2)
         
# ---------- Ball Update ------------------------ #
         
     def update(self, *args):
         self.rect.y += self.speedy
         self.rect.x -= self.speedx
         if self.rect.top > window_height:
             self.rect.y = random.randrange(-30,-40,-10)
             self.rect.x = random.randrange(window_width - self.rect.width)
             self.speedy = random.randrange(5,10) 
             self.speedx = random.randrange(-2,2)
             global score
             score += 1
             
# ------- Class Bullet -------------------------- #
             
class Bullet(pygame.sprite.Sprite):
    def __init__(self,parcax):
        super().__init__()
        self.image = Mermi
        self.rect = self.image.get_rect()
        self.rect.y = window_height - 100
        self.rect.x = parcax + 30
    
    def update(self, *args):
        self.rect.y -= 8
        
        if self.rect.top < 0:
            self.kill()
        
        
        
# -------- Sprite Groupları Ekleme ------- #        
    
             
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
mermiler = pygame.sprite.Group()

for i in range(7):
    dusen_cisimler = ball()
    all_sprites.add(dusen_cisimler)
    balls.add(dusen_cisimler)

           
bunny = player_sprites(500,689)
all_sprites.add(bunny)                
                 
#-------  Game Loop --------------------  #

while True:
    top_sayisi = len(balls)
    
    keys = pygame.key.get_pressed()    
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        #---- ateş etme ------#
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bunny.shoot()
            
            
            
# ----------- Key ----------------------- #
    right,left = keys[pygame.K_RIGHT],keys[pygame.K_LEFT]
    all_sprites.update(right,left)
    
# -------- writing score ---------------- #
                
    fontScore = font.render("Balls: {}".format(top_sayisi),1,(255,255,255))
    
    
# ----------- Draw ---------------------- #
    game_window.blit(Arka_plan,(0,0))
    
    game_window.blit(fontScore,(window_width-fontScore.get_size()[0],0))
    
    all_sprites.draw(game_window)
    
    durum = pygame.sprite.spritecollide(bunny,balls,False,collided = pygame.sprite.collide_circle)
    
    pygame.sprite.groupcollide(mermiler,balls,True,True)
    
    
    if durum:
        #pygame.mixer.music.play()
        game_window.blit(pygame.font.SysFont("Helvatica",50).render("Game Over!",1,(0,0,0)),(400,350))
        pygame.display.update()
        pygame.time.wait(1000)
        sys.exit()
    
    if top_sayisi == 0:
        game_window.blit(pygame.font.SysFont("Helvatica",50).render("You Win!",1,(255,0,0)),(400,350))
        pygame.display.update()
        pygame.time.wait(1000)
        sys.exit()
    
    
    
    pygame.display.update()
     
     