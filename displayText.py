import pygame

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bright_red = (255,128,0)
bright_green = (0,255,128)


def display_text(text, font,color=black) :
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()