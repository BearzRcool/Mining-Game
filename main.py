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
shop_exit_rect = shop_exit.get_rect()
shop_exit_rect.x = 375
shop_exit_rect.y = 25

shop_sell = pygame.Surface((25, 25))
shop_sell.fill("green")
shop_sell_rect = shop_sell.get_rect()
shop_sell_rect.x = 200
shop_sell_rect.y = 300

#TEXT:
font = pygame.font.SysFont("Arial", 20)

global grass
global ore 
grass = 0
ore = 0



shopkeeper = Shop(70,250)

shopkeeper.gamemode = "main"


player = Player(200,250)
plane = [[],[],[],[],[]]
drill = Drill(0,0)
for rows in range(0,5):
    for i in range(constants.SCREENWIDTH // Block.BLOCKSIZE +1):
        if i <= 2 and rows == 0:
            block = Block(Block.BLOCKSIZE*i,300+rows*Block.BLOCKSIZE, False)
        block = Block(Block.BLOCKSIZE*i,300+rows*Block.BLOCKSIZE)
        plane[rows].append((block.rect.x,block.rect.y))

block = Block(Block.BLOCKSIZE+100,250)


def MainScreen():
    grass = 0
    ore = 0
    money = Player.money
    touching.empty()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
            Player.money = 1000

    for item in Player.inventory:
        if item == "grass":
            grass +=1
        elif item =="ore":
            ore +=1
    
    text_surface1 = font.render(f"Money: {money}", True, (0,0,0))
    text_surface2 = font.render(f"Grass: {grass}", True, (0,0,0))
    text_surface3 = font.render(f"Ore: {ore}", True, (0,0,0))

    
    
    # inventory_surface = font.render("", True, (0,0,0)) tried to make surface of text surfaces, didnt work
    # inventory_surface.blit(font.render("Inventory: ", True, (0,0,0)), (0,0))
    # inventory_surface.blit(font.render(f"grass: {grass}", True, (0,0,0)), (0,10))
    # inventory_surface.blit(font.render(f"ore: {ore}", True, (0,0,0)), (0,20))

    screen.fill("blue")
    screen.blit(text_surface1, (0,0))
    screen.blit(text_surface2, (0,25))
    screen.blit(text_surface3, (0,50))
    blocks.update(screen,player.rect)
    for c in touching:
        player.colliding(c)
    player.update(screen,keys,blocks,drill,plane)
    
    
    
def ShopScreen():
    screen.blit(shop_background,(0,0))
    screen.blit(shop_exit, shop_exit_rect)
    screen.blit(shop_sell, shop_sell_rect)
    shopkeeper.update(screen,player.rect, Player.money, shop_exit_rect,shop_sell_rect)

while True:
    if shopkeeper.gamemode == "main":
        MainScreen()
        shopkeeper.update(screen,player.rect, Player.money, shop_exit_rect, shop_sell_rect)
    elif shopkeeper.gamemode == "shop":
        ShopScreen()
        
        
    
    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)