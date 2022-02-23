# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:44:57 2020

@author: a
"""

import pygame
import random

pygame.init()


class DusenKareler():
    def __init__(self,DKareX,DKareY,KarelerResim,Hız):
        self.DKareX = DKareX
        self.DKareY = DKareY
        self.KarelerResim = KarelerResim
        self.Hız = Hız

    def Cizim(self,Pencere):
        Pencere.blit(self.KarelerResim,(self.DKareX,self.DKareY))

    def Hareket(self):
        self.DKareY += self.Hız



class BizimOyunumuz():
    def __init__(self):
        self.pencere_yuksekligi = 1000
        self.pencere_genisligi = 800
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi,self.pencere_yuksekligi))
        pygame.display.set_caption("Kare Yakalama")
        self.Clock = pygame.time.Clock()

        self.ArkaPlan = pygame.image.load("background.png").convert_alpha()
        self.BizimKare = pygame.image.load("bunny.png").convert_alpha()
        self.YakalaKare = pygame.image.load("ball.png").convert_alpha()

        self.BizimKareX = 70
        self.BizimKareY = 111

        self.KareSayısı = 10
        self.KareListesi = []


    def Cizim(self):

        self.Pencere.blit(self.ArkaPlan,(0,0))
        self.Pencere.blit(self.BizimKare, (self.BizimKareX, self.BizimKareY))

        for DusKare in self.KareListesi:
            DusKare.Cizim(self.Pencere)

        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"
        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"

        if self.Tus[pygame.K_a]:
            self.BizimKareX -= 5
        elif self.Tus[pygame.K_d]:
            self.BizimKareX += 5



        if len(self.KareListesi) != self.KareSayısı:
            self.KareListesi.append(DusenKareler(random.randint(100,800),-10,self.YakalaKare,random.randint(4,10)))

        for DusKare in self.KareListesi:
            DusKare.Hareket()

            if DusKare.DKareY > 1000:
                DusKare.DKareY = -10
                DusKare.DKareX = random.randint(100,800)

        self.Cizim()



Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()