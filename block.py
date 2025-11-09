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

    def update(self,player_rect): #screen offsetting and other
        self.collisions(player_rect)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def collisions(self,player_rect):
        if self.rect.colliderect(player_rect):
            if self.rect.top <= player_rect.bottom:
                player_rect.y = self.rect.top-45
                print("if 1")
            elif self.rect.bottom <= player_rect.top:
                player_rect.y = self.rect.bottom+1
                print("if 2")
            if self.rect.left <= player_rect.right and player_rect.y > self.rect.top and player_rect.y < self.rect.bottom:
                player_rect.x = self.rect.left-1
                print("if 3")
            elif self.rect.right >= player_rect.left and player_rect.y > self.rect.top and player_rect.y < self.rect.bottom:
                player_rect.x = self.rect.right+1
                print("if 4")