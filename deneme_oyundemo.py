# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:33:59 2020

@author: a
"""

import pygame,sys
pygame.init()  #init komutunu amacı pygame kütüphanesini kullanılabilir hale getirme.
#Oyun giriş penceresi oluşturma:
boyut=(1000,800) #oyunda kullandığın pencere genişliği
arka_plan = pygame.image.load("arkaplan.png").convert_alpha()
karakter = pygame.image.load("karakter.png").convert_alpha()
pencere = pygame.display.set_mode(boyut) #pencereyi açmaya sağladı

pygame.mouse.set_visible(0)
#Giriş ekranı müziği:
#pygame.mixer.music.load("start_music.mp3")
#pygame.mixer.music.play()
#pygame.mixer.music.set_volume(0.1)
karakterboyutux=karakter.get_size()[0]
karakterboyutuy=karakter.get_size()[0]
x=0
y=0
xYon=1
yYon=1
clock = pygame.time.Clock()
while True: #döngünün amacı pencerenin arkada sürekli açık kalmasını sağlamak.
    
    clock.tick(40)
    for event in pygame.event.get(): #bu kısmın amacı pencerede bir iş yaparken kapanmaması için.Bir pencere aktifleştirdik.
        if event.type==pygame.QUIT:sys.exit()
    mouseX,mouseY=pygame.mouse.get_pos()
    if mouseX + karakter.get_size()[0] > 1000:
        
        mouseX = mouseX-karakter.get_size()[0]
       
        
    if mouseY + karakter.get_size()[1] >800:
        
        
        mouseY = mouseY-karakter.get_size()[1]
        
    pencere.blit(karakter,(mouseX,mouseY))
    if x>1000-karakterboyutux or x<0: 
        xYon*=-1  
    if y>800-karakterboyutuy or y<0:
        yYon*=-1
    x+=8*xYon
    y+=8*yYon 
    
    #sol,orta,sag = pygame.mouse.get_pressed()
    #if sol == 1:
       # pygame.mixer.music.unpause()
    #if sag == 1:
       # pygame.mixer.music.pause()    
    pencere.blit(arka_plan,(0,0)) #pencerede yazıyı gösterme o,o is x,y ekseni.
    pencere.blit(karakter,(0,685))
    pygame.display.update() #yazının hareket etmesini sağlayan