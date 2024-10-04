# Stas Pong v1.0 completed on 26 September 2024

import pygame
import random
import time
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200,200,200)
GREY2 = (150,150,150)
GREY3 = (100,100,100)
GREY4 = (50,50,50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

color = (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.image.load("bg.png")
background_image = pygame.image.load("bg.png")
background_image = pygame.image.load("bg.png").convert()

hitsound = pygame.mixer.Sound("blip.wav")

pygame.display.set_caption("Stas' Pong")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

StartX = 325
StartY = 225

RectX = 325
RectY = 225

DX = 4
DY = 4

LastCoord4 = [RectX-DX*8, RectY-DY*8]
LastCoord3 = [RectX-DX*6, RectY-DY*6]
LastCoord2 = [RectX-DX*4, RectY-DY*4]
LastCoord1 = [RectX-DX*2, RectY-DY*2]

VelocityY = 3

VY1 = 0
VY2 = 0
YCoord1 = 200
YCoord2 = 200

# game

InMenu = True
InLostScreen = False

LivesP1 = 3
LivesP2 = 3

fontP1 = pygame.font.SysFont("dejavu", 35, False, False)
fontP2 = pygame.font.SysFont("dejavu", 35, False, False)

# assets???? idk what to call them

#MenuText = """\
#   _____ _______        _____ _  _____   _____   ____  _   _  _____  
#  / ____|__   __|/\    / ____( )/ ____| |  __ \ / __ \| \ | |/ ____| 
# | (___    | |  /  \  | (___ |/| (___   | |__) | |  | |  \| | |  __  
#  \___ \   | | / /\ \  \___ \   \___ \  |  ___/| |  | | . ` | | |_ | 
#  ____) |  | |/ ____ \ ____) |  ____) | | |    | |__| | |\  | |__| | 
# |_____/   |_/_/    \_\_____/  |_____/  |_|     \____/|_| \_|\_____| 
#                                                                     
#                                                                     
#"""

MenuText = "STAS' PONG"
font = pygame.font.SysFont("dejavusans", 90, False, False)

# buttons
Button = pygame.font.SysFont("dejavusans", 30, False, False)

Button1Text = "PLAY 1V1"
Button2Text = "PLAY CPU"
Button3Text = "QUIT"

# SETTINGS

AIEnabled = False # CHANGE THIS IF YOU GOT NOBODY TO PLAY WITH

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP and InMenu:
            pos = pygame.mouse.get_pos()

            if pos[0] >= 280 and pos[0] <= 280+165 and pos[1] >= 192 and pos[1] <= 192+50:
                AIEnabled = False
                InMenu = False
                LivesP1 = 3
                LivesP2 = 3
                YCoord1 = 200
                YCoord2 = 200
                VY1 = 0
                VY2 = 0
            elif pos[0] >= 280 and pos[0] <= 280+165 and pos[1] >= 272 and pos[1] <= 272+50:
                InMenu = False
                AIEnabled = True
                LivesP1 = 3
                LivesP2 = 3
                YCoord1 = 200
                YCoord2 = 200
                VY1 = 0
                VY2 = 0
            elif pos[0] >= 280 and pos[0] <= 280+165 and pos[1] >= 272+80 and pos[1] <= 272+50+80:
                done = True
        
        elif event.type == pygame.KEYDOWN and not InMenu:
            if event.key == pygame.K_s:
                VY1 = VelocityY
            elif event.key == pygame.K_w:
                VY1 = -VelocityY
            elif event.key == pygame.K_DOWN and not AIEnabled:
                VY2 = VelocityY
            elif event.key == pygame.K_UP and not AIEnabled:
                VY2 = -VelocityY
        elif event.type == pygame.KEYUP and not InMenu:
            if event.key == pygame.K_s or event.key == pygame.K_w:
                VY1 = 0
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_UP) and not AIEnabled:
                VY2 = 0
    # --- Game logic should go here

    if AIEnabled and not InMenu:
        if RectY-20 <= YCoord2:
            VY2 = -VelocityY
        elif RectY >= YCoord2 + 30:
            VY2 = VelocityY
        else:
            VY2 = 0
    
    YCoord1 += VY1
    YCoord2 += VY2

    if YCoord1 <= 0:
        YCoord1 = 0

    if YCoord1 >= 400:
        YCoord1 = 400

    if YCoord2 <= 0:
        YCoord2 = 0

    if YCoord2 >= 400:
        YCoord2 = 400

    Bounced = False
    
    if RectX <= 25 and RectY >= YCoord1-50 and RectY <= YCoord1+100:
        RectX = 25
        DX = -DX * 1.05
        color = (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))
        Bounced = True
        hitsound.play()

    if RectX >= 625 and RectY >= YCoord2-50 and RectY <= YCoord2+100:
        RectX = 625
        DX = -DX * 1.05
        color = (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))
        Bounced = True
        hitsound.play()
    
    if (RectX <= 0 or RectX >= 650) and not Bounced:
        color = (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))
        
        if RectX <= 0:
            LivesP1 -= 1
            DX = 4
            DY = -4
        else:
            LivesP2 -= 1
            DX = -4
            DY = 4
        RectX = StartX
        RectY = StartY

    if RectY <= 0 or RectY >= 450:
        hitsound.play()
        DY = -DY
        color = (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))

    if not InMenu:
        if (LivesP1 <= 0 or LivesP2 <= 0):
            InMenu = True
            InLostScreen = True
        else:
            RectX += DX
            RectY += DY

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
    screen.fill(BLACK)

        # --- Drawing code should go here

    if InMenu and InLostScreen:

        PlayerThatLost = "Player 1"
        if LivesP2 <= 0:
            PlayerThatLost = "Player 2"

        LostFont = pygame.font.SysFont("dejavusans", 20, False, False)
        
        fontsurf = LostFont.render(f"{PlayerThatLost} lost... womp womp", True, WHITE)
        screen.blit(fontsurf,(100,100))

        pygame.display.flip()
        
        time.sleep(2.5)

        InLostScreen = False
    elif InMenu and not InLostScreen:

        screen.blit(background_image, [0, 0])
        
        fontsurf = font.render(MenuText, True, WHITE)
        screen.blit(fontsurf,(85,50))

        Button1 = Button.render(Button1Text, True, WHITE)
        Button2 = Button.render(Button2Text, True, WHITE)
        Button3 = Button.render(Button3Text, True, WHITE)

        screen.blit(Button1,(290,200))
        screen.blit(Button2,(290,280))
        screen.blit(Button3,(326,360))

        pygame.draw.rect(screen,WHITE,[280,192,165,50],3)
        pygame.draw.rect(screen,WHITE,[280,272,165,50],3)
        pygame.draw.rect(screen,WHITE,[280,352,165,50],3)
    else:
        screen.blit(background_image, [0, 0])
        pygame.draw.rect(screen,(color[0]/5,color[1]/5,color[2]/5), [LastCoord4[0],LastCoord4[1], 50, 50])
        pygame.draw.rect(screen, (color[0]/4,color[1]/4,color[2]/4), [LastCoord3[0],LastCoord3[1], 50, 50])
        pygame.draw.rect(screen, (color[0]/3,color[1]/3,color[2]/3), [LastCoord2[0],LastCoord2[1], 50, 50])
        pygame.draw.rect(screen, (color[0]/2,color[1]/2,color[2]/2), [LastCoord1[0],LastCoord1[1], 50, 50])

        pygame.draw.rect(screen,RED,[0,YCoord1,20,100])
        pygame.draw.rect(screen,GREEN,[675,YCoord2,20,100])

        pygame.draw.rect(screen,color,[RectX,RectY,50,50])

        LastCoord4 = LastCoord3
        LastCoord3 = LastCoord2
        LastCoord2 = LastCoord1
        LastCoord1 = [RectX,RectY]

        fontsurfP1 = fontP1.render(str(LivesP1), True, RED)
        fontsurfP2 = fontP2.render(str(LivesP2), True, GREEN)

        screen.blit(fontsurfP1,(0,0))
        screen.blit(fontsurfP2,(685,0))
        
        # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(40)

    # Close the window and quit.
pygame.quit()