import pygame
import ui

from game import Game
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT
from config import FALL_SPEED, MOVE_DELAY


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Game")

game = Game(BOARD_WIDTH, BOARD_HEIGHT)
clock = pygame.time.Clock()

fall_time = pygame.time.get_ticks()
move_time = pygame.time.get_ticks()

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
        
        if keys[pygame.K_LEFT] and current_time - move_time > MOVE_DELAY:
            game.move_piece(-1, 0)
            move_time = current_time
        if keys[pygame.K_RIGHT] and current_time - move_time > MOVE_DELAY:
            game.move_piece(1, 0)
            move_time = current_time
        if keys[pygame.K_DOWN] and current_time - move_time > MOVE_DELAY:
            game.move_piece(0, 1)
            move_time = current_time
                      
        # Caída automática
        if current_time - fall_time > FALL_SPEED:
            if game.can_move_down():
                game.move_piece(0, 1)
            else:
                game.drop_piece()
            fall_time = current_time
    

    # Dibujar el estado actual del juego
    ui.draw_board(screen, game)
    ui.draw_side_panel(screen, game)
    if paused:
        ui.draw_pause(screen)
    if game.game_over:
        ui.draw_game_over(screen)
    pygame.display.flip()
    clock.tick(30)  # Limitar a 30 FPS


pygame.quit()


# TODO: Mostrar puntuación y piezas siguientes --> OK
# TODO: Definir puntuación según líneas eliminadas o Tetris(4 líneas a la vez) --> OK
# TODO: Implementar lógica de fin de juego --> OK
# TODO: Implementar lógica de reinicio del juego --> OK
# TODO: Desacoplar lógica de control de movimiento de piezas y lógica de dibujo --> OK

# TODO: Mejorar la interfaz gráfica y añadir sonidos
# TODO: Añadir sistema de niveles que aumente la velocidad de caída de las piezas cada 10 líneas eliminadas

# TODO: BUGFIX: NO TODAS LAS PIEZAS APARECEN CENTRADAS AL INICIO