import pygame
height = 500
width = 600
win = pygame.display.set_mode((height, width))

clientNumber = 0

def redrawWindow():
    win.fill(255,255,255)
    pygame.display.update