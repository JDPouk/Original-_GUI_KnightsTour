# -*- coding: utf-8 -*-
# import to be used in the code
import pygame
from time import sleep

# clock to controll the fps of the GUI
clock = pygame.time.Clock()

# intialise variables
WIDTH , HEIGHT,FPS  = 722, 722, 30;

BLACK = (0,0,0)
GREEN = (0,255,0)
background_image = pygame.image.load('board.png')
knight = pygame.image.load('Chess-Knight.svg')
des_x = 136;
des_y = 46;
cord_X =()

# the class for the player which should only be an object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       
        self.image =  pygame.transform.scale(knight, (70, 70))
        
        self.rect = self.image.get_rect()
        self.rect.center = (46, 46)

        
    def update(self):
            self.rect.move(136, 46)
            
# creates the varibles for the pygame     
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH , HEIGHT))

clock = pygame.time.Clock()   


    
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
 
# the game loop that updates as the program runs
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
  
    screen.blit( background_image, ( 0,0 ) )
    all_sprites.draw(screen)
   
    pygame.display.flip()
            

# Quits the program when the loop has ended
pygame.quit()