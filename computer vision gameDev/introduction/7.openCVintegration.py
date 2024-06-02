#import
import pygame
import cv2 
import numpy as np # control matrices

#initialize
pygame.init()

#Create Window
width, height = 1280 , 720
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Atharva Pygame")

#Intialize Clock for FPS
fps=30
clock = pygame.time.Clock()

#Webcam
cap=cv2.VideoCapture(0)
cap.set(3,1280) #height
cap.set(4,720) #width

#main loop
start= True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start= False
            pygame.quit()

    #apply logic
        
    #openCV

    success, img = cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # we did this because CV use BRG convention and pygame use RGB so we converted
    imgRGB=np.rot90(imgRGB)
    frame=pygame.surfarray.make_surface(imgRGB).convert()
    # frame = pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))

    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)