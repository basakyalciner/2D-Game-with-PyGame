# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:48:05 2020

@author: a
"""

import pygame,sys
pygame.init()  #init komutunu amacı pygame kütüphanesini kullanılabilir hale getirme.
#Oyun giriş penceresi oluşturma:
boyut=(800,600) #oyunda kullandığın pencere genişliği
ekran = pygame.image.load("start_ekran.png")
karakter =pygame.image.load("karakter.png")
pencere = pygame.display.set_mode(boyut) #pencereyi açmaya sağladı
#Giriş ekranı müziği:
pygame.mixer.music.load("start_music.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
clock = pygame.time.Clock()
while True: #döngünün amacı pencerenin arkada sürekli açık kalmasını sağlamak.
    
    clock.tick(40)
    for event in pygame.event.get(): #bu kısmın amacı pencerede bir iş yaparken kapanmaması için.Bir pencere aktifleştirdik.
        if event.type==pygame.QUIT:sys.exit()
    sol,orta,sag = pygame.mouse.get_pressed()
    if sol == 1:
        pygame.mixer.music.unpause()
    if sag == 1:
        pygame.mixer.music.pause()    
    pencere.blit(ekran,(0,0)) #pencerede yazıyı gösterme o,o is x,y ekseni.
    pygame.display.update() #yazının hareket etmesini sağlayan