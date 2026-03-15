import pygame
import constants
from player import Player
class Shop(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        #self.image = pygame.image.load("Images/shopkeeper.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image,(50,50))
        
        self.image = pygame.Surface((50,50))
        self.image.fill('white')
        
        self.rect = self.image.get_rect()
        self.rect.y = posy
        self.rect.x = posx
        
        self.gamemode = ''
        self.items = {
            "drill":10,
            "drill v2":50,
            "boots":100,
        }
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self,screen,player_rect,money,buttons, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if self.gamemode != 'shop':
            self.draw(screen)
        if self.rect.colliderect(player_rect):
            self.gamemode = 'shop'
            self.shop(money,player_rect,buttons,player)
    
    def shop(self, money,player_rect,buttons,player):
     
        exit = buttons[0]
        sell = buttons[1]
        buy = buttons[2]

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0]:
            if exit.collidepoint(mouse):
                    player_rect.x += 50  # Move player away from shopkeeper to avoid immediate re-entry
                    self.gamemode = "main"
            elif sell.collidepoint(mouse):
                    for item in Player.inventory:
                        if item == 'grass':
                            Player.money += 1
                        elif item == 'ore':
                            Player.money += 5
                    Player.inventory.clear()
            elif buy.collidepoint(mouse):
                Player.PlayerSpeed += 1
                print(Player.PlayerSpeed)