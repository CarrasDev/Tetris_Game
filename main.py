import pygame
import ui

from game import Piece, Board, Game, SHAPES, COLORS
from config import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT, SIDE_PANEL_WIDTH, SIDE_PANEL_INCREMENT, GAME_FONT, GAME_FONT_SIZE


# TODO: Provisional refactorización en config.py
'''
CELL_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SIDE_PANEL_INCREMENT = 6

SCREEN_HEIGHT = CELL_SIZE * BOARD_HEIGHT
SIDE_PANEL_WIDTH = CELL_SIZE * SIDE_PANEL_INCREMENT
SCREEN_WIDTH = CELL_SIZE * BOARD_WIDTH + SIDE_PANEL_WIDTH

GAME_FONT = 'Consolas'
GAME_FONT_SIZE = 20
'''


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Game")

game = Game(BOARD_WIDTH, BOARD_HEIGHT)
clock = pygame.time.Clock()

# TODO: Provisional refactorización en ui.py
'''
def draw_board(screen, game):
    screen.fill((0, 0, 0))
    for y, row in enumerate(game.board.get_grid()):
        for x, color in enumerate(row):
            if color != (0, 0, 0):
                pygame.draw.rect(
                    screen,
                    color,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
    # Dibujar pieza actual
    for x, y in game.current_piece.get_cells():
        pygame.draw.rect(
            screen,
            game.current_piece.color,
            (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )


def draw_side_panel(screen, game):
    font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, bold=True)
    text = font.render('Next:', True, (255, 255, 0))
    next_x = BOARD_WIDTH * CELL_SIZE + 10
    next_y = 10
    screen.blit(text, (next_x, next_y))
    
    next_shape = game.next_piece.get_current_shape()
    color = game.next_piece.color
    offset_x = BOARD_WIDTH * CELL_SIZE + 40
    offset_y = 60
    for y, row in enumerate(next_shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    color,
                    (offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
                
    score_label_font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, bold=True)
    score_label_text = score_label_font.render('Score:', True, (255, 255, 0))
    score_label_x = BOARD_WIDTH * CELL_SIZE + 10
    score_label_y = 180
    screen.blit(score_label_text, (score_label_x, score_label_y))
    
    score_font = pygame.font.SysFont(GAME_FONT, 28, bold=True)
    score_str = f"{game.score:,}".replace(',', '.')
    score_text = score_font.render(score_str, True, (255, 255, 255))
    score_x = score_label_x
    score_y = score_label_y + 30
    screen.blit(score_text, (score_x, score_y))
'''
     
# Variables de control de caída
fall_time = 0
fall_speed = 800  # Milisegundos entre caídas de piezas
move_delay = 50  # Milisegundos entre movimientos
last_fall_time = pygame.time.get_ticks()


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
    ui.draw_board(screen, game)

    pygame.draw.line(
        screen,
        (80, 80, 80),
        (BOARD_WIDTH * CELL_SIZE, 0),
        (BOARD_WIDTH * CELL_SIZE, SCREEN_HEIGHT),
        2
    )

    ui.draw_side_panel(screen, game)

    if paused:
        font = pygame.font.SysFont(GAME_FONT, 20, bold=True)
        text = font.render('PAUSE', True, (255, 255, 255))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, rect)
    if game.game_over:
        font = pygame.font.SysFont(GAME_FONT, 40, bold=True)
        text = font.render('GAME OVER', True, (255, 0, 0))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, rect)
    pygame.display.flip()
    clock.tick(30)  # Limitar a 30 FPS


pygame.quit()


# TODO: Mostrar puntuación(OK), Nivel del juego y piezas siguientes(OK)
# TODO: Definir puntuación según líneas eliminadas o Tetris(4 líneas a la vez) --> OK
# TODO: Implementar lógica de fin de juego --> OK
# TODO: Implementar lógica de reinicio del juego --> OK
# TODO: Mejorar la interfaz gráfica y añadir sonidos
# TODO: Desacoplar lógica de control de movimiento de piezas y lógica de dibujo
# TODO: Añadir sistema de niveles que aumente la velocidad de caída de las piezas con el tiempo o con la puntuación

# TODO: BUGFIX: NO TODAS LAS PIEZAS APARECEN CENTRADAS AL INICIO
# TODO: BUGFIX: NO TODAS LAS PIEZAS DESCIENDEN LINEA A LINEA