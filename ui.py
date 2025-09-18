import pygame

from config import CELL_SIZE, BOARD_WIDTH
from config import GAME_FONT, GAME_FONT_SIZE
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_board(screen, game):
    screen.fill((0, 0, 0))

    # Dibujar cuadrícula
    grid_color = (40, 40, 40)  # Gris oscuro
    for x in range(game.board.width + 1):
        pygame.draw.line(
            screen,
            grid_color,
            (x * CELL_SIZE, 0),
            (x * CELL_SIZE, game.board.height * CELL_SIZE),
            1
        )
    for y in range(game.board.height + 1):
        pygame.draw.line(
            screen,
            grid_color,
            (0, y * CELL_SIZE),
            (game.board.width * CELL_SIZE, y * CELL_SIZE),
            1
        )

    # Dibujar piezas en el tablero
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
    # Linea divisoria
    pygame.draw.line(
        screen,
        (80, 80, 80),
        (BOARD_WIDTH * CELL_SIZE, 0),
        (BOARD_WIDTH * CELL_SIZE, SCREEN_HEIGHT),
        2
    )

    # Next piece
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

    # Score
    score_label_font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, bold=True)
    score_label_text = score_label_font.render('Score:', True, (255, 255, 0))
    score_label_x = BOARD_WIDTH * CELL_SIZE + 10
    score_label_y = 180
    screen.blit(score_label_text, (score_label_x, score_label_y))
    
    score_font = pygame.font.SysFont(GAME_FONT, 28, bold=True)
    score_str = f"{game.score:,}".replace(',', '.')
    score_text = score_font.render(score_str, True, (255, 255, 255))
    score_x = SCREEN_WIDTH - score_text.get_width() - 10
    score_y = score_label_y + 30
    screen.blit(score_text, (score_x, score_y))

    # Level
    level_label_font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, bold=True)
    level_label_text = level_label_font.render('Level:', True, (255, 255, 0))
    level_label_x = BOARD_WIDTH * CELL_SIZE + 10
    level_label_y = 250
    screen.blit(level_label_text, (level_label_x, level_label_y))
    
    level_font = pygame.font.SysFont(GAME_FONT, 28, bold=True)
    level_str = f"{game.level}"
    level_text = level_font.render(level_str, True, (255, 255, 255))
    level_x = SCREEN_WIDTH - level_text.get_width() - 10
    level_y = level_label_y + 30
    screen.blit(level_text, (level_x, level_y))

    # Lines Cleared
    lines_label_font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, bold=True)
    lines_label_text = lines_label_font.render('Lines:', True, (255, 255, 0))
    lines_label_x = BOARD_WIDTH * CELL_SIZE + 10
    lines_label_y = 320
    screen.blit(lines_label_text, (lines_label_x, lines_label_y))

    lines_font = pygame.font.SysFont(GAME_FONT, 28, bold=True)
    lines_str = f"{game.lines_cleared_total}"
    lines_text = lines_font.render(lines_str, True, (255, 255, 255))
    lines_x = SCREEN_WIDTH - lines_text.get_width() - 10
    lines_y = lines_label_y + 30
    screen.blit(lines_text, (lines_x, lines_y))


def draw_pause(screen):
    font = pygame.font.SysFont(GAME_FONT, 20, bold=True)
    text = font.render('PAUSE', True, (255, 255, 255))
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, rect)


def draw_game_over(screen):
    font = pygame.font.SysFont(GAME_FONT, 40, bold=True)
    text = font.render('GAME OVER', True, (255, 0, 0))
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, rect)