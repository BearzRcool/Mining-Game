import pygame
import constants
import random
blocks = pygame.sprite.Group()
touching = pygame.sprite.Group()
class Block(pygame.sprite.Sprite): #calling the built in pygame sprite class
    BLOCKSIZE = 50
    def __init__(self, posx, posy, destructable=True):
        pygame.sprite.Sprite.__init__(self,blocks) #initializing the sprite class
        #self.image = pygame.image.load("Images/grass.png").convert_alpha()
        self.image = pygame.Surface((self.BLOCKSIZE, self.BLOCKSIZE))
        self.image.fill("dark green") #(0,100,0)
        #self.image = pygame.transform.scale(self.image,(self.BLOCKSIZE,self.BLOCKSIZE))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.player = None
        self.destroyed = False
        self.destructable = destructable
        self.animation = [] #list of all the images

        self.repeats = 0
        self.colorChange = 0 #in place for animationbs rn

        self.type = random.choice(["grass","ore"])

    def update(self,screen,player): #screen offsetting and other
        self.draw(screen)
        # if self.destroyed:
        #     return
        # if player.speed.x >= player.rect.right - self.rect.left:
        #     player.speed.x = 0
        #     player.rect.right = self.rect.left-1
        # if player.speed.x <= player.rect.left - self.rect.right:
        #     player.speed.x = 0
        #     player.rect.left = self.rect.right+1
        # if player.speed.y >= player.rect.bottom - self.rect.top: 
        #     print("standing on something")
        #     player.speed.y = 0
        #     player.rect.bottom = self.rect.top
        # if player.speed.y >= self.rect.bottom - player.rect.top:
        #     player.speed.y = 0
        #     player.rect.top = self.rect.bottom
        if self.rect.colliderect(player.rect) and self.destroyed == False:
            
            touching.add(self)

        
        
        
    def draw(self,screen):
        if not self.destroyed:
            screen.blit(self.image,self.rect)
    def updateDestroyed(self,isDestroyed):
        self.destroyed = isDestroyed

