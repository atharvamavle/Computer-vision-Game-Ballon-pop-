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
        red, green, blue = (255,0,0), (0,255,0), (0,0,255)
        pygame.draw.polygon(window,red,((491,100),(788,100),(937,357),(788,614),(491,614),(342,357)))
        pygame.draw.circle(window, green, (640,360),200) # so here width=1280/2=640 and height 720/2=360 to find centre 
        pygame.draw.line(window,blue,(468,392),(812,392),10) # (468,392) is (X1 ,Y1) and (812,392) is (X2, Y2)
        pygame.draw.rect(window,blue,(468,307,345,70), border_radius=20)
        

    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)