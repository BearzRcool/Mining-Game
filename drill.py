import pygame
import constants
class Drill(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        self.image = pygame.image.load("Images/drill.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(33,33))
        self.rect = self.image.get_rect()
        self.rect.y = posy 
        self.rect.x = posx
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    
    def update(self,screen):
        self.draw(screen)
        