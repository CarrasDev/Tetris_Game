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
pygame.display.set_caption("Block Game")

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

     
# Variables de control de caída de piezas TODO: Pendiente decidir si declarar en Game o como constantes
fall_time = 0 # TODO: ¿Necesario?
fall_speed = 700  # Milisegundos entre caídas de piezas
move_delay = 80  # Milisegundos entre movimientos
last_fall_time = pygame.time.get_ticks()


# Bucle principal del juego
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
                paused = False
            else:
                if event.key == pygame.K_p:
                    paused = not paused
                if not paused:
                    if event.key == pygame.K_UP:
                        game.rotate_piece()
                    elif event.key == pygame.K_SPACE:
                        game.drop_piece()
    if not paused and not game.game_over:
        # Teclas pulsadas permanentemente
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_LEFT] and current_time - last_fall_time > move_delay:
            game.move_piece(-1, 0)
            last_fall_time = current_time
        if keys[pygame.K_RIGHT] and current_time - last_fall_time > move_delay:
            game.move_piece(1, 0)
            last_fall_time = current_time
        if keys[pygame.K_DOWN] and current_time - last_fall_time > move_delay:
            game.move_piece(0, 1)
            last_fall_time = current_time
                      
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
    if paused:
        font = pygame.font.SysFont('Arial', 30, bold=True)
        text = font.render('PAUSE', True, (255, 255, 255))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, rect)
    if game.game_over:
        font = pygame.font.SysFont('Arial', 40, bold=True)
        text = font.render('GAME OVER', True, (255, 0, 0))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, rect)
    pygame.display.flip()
    clock.tick(30)  # Limitar a 30 FPS


pygame.quit()


# TODO: Mostrar puntuación, Nivel del juego y piezas siguientes
# TODO: Definir puntuación según líneas eliminadas o Tetris(4 líneas a la vez)
# TODO: Implementar lógica de fin de juego
# TODO: Implementar lógica de reinicio del juego
# TODO: Mejorar la interfaz gráfica y añadir sonidos
# TODO: Desacoplar lógica de control de movimiento de piezas y lógica de dibujo