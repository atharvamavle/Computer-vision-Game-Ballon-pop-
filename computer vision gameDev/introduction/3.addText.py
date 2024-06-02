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
        font = pygame.font.Font("C:/Users/Atharva/OneDrive/Documents/computer vision gameDev/Resources/text.tff",20).convert() #none means you can add external file
        text=font.render("Atharva Game",True,(50,50,50)) # here True means to create smooth text
        window.blit(text, (350,300)) # this is actually use to print on window 

    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)

