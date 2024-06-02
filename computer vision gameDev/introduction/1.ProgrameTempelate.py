"""
Pygame tempelates

    import 
    initialize
    Create Window
    Intialize Clock for FPS

    Loop
        Get events
            if quit
                quit game
        Apply Logic
        Update Display/Window
        Set Fps

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

#main loop
start= True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start= False
            pygame.quit()

    #apply logic
        window.fill((255 , 255 , 255)) # 2^8=256 0 to 255 8 here means bits

    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)

