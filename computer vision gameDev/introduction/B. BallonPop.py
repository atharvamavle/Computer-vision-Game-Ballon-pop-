#import
import pygame
import cv2 
import numpy as np # control matrices
import random
from cvzone.HandTrackingModule import HandDetector

#initialize
pygame.init()

#Create Window
width, height = 1280 , 720
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Atharva ballon Pop Game")

#Intialize Clock for FPS
fps=30
clock = pygame.time.Clock()

#Webcam
cap=cv2.VideoCapture(0)
cap.set(3,1280) #height
cap.set(4,720) #width

#Images
imgBallon=pygame.image.load("C:/Users/Atharva/OneDrive/Documents/computer vision gameDev/Resources/BalloonRed.png").convert_alpha()

rectBallon=imgBallon.get_rect()
rectBallon.x, rectBallon.y=500,300 #here we are declaring postion of ballon (W,H)

#variables
speed=5
score=0


# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

def resetBallon():
    rectBallon.x=  random.randint(100,img.shape[1]-100)
    rectBallon.y=img.shape[0]+50




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
    hands , img= detector.findHands(img, flipType=True)
    img=cv2.flip(img,1)

    rectBallon.y-= speed #move the ballon up

    if rectBallon.y<0: #We are adding this becuase as soon as ballon reach to the top of window it should be reset
        resetBallon()
        speed+=1

    if hands:
        hand = hands[0]
        x = hand['lmList'][8][0]

        y = hand['lmList'][8][1]

        if rectBallon.collidepoint(x,y):
            resetBallon()
            score+=10
         



    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # we did this because CV use BRG convention and pygame use RGB so we converted
    imgRGB=np.rot90(imgRGB)
    frame=pygame.surfarray.make_surface(imgRGB).convert()
    # frame = pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))


    window.blit(imgBallon,rectBallon)

    font = pygame.font.Font("C:/Users/Atharva/OneDrive/Documents/computer vision gameDev/Resources/text.ttf",50)
    textScore=font.render(f"Score :{score}",True,(255,50,50))
    window.blit(textScore,(35,35))
                    

    #Update Display/Window
    pygame.display.update()

    #set FPs
    clock.tick(fps)