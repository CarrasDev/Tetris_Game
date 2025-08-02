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
        for cell in self.current_piece.get_cells():
            x, y = cell
            if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
                return False
            if self.board.grid[y][x] != (0, 0, 0):
                return False
        return True
    
    def move_piece(self, dx, dy):
        self.current_piece.x += dx
        self.current_piece.y += dy
        if not self.is_valid_position():
            self.current_piece.x -= dx
            self.current_piece.y -= dy
    
    