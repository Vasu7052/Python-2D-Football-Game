import pygame
import random
import time
import Things
import intro
import buttons
import displayText
import Paused

pygame.init()
clock = pygame.time.Clock()
sound = pygame.mixer.Sound("sounds/sound.wav")   
pygame.mixer.music.load('sounds/music.mp3')
#pygame.mixer.music.play(-1)
backImg = pygame.image.load('images/background.png')
ballImg = pygame.image.load('images/football.png')
goalLeftImg = pygame.image.load('images/goalLeft.png')
goalRightImg = pygame.image.load('images/goalRight.png')   
boyFirstLeftNormalImg = pygame.image.load('images/boyFirstNormalLeft.png')
boyFirstRightNormalImg = pygame.image.load('images/boyFirstNormalRight.png')
boyFirstLeftKickImg = pygame.image.load('images/boyFirstKickLeft.png')
boyFirstRightKickImg = pygame.image.load('images/boyFirstKickRight.png')
display_width = 1200
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Football')
pygame.display.set_icon(ballImg)



white = (255,255,255)  
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red = (255,128,0)
bright_green = (0,255,128)

goal_width = goalLeftImg.get_rect().size[0]
goal_height = goalLeftImg.get_rect().size[1]

gravityAcceleration = 0.3
horizontalAcceleration = 0
verticalSpeed = [0, 0]
horizontalSpeed = [0, 0]
ballrect = ballImg.get_rect()   
ball_width = ballrect.size[0]
ball_height = ballrect.size[1]
ball_x = 600
ball_y = 300
   
boyGravityAcceleration = 0.3
boyVerticalSpeed = [0, 0]
boyRect = boyFirstRightNormalImg.get_rect()
boy_width = boyRect.size[0]
boy_height = boyRect.size[1]
boy_x = display_width/2
boy_y = display_height - boy_height
boy_x_change = 0
boy_y_change = 0

score_left = 0
score_right = 0


def background(x, y):
    gameDisplay.blit(backImg, (x, y))

def goal(x1,y1 , x2,y2):
    gameDisplay.blit(goalLeftImg, (x1, y1))
    gameDisplay.blit(goalRightImg, (x2, y2))

def ball(x,y) :
    gameDisplay.blit(ballImg,(x,y))

def firstBoy(type,x,y):
    if type == 'normal left' :
        gameDisplay.blit(boyFirstLeftNormalImg,(x,y))
    elif type == 'normal right' :
        gameDisplay.blit(boyFirstRightNormalImg, (x, y))
    elif type == 'kick left' :
        gameDisplay.blit(boyFirstLeftKickImg, (x, y))
    elif type == 'kick right' :
        gameDisplay.blit(boyFirstRightKickImg, (x, y))


intro.game_intro(gameDisplay,display_width,display_height,sound)

crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    background(0,0)
    goal(0,display_height-goal_height,display_width-goal_width,display_height-goal_height)

    '''    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            horizontalSpeed[0] = 0
            horizontalSpeed[1] = -10
        if event.key == pygame.K_RIGHT:
            horizontalSpeed[0] = 0
            horizontalSpeed[1] = 10
        if event.key == pygame.K_UP :
            verticalSpeed[0] = 0
            verticalSpeed[1] = -10
        if event.key == pygame.K_p:
            Paused.paused(gameDisplay, display_width, display_height, True)
    '''

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            boy_x_change = -15
        if event.key == pygame.K_RIGHT:
            boy_x_change = 15
        if event.key == pygame.K_UP :
            boy_y_change = -15
        if event.key == pygame.K_DOWN:
            if boy_y < display_height-boy_height :
                boy_y_change = 15
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            boy_x_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            boy_y_change = 0

        if event.key == pygame.K_p:
            Paused.paused(gameDisplay, display_width, display_height, True)

    boy_x += boy_x_change
    boy_y += boy_y_change


    boyVerticalSpeed[0] = boyGravityAcceleration + boyVerticalSpeed[1]
    boy_y += boyVerticalSpeed[0]
    boyVerticalSpeed[1] = boyVerticalSpeed[0]

    if boy_x < 0 :
        boy_x = 0
    if boy_x > (display_width - boy_height ):
        boy_x = display_width - boy_height
    if boy_y < 0:
        boy_y = 0
        boyVerticalSpeed = [0, 0]
    if boy_y > display_height - boy_height :
        boy_y = display_height - boy_height
        boyVerticalSpeed = [-boyVerticalSpeed[0] * 0.7, -boyVerticalSpeed[1] * 0.7]

    verticalSpeed[0] = gravityAcceleration + verticalSpeed[1]
    ball_y += verticalSpeed[0]
    verticalSpeed[1] = verticalSpeed[0]

    horizontalSpeed[0] = horizontalAcceleration + horizontalSpeed[1]
    ball_x += horizontalSpeed[0]
    horizontalSpeed[1] = horizontalSpeed[0]

    if ball_x < 0 :
        ball_x = 0
        horizontalSpeed = [-horizontalSpeed[0] * 0.7, -horizontalSpeed[1] * 0.7]
    if ball_x > (display_width - ballrect.right):
        ball_x = display_width - ballrect.right
        horizontalSpeed = [-horizontalSpeed[0] * 0.7, -horizontalSpeed[1] * 0.7]
    if ball_y < 0:
        ball_y = 0
        verticalSpeed = [0, 0]
    if ball_y > (display_height - ballrect.bottom):
        ball_y = display_height - ballrect.bottom
        verticalSpeed = [-verticalSpeed[0] * 0.7, -verticalSpeed[1] * 0.7]
        if (ball_y == (display_height - ballrect.height)):
            horizontalSpeed = [horizontalSpeed[0] * 0.95, horizontalSpeed[1] * 0.95]

    if ball_x > boy_x+boy_width-10 and ball_x < boy_x+boy_width+10 and ball_y+(ball_height/2) > boy_y and ball_y+(ball_height/2) < boy_y+boy_height :
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        firstBoy('kick right', boy_x, boy_y)
    if  ball_x+ball_width < boy_x+10 and ball_x+ball_width > boy_x-10 and ball_y+(ball_height/2) > boy_y and ball_y+(ball_height/2) < boy_y+boy_height :
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = -10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        firstBoy('kick left', boy_x, boy_y)
    if  ball_x+(ball_width/2) > boy_x and ball_x+(ball_width/2) < boy_x+boy_width and ball_y+(ball_height) < boy_y+10 and ball_y+(ball_height) > boy_y-10 :
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        firstBoy('kick right', boy_x, boy_y)

    if ball_x > 0 and ball_x < goal_width-ballrect.right and ball_y < display_height and ball_y > display_height-goal_height :
        score_left += 1
        Paused.paused(gameDisplay,display_width,display_height,'Player 1 scores',True)
        ball_x = 600
        ball_y = 300-(ballrect.right/2)
        gravityAcceleration = 0.3
        horizontalAcceleration = 0
        verticalSpeed = [0, 0]
        horizontalSpeed = [0, 0]

    if ball_x > (display_width - goal_width) and ball_x < display_width and ball_y < display_height and ball_y > display_height-goal_height :
        score_right += 1
        Paused.paused(gameDisplay, display_width, display_height, 'Player 2 scores', True)
        ball_x = 600
        ball_y = 300 - (ballrect.right / 2)
        gravityAcceleration = 0.3
        horizontalAcceleration = 0
        verticalSpeed = [0, 0]
        horizontalSpeed = [0, 0]


    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = displayText.display_text(str(score_left) + " | " + str(score_right), largeText)
    TextRect.center = ((display_width / 2), 20)
    gameDisplay.blit(TextSurf, TextRect)

    gameDisplay.blit(ballImg, (ball_x, ball_y))
    if ball_x >= (display_width/2) :
        firstBoy('normal right', boy_x, boy_y)
    elif ball_x < (display_width/2) :
        firstBoy('normal left', boy_x, boy_y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()