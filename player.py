import pygame
import constants
class Player():
    PLAYERSPEED = 5
    def __init__(self,posx,posy):
        self.image = pygame.Surface([25,50])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.speed = pygame.Vector2()
        self.gravity = constants.GRAVITY
        self.original_pos = self.rect.y
        self.jump = False
    def draw(self,screen):
        screen.blit(self.image,self.rect)

        
    def update(self,screen,keys,blocks,money):
        self.speed.x = 0
        self.draw(screen)
        if keys[pygame.K_a]:
            self.rect.x -= self.PLAYERSPEED
            self.speed.x = -self.PLAYERSPEED
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[pygame.K_d]:
            self.rect.x += self.PLAYERSPEED
            self.speed.x += self.PLAYERSPEED
            if self.rect.x > constants.SCREENWIDTH-25:
                self.rect.x = constants.SCREENWIDTH-25
        if keys[pygame.K_w] and self.onground(blocks):
            self.speed.y = constants.PLAYERVELOCITY
            self.jump = True
        

        if self.onground(blocks) == False:
            self.jump = True

        if self.jump:
            self.jumping(blocks)
    def jumping(self,blocks):
        

        self.rect.y-=self.speed.y
        self.speed.y-=self.gravity
        
        if self.onground(blocks):
            self.speed.y = 0
            self.jump = False

    def onground(self,blocks):
        for block in blocks:
            if block.rect.colliderect(self.rect):
                return True
        return False
    
    def colliding(self,block):
        if self.speed.x >= self.rect.right - block.rect.left:
            self.speed.x = 0
            self.rect.right = block.rect.left-1
        if self.speed.x <= self.rect.left - block.rect.right:
            self.speed.x = 0
            self.rect.left = block.rect.right+1
        if self.speed.y >= self.rect.bottom - block.rect.top:
            self.speed.y = 0
            self.rect.bottom = block.rect.top-1
        if self.speed.y <= self.rect.top - block.rect.bottom:
            self.speed.y = 0
            self.rect.top = block.rect.bottom+1
'''
example:
speeds = [0,0] ticks of x speed movement and y speed movemet
while true:
if speeds[0] == 0: if no x moevment
    if keys[pygame.K_LEFT]:
        speeds[0] = (-10 set x ticks to -10)
    if keys[pygame.K_RIGHT]:
        speeds[0] = 10 (x ticks to 10)
else:
    if speeds[0] > 0:
        player_Rect.x += 5 
        speeds[0] -= 1
    else:
        player_rect.x -= 5

check if something is there before moving, if there is something, 
amount of ticks and speed should be factors of the block size ex: 5,10 = 50
'''