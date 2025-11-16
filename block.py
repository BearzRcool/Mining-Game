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

    def update(self,screen,player_rect): #screen offsetting and other
        self.draw(screen)
        if self.rect.colliderect(player_rect):
            self.collisions(player_rect)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def collisions(self,player_rect):
        if self.rect.left >= player_rect.right and player_rect.bottom > self.rect.top:
            player_rect.x = self.rect.left-1
            # print("if 3")
        if self.rect.right <= player_rect.left and player_rect.bottom > self.rect.top:
            player_rect.x = self.rect.right+1
            # print("if 4")
        if self.rect.top <= player_rect.bottom and self.rect.left < player_rect.right and self.rect.right > player_rect.left:
            player_rect.y = self.rect.top-49
            # print("if 1")
        if self.rect.bottom <= player_rect.top and self.rect.left < player_rect.right and self.rect.right > player_rect.left:
            player_rect.y = self.rect.bottom+1
            # print("if 2")
        