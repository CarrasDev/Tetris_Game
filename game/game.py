import random

from config import FALL_ACCELERATION, LEVEL_UP_LINES, SCORE_PER_LINE, TETRIS_BONUS

from.board import Board
from.piece import Piece
from.shapes import SHAPES, COLORS

class Game:
    def __init__(self, width=10, height=20):
        self.board = Board(width, height)
        self.current_piece = self.get_random_piece()
        self.next_piece = self.get_random_piece()
        self.score = 0
        self.game_over = False
        self.tetris_streak = 0
        self.level = 0
        self.lines_cleared_total = 0

    def get_random_piece(self):
        shape_key = random.choice(list(SHAPES.keys()))
        shape = SHAPES[shape_key]
        color = COLORS[shape_key]
        x = (self.board.width - len(shape[0][0])) // 2
        y = 0
        return Piece(x, y, shape, color)
    
    def rotate_piece(self):
        self.current_piece.rotate()
        if not self.is_valid_position():
            self.current_piece.rotate_left()
    
    def is_valid_position(self):
        return self.board.is_valid_position(self.current_piece)
    
    def move_piece(self, dx, dy):
        self.current_piece.x += dx
        self.current_piece.y += dy
        if not self.is_valid_position():
            self.current_piece.x -= dx
            self.current_piece.y -= dy
    
    def can_move_down(self):
        self.current_piece.y += 1
        valid = self.is_valid_position()
        self.current_piece.y -= 1   # Restituye la posición original
        return valid
    
    def drop_piece(self):
        while self.can_move_down():
            self.move_piece(0, 1)
        self.board.add_piece(self.current_piece)
        lines_cleared = self.board.clear_lines()
        self._update_score(lines_cleared)

        # Cambiar a la siguiente pieza
        self.current_piece = self.next_piece
        self.next_piece = self.get_random_piece()
        if not self.is_valid_position():
            self.game_over = True
            
    def _update_score(self, lines_cleared):
        self.lines_cleared_total += lines_cleared
        self.level = self.lines_cleared_total // LEVEL_UP_LINES
        
        # Actualizar puntuación
        if lines_cleared == 1:
            self.score += SCORE_PER_LINE
            self.tetris_streak = 0
        elif lines_cleared == 2:
            self.score += (SCORE_PER_LINE * 3)
            self.tetris_streak = 0
        elif lines_cleared == 3:
            self.score += (SCORE_PER_LINE * 5)
            self.tetris_streak = 0
        elif lines_cleared == 4:
            if self.tetris_streak == 0:
                self.score += (SCORE_PER_LINE * 12)
            else:
                self.score += (SCORE_PER_LINE * 12) + (self.tetris_streak * TETRIS_BONUS)
            self.tetris_streak += 1
        else:
            self.tetris_streak = 0
    
    def reset(self):
        self.board.reset()
        self.current_piece = self.get_random_piece()
        self.next_piece = self.get_random_piece()
        self.score = 0
        self.game_over = False
        self.tetris_streak = 0
        self.level = 0
        self.lines_cleared_total = 0

    def get_fall_speed(self, base_speed, min_speed=100):
        speed = int(base_speed * (FALL_ACCELERATION ** self.level))
        return max(speed, min_speed)
    
    def get_remaining_lines(self):
        return LEVEL_UP_LINES - (self.lines_cleared_total % LEVEL_UP_LINES)