import pygame

from game import Piece, Board, Game, SHAPES, COLORS




# Código para iniciar pygame y crear una ventana de prueba
pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Tetris Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()