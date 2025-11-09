import pygame
import constants
class Player():
    PLAYERSPEED = 5
    def __init__(self,posx,posy):
        self.image = pygame.Surface([25,45])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.velocity = 0
        self.gravity = constants.GRAVITY
        self.original_pos = self.rect.y
        self.jump = False
    def draw(self,screen):
        screen.blit(self.image,self.rect)

        
    def update(self,keys,blocks):
        if keys[pygame.K_a]:
            self.rect.x -= self.PLAYERSPEED
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[pygame.K_d]:
            self.rect.x += self.PLAYERSPEED
            if self.rect.x > constants.SCREENWIDTH-25:
                self.rect.x = constants.SCREENWIDTH-25
        if keys[pygame.K_w] and self.onground(blocks):
            self.velocity = constants.PLAYERVELOCITY
            self.jump = True
        print(self.onground(blocks))
        if self.onground(blocks) == False:
            self.jump = True

        if self.jump:
            self.jumping(blocks)
    def jumping(self,blocks):
        

        self.rect.y-=self.velocity
        self.velocity-=self.gravity
        
        if self.onground(blocks):
            self.velocity = 0
            self.jump = False

    def onground(self,blocks):
        for block in blocks:
            if block.rect.colliderect(self.rect):
                return True
        return False
        