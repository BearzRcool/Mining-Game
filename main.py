import pygame
import random
from player import Player
from block import Block
import constants
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((constants.SCREENWIDTH,constants.SCREENHEIGHT))
screen.fill("light blue")

player = Player(200,250)

blocks = pygame.sprite.Group()
for i in range(constants.SCREENWIDTH // Block.BLOCKSIZE +1):
    block = Block(Block.BLOCKSIZE*i,300)
    blocks.add(block)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    
    player.update(keys)
    blocks.update()

    screen.fill("light blue")
    blocks.draw(screen)
    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)