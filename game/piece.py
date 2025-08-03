# Representamos la forma de cada pieza del juego
# Manejar su posición en el tablero
# Permitir rotaciones
# Asignar colores


class Piece:
    def __init__(self, x, y, shape, color):
        self.x = x  # Posición horizontal en el tablero
        self.y = y  # Posición vertical en el tablero
        self.shape = shape  # Forma de la pieza
        self.color = color  # Color de la pieza
        self.rotation = 0   # Estado de rotación de la pieza

    def get_current_shape(self):
        return self.shape[self.rotation]    # Obtener la forma actual de la pieza según su rotación

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)   # Rotar la pieza de forma cíclica
    
    def rotate_left(self):
        self.rotation = (self.rotation - 1) % len(self.shape)   # Rotar la pieza hacia la izquierda de forma cíclica
    
    def get_cells(self):
        cells =  []
        current_shape = self.get_current_shape()
        for y, row in enumerate(current_shape):
            for x, cell in enumerate(row):
                if cell:
                    cells.append((self.x + x, self.y + y))
        return cells   
    
    
    # TODO: Proseguir con la implementación de metodos de las piezas