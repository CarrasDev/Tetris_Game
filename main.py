import pygame

from game import Piece, Board, SHAPES, COLORS

#, Game




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


# TODO: Dibujar tablero y pieza actual en la ventana
# TODO: Implementar lógica de juego básica
# TODO: Manejar entrada del usuario para mover y rotar la pieza
# TODO: Implementar caída de piezas y velocidad de juego
# TODO: Mostrar puntuación, estado del juego y piezas siguientes