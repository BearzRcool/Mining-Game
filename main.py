import pygame
import random
from player import Player
from block import Block
from shopkeeper import Shop
import constants

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((constants.SCREENWIDTH,constants.SCREENHEIGHT))
screen.fill("light blue")

money = 10

player = Player(200,250)

blocks = pygame.sprite.Group()
for i in range(constants.SCREENWIDTH // Block.BLOCKSIZE +1):
    block = Block(Block.BLOCKSIZE*i,300)
    blocks.add(block)
block = Block(Block.BLOCKSIZE+100,250)
blocks.add(block)

shopkeeper = Shop(70,250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
            money = 1000

    screen.fill("light blue")

    player.update(screen,keys,blocks,money)
    blocks.update(screen,player.rect)
    shopkeeper.update(screen,player.rect, money)


   

    pygame.display.flip()

    clock.tick(60)