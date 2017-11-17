import pygame
import displayText

def close():
    pygame.quit()
    quit()

def button(gameDisplay,msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action is 'close_intro':
                return 'closeIntroClicked'
            elif action is 'close_game' :
                return 'closeGameClicked'
                close()
            elif action is'continue_game' :
                return 'continueGame'
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = displayText.display_text(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
