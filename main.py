import pygame
import ui

from game import Game
from config import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT, GAME_FONT
from config import FALL_SPEED, MOVE_DELAY


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Game")

game = Game(BOARD_WIDTH, BOARD_HEIGHT)
clock = pygame.time.Clock()
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
        if keys[pygame.K_LEFT] and current_time - last_fall_time > MOVE_DELAY:
            game.move_piece(-1, 0)
            last_fall_time = current_time
        if keys[pygame.K_RIGHT] and current_time - last_fall_time > MOVE_DELAY:
            game.move_piece(1, 0)
            last_fall_time = current_time
        if keys[pygame.K_DOWN] and current_time - last_fall_time > MOVE_DELAY:
            game.move_piece(0, 1)
            last_fall_time = current_time
                      
        # Lógica de caída de piezas
        current_time = pygame.time.get_ticks()
        if current_time - last_fall_time > FALL_SPEED:
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