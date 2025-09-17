import pygame

from config import CELL_SIZE, BOARD_WIDTH, GAME_FONT, GAME_FONT_SIZE
from config import SCREEN_WIDTH, SCREEN_HEIGHT

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