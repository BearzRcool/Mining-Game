import pygame
import constants
blocks = pygame.sprite.Group()
touching = pygame.sprite.Group()
class Block(pygame.sprite.Sprite): #calling the built in pygame sprite class
    BLOCKSIZE = 50
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self,blocks) #initializing the sprite class
        self.image = pygame.image.load("Images/grass.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.BLOCKSIZE,self.BLOCKSIZE))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.player = None

    def update(self,screen,player_rect): #screen offsetting and other
        self.draw(screen)
        if self.rect.colliderect(player_rect):
            touching.add(self)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    