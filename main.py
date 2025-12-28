import pygame
import random
from drill import Drill
from player import Player
from block import *
from shopkeeper import Shop
import constants

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((constants.SCREENWIDTH,constants.SCREENHEIGHT))
screen.fill("light blue")

shop_background = pygame.image.load("Images/shop background.png").convert_alpha()
shop_background = pygame.transform.scale(shop_background,(400,600))
shop_exit = pygame.image.load("Images/exit button.png").convert_alpha()
shop_exit = pygame.transform.scale(shop_exit,(25,25))


shopkeeper = Shop(70,250)

shopkeeper.gamemode = "main"

money = 10

player = Player(200,250)

drill = Drill(0,0)
for j in range(0,5):
    for i in range(constants.SCREENWIDTH // Block.BLOCKSIZE +1):
        block = Block(Block.BLOCKSIZE*i,300+j*Block.BLOCKSIZE)

block = Block(Block.BLOCKSIZE+100,250)




while True:
    if shopkeeper.gamemode == "main":
        touching.empty()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
                money = 1000

        screen.fill("blue")
        
        blocks.update(screen,player.rect)
        for c in touching:
            player.colliding(c)
        player.update(screen,keys,blocks,drill)
        
        
        shopkeeper.update(screen,player.rect, money)
    elif shopkeeper.gamemode == "shop":
        screen.blit(shop_background,(0,0))
        screen.blit(shop_exit,(375, 25))
        pass
   

    pygame.display.flip()

    clock.tick(60)