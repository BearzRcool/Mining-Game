import pygame
import constants
class Block(pygame.sprite.Sprite): #calling the built in pygame sprite class
    BLOCKSIZE = 50
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self) #initializing the sprite class
        self.image = pygame.image.load("grass.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.BLOCKSIZE,self.BLOCKSIZE))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def update(self): #screen offsetting and other
        pass
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)