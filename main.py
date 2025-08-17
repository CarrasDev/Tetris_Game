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

     
# Variables de control de caída de piezas TODO: Pendiente decidir si declarar en Game o aquí
fall_time = 0 # TODO: ¿Necesario?
fall_speed = 500  # Milisegundos entre caídas de piezas
last_fall_time = pygame.time.get_ticks()


# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_piece(-1, 0)
            elif event.key == pygame.K_RIGHT:
                game.move_piece(1, 0)
            elif event.key == pygame.K_DOWN:
                game.move_piece(0, 1)
            elif event.key == pygame.K_UP:
                game.rotate_piece()
            elif event.key == pygame.K_SPACE:
                game.drop_piece()

                      
    # Lógica de caída de piezas
    current_time = pygame.time.get_ticks()
    if current_time - last_fall_time > fall_speed:
        if game.can_move_down():
            game.move_piece(0, 1)
        else:
            game.drop_piece()
        last_fall_time = current_time
    

    # Dibujar el estado actual del juego
    draw_board(screen, game)
    pygame.display.flip()
    clock.tick(30)  # Limitar a 30 FPS


pygame.quit()


# TODO: Mejorar entrada del usuario para detectar teclas pulsadas permanentemente
# TODO: Mostrar puntuación, estado del juego y piezas siguientes
# TODO: Implementar lógica de fin de juego
# TODO: Implementar lógica de reinicio del juego
# TODO: Mejorar la interfaz gráfica y añadir sonidos