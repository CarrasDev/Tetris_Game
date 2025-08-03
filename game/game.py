import random
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
        if not self.is_valid_position():
            self.current_piece.y -= 1
            return False
        return True
    
    def drop_piece(self):
        while self.can_move_down():
            pass
        self.board.add_piece(self.current_piece)
        lines_cleared = self.board.clear_lines()
        self.score += lines_cleared * 100  # TODO: Pendiente de definir sistema de puntuación

        # Cambiar a la siguiente pieza
        self.current_piece = self.next_piece
        self.next_piece = self.get_random_piece()
        if not self.is_valid_position():
            self.game_over = True
            print("Game Over!")     # TODO: Implement game over logic