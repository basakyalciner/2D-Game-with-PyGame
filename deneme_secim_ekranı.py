# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:53:51 2020

@author: a
"""

import pygame,sys 

pygame.init()

#-----Setting------------------- #
width = 1000
height = 800

#-------- İmages and Sounds ------------------- #
Secim_ekrani =  pygame.image.load("seviyeekrani.png") 


#------Game Window-----------------------------  #

start_window = pygame.display.set_mode((width,height))

pygame.display.set_caption("boing boing game")

#------- Fps ------------------------------------ #

clock = pygame.time.Clock()
fps = 60

#-------------- Start Class 
class Start():
    def __init__(self):
        self.imagee  =  Secim_ekrani 
        self.easyx1 = 339
        self.easyx2 = 658
        self.easyy1 = 90
        self.easyy2 = 180
        self.mediumx1 = 339 
        self.mediumx2 = 658 
        self.mediumy1 = 209
        self.mediumy2 = 338
        self.hardx1 = 338 
        self.hardx2 = 658 
        self.hardy1 = 411 
        self.hardy2 = 492
        
    def update(self):
        start_window.blit(self.imagee,(0,0))
        pygame.display.update()
        
    def start_update(self):
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        # ----------------- mouse action ------------ #
        left,middle,right  = pygame.mouse.get_pressed()
      
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
            
              return "exit"
        
        if self.easyx1 < mouse_x < self.easyx2 and self.easyy1 < mouse_y < self.easyy2:
            if left == 1:
                import LevelEasy
                LevelEasy()
        if self.mediumx1 < mouse_x < self.mediumx2 and self.mediumy1 < mouse_y < self.mediumy2:
            if left == 1:
                import LevelMedium
                LevelMedium()
        if self.hardx1 < mouse_x < self.hardx2 and self.hardy1 < mouse_y < self.hardy2:
            if left == 1:
                import LevelHard
                LevelHard()
            
        self.update()
# --------- loop ----------- #       
start = Start()
while True:
    durum = start.start_update()
    if durum == "exit":
        break
    
    
pygame.quit()
    
        