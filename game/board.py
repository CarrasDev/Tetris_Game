

class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]  # color (0, 0, 0) for empty cells
                                                                   

    # TODO: Implementar métodos para manejar el tablero, como agregar piezas, eliminar líneas completas, etc.