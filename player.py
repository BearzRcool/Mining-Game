import pygame
import constants

class Player():
    PLAYERSPEED = 5
    def __init__(self,posx,posy):
        #self.image = pygame.image.load("Images/player.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image,(25,50))
        self.image = pygame.Surface((25, 50))
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

        
    def update(self,screen,keys,blocks,drill):
        self.speed.x = 0
        self.draw(screen)
         #drill ROTATING NOT WORKING
        if keys[pygame.K_RIGHT]:
            if drill.drill_state != 'right':
                drill.drill_state = 'right'
                drill.image = drill.original_image
            drill.rect.x = self.rect.x + 25
            drill.rect.y = self.rect.y + 20
            drill.update(screen)
        elif keys[pygame.K_LEFT]:
            if drill.drill_state != 'left':
                drill.image = pygame.transform.rotate(drill.original_image, 180)
                drill.rect = drill.image.get_rect(center=drill.rect.center)
                drill.drill_state = 'left'  
            drill.rect.x = self.rect.x - 20
            drill.rect.y = self.rect.y + 20
            drill.update(screen)
            
        elif keys[pygame.K_UP]:
            if drill.drill_state != 'up':
                drill.drill_state = 'up'
                drill.image = pygame.transform.rotate(drill.original_image, 90)
                drill.rect = drill.image.get_rect(center=drill.rect.center)
            drill.rect.x = self.rect.x + 3
            drill.rect.y = self.rect.y - 20
            drill.update(screen)
            

        elif keys[pygame.K_DOWN]:
            if drill.drill_state != 'down':
                drill.drill_state = 'down'
                drill.image = pygame.transform.rotate(drill.original_image, -90)
                drill.rect = drill.image.get_rect(center=drill.rect.center)
            drill.rect.x = self.rect.x + 3
            drill.rect.y = self.rect.y + 50
            drill.update(screen)
            
        #movement
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
        #jump
        if keys[pygame.K_w] and self.onground(blocks):
            self.speed.y = constants.PLAYERVELOCITY
            self.jump = True
    
        if not self.onground(blocks):
            self.jump = True

        if self.jump:
            self.jumping(blocks)

    def jumping(self, blocks):
        if self.speed.y <= -5:
            self.speed.y = -5
        self.rect.y -= self.speed.y
        self.speed.y -= self.gravity
        
        if self.onground(blocks):
            self.speed.y = 0
            self.jump = False

    def onground(self, blocks):
        for block in blocks:
            if self.rect.bottom <= block.rect.top+2 and self.rect.bottom >= block.rect.top - 2:
                if self.rect.left <= block.rect.right and self.rect.left >= block.rect.left:
                    return True
                if self.rect.right >= block.rect.left and self.rect.right <= block.rect.right:
                    return True
        return False
    
    def colliding(self, block):
        if self.speed.x >= self.rect.right - block.rect.left:
            self.speed.x = 0
            self.rect.right = block.rect.left
        if self.speed.x <= self.rect.left - block.rect.right:
            self.speed.x = 0
            self.rect.left = block.rect.right
        if self.speed.y >= self.rect.bottom - block.rect.top:
            self.speed.y = 0
            self.rect.bottom = block.rect.top
        if self.speed.y <= self.rect.top - block.rect.bottom:
            self.speed.y = 0
            self.rect.top = block.rect.bottom+1

