# Representamos la forma de cada pieza del juego
# Manejar su posición en el tablero
# Permitir rotaciones
# Asignar colores

import random
class Piece:
    def __init__(self, shape, color):
        self.shape = shape  # Forma de la pieza (lista de coordenadas)
        self.color = color  # Color de la pieza
        self.position = (0, 0)  # Posición inicial en el tablero

    def rotate(self):
        """Rota la pieza 90 grados en sentido horario."""
        self.shape = [(-y, x) for x, y in self.shape]

    def move(self, dx, dy):
        """Mueve la pieza a una nueva posición."""
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def get_coordinates(self):
        """Devuelve las coordenadas actuales de la pieza en el tablero."""
        return [(x + self.position[0], y + self.position[1]) for x, y in self.shape]
    
