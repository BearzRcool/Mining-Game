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

money = 10

player = Player(200,250)

drill = Drill(-10,-10)

for i in range(constants.SCREENWIDTH // Block.BLOCKSIZE +1):
    block = Block(Block.BLOCKSIZE*i,300)
    
block = Block(Block.BLOCKSIZE+100,250)


#shopkeeper = Shop(70,250)

while True:
    touching.empty()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
            money = 1000

    screen.fill("light blue")
    
    blocks.update(screen,player.rect)
    for c in touching:
        player.colliding(c)
    player.update(screen,keys,blocks,drill)
    
    print ("x " + str(player.rect.x) + " y " + str(player.rect.y))
    #shopkeeper.update(screen,player.rect, money)


   

    pygame.display.flip()

    clock.tick(60)