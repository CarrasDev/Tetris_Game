

class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]  # color (0, 0, 0) for empty cells

    def add_piece(self, piece):
        for cell in piece.get_cells():
            x, y = cell
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = piece.color

    def clear_lines(self):
        lines_to_clear = []
        for y in range(self.height):
            if all(self.grid[y][x] != (0, 0, 0) for x in range(self.width)):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [(0, 0, 0) for _ in range(self.width)])
        
        return len(lines_to_clear)  # Return the number of lines cleared
    
    
    # TODO: Implementar métodos para manejar el tablero, como agregar piezas, eliminar líneas completas, etc.