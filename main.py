import pygame
pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Tetris Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()