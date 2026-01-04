import pygame
import constants

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

    def update(self,screen,player_rect,money,exit_button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.draw(screen)
        if self.rect.colliderect(player_rect):
            self.gamemode = 'shop'
            self.shop(money,player_rect,exit_button)
    
    def shop(self, money,player_rect, exit_button):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if exit_button.collidepoint(mouse):
            if click[0]:
                player_rect.x += 50  # Move player away from shopkeeper to avoid immediate re-entry
                self.gamemode = "main"
        # items = self.items.keys()
        # item = input("What do you want to buy?").lower()
        # if item in list(items):
        #     if money >= self.items[item]:
        #         chosen_item = self.items.pop(item)
        #         money -= chosen_item
        #         print(money)
        #         print(items)
            

        

           