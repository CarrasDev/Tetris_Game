import pygame

from game import Piece, Board, Game, SHAPES, COLORS

# Constantes de tamaño
CELL_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = CELL_SIZE * BOARD_HEIGHT


# Código para iniciar pygame y crear una ventana de prueba
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris Test")

game = Game(BOARD_WIDTH, BOARD_HEIGHT)
clock = pygame.time.Clock()

def draw_board(screen, game):
    # Dibujar fondo
    screen.fill((0, 0, 0))
    # Dibujar celdas del tablero
    for y, row in enumerate(game.board.get_grid()):
        for x, color in enumerate(row):
            if color != (0, 0, 0):
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Dibujar pieza actual
    for x, y in game.current_piece.get_cells():
        pygame.draw.rect(screen, game.current_piece.color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


# TODO: Dibujar tablero y pieza actual en la ventana: Hecho
# TODO: Implementar lógica de juego básica
# TODO: Manejar entrada del usuario para mover y rotar la pieza
# TODO: Implementar caída de piezas y velocidad de juego --> Seguir por aquí
# TODO: Mostrar puntuación, estado del juego y piezas siguientes