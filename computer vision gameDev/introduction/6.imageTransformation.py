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
# imgBallonpng=pygame.transform.rotate(imgBallonpng,90)
# imgBallonpng=pygame.transform.flip(imgBallonpng,False,True)
imgBallonpng=pygame.transform.rotozoom(imgBallonpng, 90,0.3)
#main loop
start= True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start= False
            pygame.quit()

    #apply logic

    imgBallonpng=pygame.transform.smoothscale(imgBallonpng, (100,100))

    window.fill((255 , 255 , 255)) # 2^8=256 0 to 255 8 here means bits
    window.blit(imgBackground ,(0,0))
    window.blit(imgBallonpng,(200,300))


    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)