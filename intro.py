import pygame
import displayText
import buttons

clock = pygame.time.Clock()

def game_intro(gameDisplay,display_width,display_height,sound) :
    white = (255,255,255)
    black = (0,0,0)

    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)

    bright_red = (255,128,0)
    bright_green = (0,255,128)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        introAction = None

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = displayText.display_text("Football Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        introAction = buttons.button(gameDisplay,"Go",400,450,100,50,green,bright_green,'close_intro')
        buttons.button(gameDisplay,"Cancel",800,450,100,50,red,bright_red,'close_game')

        if introAction is 'closeIntroClicked' :
            #pygame.mixer.Sound.play(sound)
            #pygame.mixer.music.stop()
            intro = False

        pygame.display.update()
        clock.tick(15)