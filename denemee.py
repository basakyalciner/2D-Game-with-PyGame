# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:40:29 2020

@author: a
"""

import pygame,sys,random


#---İnitilaze Pygame------------ #
pygame.init()

#-----Setting------------------- #
window_width = 1000
window_height = 800

#-------- İmages ------------------------------- #

pygame.display.set_caption("boing boing game")
Arka_plan = pygame.image.load("background.png").convert_alpha()
Karakter = pygame.image.load("bunny2.png").convert_alpha()
Ball = pygame.image.load("ball.png").convert_alpha()
Mermi =  pygame.image.load("bullett.png").convert_alpha()
Pasta =  pygame.image.load("pasta.png").convert_alpha()
Try_again_button = pygame.image.load("button.png").convert_alpha()


#-------- Sounds ------------------------------- #

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
         self.speedy = random.randrange(3,7) 
         self.speedx = random.randrange(-1,1)
         
# ---------- Ball Update ------------------------ #
         
     def update(self, *args):
         self.rect.y += self.speedy
         self.rect.x -= self.speedx
         if self.rect.top > window_height:
             self.rect.y = random.randrange(-30,-40,-10)
             self.rect.x = random.randrange(window_width - self.rect.width)
             self.speedy = random.randrange(3,7) 
             self.speedx = random.randrange(-1,1)
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

# ----- Tehlikeli Pasta -------------------------- #
            
class pasta(pygame.sprite.Sprite):
     def __init__(self):
         super().__init__()
         self.image =  Pasta
         self.rect = self.image.get_rect()
         self.radius = int((self.rect.width *0.80 )/ 2)
    
         self.rect.x = random.randrange(window_width - self.rect.width)
         self.rect.y = random.randrange(-30,-40,-10)
         self.speedy = random.randrange(3,7) 
         self.speedx = random.randrange(-1,1)
         
# ---------- Pasta Update ------------------------ #
         
     def update(self, *args):
         self.rect.y += self.speedy
         self.rect.x -= self.speedx
         if self.rect.top > window_height:
             self.rect.y = random.randrange(-30,-40,-10)
             self.rect.x = random.randrange(window_width - self.rect.width)
             self.speedy = random.randrange(3,5) 
             self.speedx = random.randrange(-2,2)
             global score
             score += 1
             

               
                
# -------- Sprite Groupları Ekleme ------- #        
    
             
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
mermiler = pygame.sprite.Group()
pastalar = pygame.sprite.Group()
# ----- Sürekli düşen toplar  ----------  #
for i in range(10):
    dusen_cisimler = ball()
    all_sprites.add(dusen_cisimler)
    balls.add(dusen_cisimler)
    
# ----- Sürekli düşen pastalar  ----------  #    
for i in range(2):
    dusen_cisimler_2 = pasta()
    all_sprites.add(dusen_cisimler_2)
    pastalar.add(dusen_cisimler_2)

           
bunny = player_sprites(500,689)
all_sprites.add(bunny)  

# -------- home button --------------------- #

class home():
    def __init__(self):
        self.imagee  = home  
        self.x1 = 339
        self.x2 = 658
        self.y1 = 90
        self.y2 = 180
        
    def update(self):
        
        pygame.display.update()
        
    def start_update(self):
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        # ----------------- mouse action ------------ #
        left,middle,right  = pygame.mouse.get_pressed()         
                 
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
    
# -------- Writing score ---------------- #
                
    fontScore = font.render("Balls: {}".format(top_sayisi),1,(255,255,255)) 
    
# ----------- Draw ---------------------- #
    game_window.blit(Arka_plan,(0,0))
    
    game_window.blit(fontScore,(window_width-fontScore.get_size()[0],0))
    
    all_sprites.draw(game_window)
    
    # --- Top ile tavşanın çarpışması ----------------------#
    durum = pygame.sprite.spritecollide(bunny,balls,False,collided = pygame.sprite.collide_circle)
    
    # ---- Mermilerin topa isabet etmesi ------------------ #
    pygame.sprite.groupcollide(mermiler,balls,True,True)
    
    #----------- Tehlikeli Pasta Collide  ----------------- #
    durum_1 =  pygame.sprite.spritecollide(bunny,pastalar,False,collided = pygame.sprite.collide_circle)
    durum_2 = pygame.sprite.groupcollide(mermiler,pastalar,True,True)
    
    # ------- Collision results --------------------------- #
    
    if durum_1 or durum_2:
        
        game_window.blit(pygame.font.SysFont("Helvatica",50).render("Game Over!",1,(0,0,0)),(400,350))
        game_window.blit(Try_again_button,(470,400))
        pygame.display.update()
        pygame.time.wait(1000)
        sys.exit()

    
    if durum:
        #pygame.mixer.music.play()
        
        game_window.blit(pygame.font.SysFont("Helvatica",50).render("Game Over!",1,(0,0,0)),(400,350))
        game_window.blit(Try_again_button,(470,400))
        pygame.display.update()
        pygame.time.wait(1000)        
        sys.exit()

    
        
    
    if top_sayisi == 0:
        
        game_window.blit(pygame.font.SysFont("Helvatica",50).render("You Win!",1,(0,0,0)),(400,350))
        game_window.blit(Try_again_button,(470,400))
        pygame.display.update()
        pygame.time.wait(1000)
        sys.exit()

    
    
    pygame.display.update()
     
