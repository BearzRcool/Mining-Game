import pygame
import constants
from block import Block
import time
from drill import Drill



class Player():
    #STATIC VARIABLES, AFFECTS EVERY OBJECT OF THIS CLASS
    PlayerSpeed = 5
    inventory = []
    money = 0
    def __init__(self,posx,posy):
        #self.image = pygame.image.load("Images/player.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image,(25,50))
        self.image = pygame.Surface((25, 49.5))
        self.image.fill("red")
      
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.speed = pygame.Vector2()
        self.gravity = constants.GRAVITY
        self.original_pos = self.rect.y
        self.jump = False
        self.startTime = time.time()
        self.timer = True

        

    def draw(self,screen):
        screen.blit(self.image,self.rect)
    
    def onground(self, blocks, detection):
        for block in blocks:
            if not block.destroyed: #and block.rect.top - self.rect.bottom > self.speed.y:
                if self.rect.bottom <= block.rect.top and self.rect.bottom >= block.rect.top:
                    if self.rect.left <= block.rect.right and self.rect.left >= block.rect.left:
                        # if detection == True:
                            
                        #     self.rect.bottom = block.rect.top
                        #     self.speed.y = 0
                        #     break
                        return block #block you are standing on
                    
                    if self.rect.right >= block.rect.left and self.rect.right <= block.rect.right:
                        # if detection == True:
                            
                        #     self.rect.bottom = block.rect.top
                        #     self.speed.y = 0
                        return block #block you are standing on
        return False
        

        
    def update(self,screen,keys,blocks,drill,plane):
        
        if self.timer:
            self.startTime = time.time()


        self.speed.x = 0
        self.draw(screen)

        if keys[pygame.K_RIGHT]:
            if drill.drill_state != 'right':
                drill.drill_state = 'right'
                drill.image = drill.original_image
            drill.rect.x = self.rect.x + 25
            drill.rect.y = self.rect.y + 15 
            drill.update(screen)
        elif keys[pygame.K_LEFT]:
            if drill.drill_state != 'left':
                drill.image = pygame.transform.rotate(drill.original_image, 180)
                drill.rect = drill.image.get_rect(center=drill.rect.center)
                drill.drill_state = 'left'  
            drill.rect.x = self.rect.x - 30
            drill.rect.y = self.rect.y + 15 
            drill.update(screen)
            
        elif keys[pygame.K_UP]:
            if drill.drill_state != 'up':
                drill.drill_state = 'up'
                drill.image = pygame.transform.rotate(drill.original_image, 90)
                drill.rect = drill.image.get_rect(center=drill.rect.center)
            drill.rect.x = self.rect.x - 5
            drill.rect.y = self.rect.y - 20
            drill.update(screen)
            

        elif keys[pygame.K_DOWN]:
            if drill.drill_state != 'down':
                drill.drill_state = 'down'
                drill.image = pygame.transform.rotate(drill.original_image, -90)
                drill.rect = drill.image.get_rect(center=drill.rect.center)
            drill.rect.x = self.rect.x - 5
            drill.rect.y = self.rect.y + 40
            drill.update(screen)
        else:
            drill.rect.x = 0
            drill.rect.y = 0
            
        drill_check = self.drill_colliding(blocks,drill)
        if drill_check and drill_check.destructable == True:
            self.timer = False
            drill_check.x = 1000
        
            length = len(drill_check.animation)
            length = 5 #change later
            
            

            current = time.time()
           

            if current - self.startTime > Drill.drill_speed:
                self.startTime = current
                drill_check.colorChange += 10
                drill_check.image.fill((0,100-drill_check.colorChange,0)) #drill_check.currentFrame = drill_check.animation[repeats]
                drill_check.repeats+=1
                
            if drill_check.repeats == length:
                self.inventory.append(drill_check.type)
                drill_check.destroyed = True
                self.timer = True
                drill_check.repeats = 0
                drill_check.colorChange = 0
                drill_check.image.fill('dark green')
        else:
            for block in blocks:
                block.image.fill('dark green')
                block.repeats = 0
                block.colorChange = 0


        #movement
        if keys[pygame.K_a]:
            self.rect.x -= self.PlayerSpeed
            self.speed.x = -self.PlayerSpeed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[pygame.K_d]:
            self.rect.x += self.PlayerSpeed
            self.speed.x += self.PlayerSpeed
            if self.rect.x > constants.SCREENWIDTH-25:
                self.rect.x = constants.SCREENWIDTH-25
        if keys[pygame.K_s]:
                if block.destroyed:
                    if self.rect.x > block.rect.left and self.rect.x < block.rect.right:   
                        if self.rect.bottom < block.rect.top and self.rect.bottom > block.rect.top - 25:
                            if block.type == 'grass' and 'grass' in self.inventory:
                                self.inventory.remove('grass')
                                block.updateDestroyed(False)
                            elif block.type == 'ore' and 'ore' in self.inventory:
                                self.inventory.remove('ore')
                                block.updateDestroyed(False)

                           
                            

        #jump
        if keys[pygame.K_w] and self.onground(blocks, False):
            self.speed.y = constants.PLAYERVELOCITY
            self.jump = True
    
        if not self.onground(blocks, False):
            self.jump = True

        if self.jump:
            self.jumping(blocks)

        self.onground(blocks, True)
    def jumping(self, blocks):
        if self.speed.y <= -5:
            self.speed.y = -5
        self.rect.y -= self.speed.y
        self.speed.y -= self.gravity
        
        if self.onground(blocks, False):
            self.speed.y = 0
            self.jump = False

    
    
    def colliding(self, block): #print out the block edges to check hitboxes to check if there is slight edge overlapping, can fix by making the top check smaller
        if not block.destroyed:
            
            if self.speed.x >= self.rect.right - block.rect.left:
                self.speed.x = 0
                self.rect.right = block.rect.left
            if self.speed.x <= self.rect.left - block.rect.right:
                self.speed.x = 0
                self.rect.left = block.rect.right
            
            if abs(self.speed.y) >= self.rect.bottom - block.rect.top: 
                self.speed.y = 0
                self.rect.bottom = block.rect.top
            print(f"checking player y = {self.speed.y} >= {block.rect.bottom} - {self.rect.top}")
            #if you are about to hit your head:
            if self.speed.y >= block.rect.bottom - self.rect.top:
                self.speed.y = 0
                self.rect.top = block.rect.bottom
            #if you are already inside the block:
            if self.rect.top < block.rect.bottom and (self.rect.left < block.rect.right or self.rect.right > block.rect.left) and self.jump and self.rect.bottom > block.rect.bottom:
                self.speed.y = 0
                # self.rect.top = block.rect.bottom
           
        
    def drill_colliding(self,blocks,drill): #return a block
        for block in blocks:
            if not block.destroyed:
                if drill.drill_state == "up":
                    drill_top = drill.rect.midtop
                    if drill_top[1] <= block.rect.bottom and drill_top[1] >= block.rect.top:
                        if drill_top[0] <= block.rect.right and drill_top[0] >= block.rect.left:
                            return block #block you are drilling
                if drill.drill_state == "down":
                    drill_bottom = drill.rect.midbottom
                    if drill_bottom[1] >= block.rect.top and drill_bottom[1] <= block.rect.bottom:
                        if drill_bottom[0] <= block.rect.right and drill_bottom[0] >= block.rect.left:
                            return block #block you are drilling
                if drill.drill_state == "left":
                    drill_left = drill.rect.midleft
                    if drill_left[1] >= block.rect.top and drill_left[1] <= block.rect.bottom:
                        if drill_left[0] <= block.rect.right and drill_left[0] >= block.rect.left:
                            return block #block you are drilling

                if drill.drill_state == "right":
                    drill_right = drill.rect.midright
                    if drill_right[1] >= block.rect.top and drill_right[1] <= block.rect.bottom:
                        if drill_right[0] <= block.rect.right and drill_right[0] >= block.rect.left:
                            return block #block you are drilling
                            
        return False
        

        

