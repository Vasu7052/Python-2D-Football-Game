import pygame
import buttons
import displayText

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bright_red = (255,128,0)
bright_green = (0,255,128)



def paused(gameDisplay,display_width,display_height,message,pause=False):
    #gameDisplay.fill(white)

    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = displayText.display_text(message, largeText , white)
    TextRect.center = ((display_width / 2), (display_height / 5))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        continueAction = None

        continueAction = buttons.button(gameDisplay,"Continue", 350, 250, 100, 50, green, bright_green,'continue_game')
        buttons.button(gameDisplay,"Quit", 750, 250, 100, 50, red, bright_red)

        if continueAction is 'continueGame' :
            pause = False

        pygame.display.update()
        clock.tick(15)