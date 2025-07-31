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


    
    # TODO: Proseguir con la implementación de metodos de las piezas