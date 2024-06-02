"""
    Can Detect Collision 
    Can access x and y points

    two ways of creating react 
        1. pygame.Rect(x,y, width , height)
        2.surface.get_rect() # creates rect around a surface/image
"""

#import
import pygame

#initialize
pygame.init()

#Create Window
width, height = 1280 , 720
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Atharva Pygame")

#Intialize Clock for FPS
fps=30
clock = pygame.time.Clock()

#load image
imgBackground= pygame.image.load("C:/Users/Atharva/OneDrive/Documents/computer vision gameDev/Resources/2.jpg").convert()
imgBallonpng=pygame.image.load("C:/Users/Atharva/OneDrive/Documents/computer vision gameDev/Resources/3.png").convert_alpha()
rectBallon= imgBallonpng.get_rect()

#Rect
rectNew=pygame.Rect(500,0,200,200)

#main loop
start= True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start= False
            pygame.quit()

    #apply logic
        print(rectBallon.colliderect(rectNew))

        rectBallon.x += 2 # rectBallon.x=rectBallon.x+5
        rectBallon.y += 2

        window.fill((255 , 255 , 255)) # 2^8=256 0 to 255 8 here means bits
        window.blit(imgBackground ,(0,0))
        # window.blit(imgBallonpng,(rectBallon))
        pygame.draw.rect(window,(0, 255, 0),rectBallon)
        pygame.draw.rect(window,(0, 255, 0),rectNew) #this logic to make pic inside the rec
        window.blit(imgBallonpng,(rectBallon))


    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)
