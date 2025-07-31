# Representamos la forma de cada pieza del juego
# El nombre de cada pieza
# Los colores de cada una de las piezas


# Definimos las formas de las piezas del juego
T_SHAPE = [
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
]
# TODO: Añadir más formas de piezas como I, O, L, J, S, Z


# Nombres de las formas de las piezas
SHAPES = {
    'T': T_SHAPE,
    'Z': Z_SHAPE,  # TODO: Definir Z_SHAPE
    'S': S_SHAPE,  # TODO: Definir S_SHAPE
    'I': I_SHAPE,  # TODO: Definir I_SHAPE
    'O': O_SHAPE,  # TODO: Definir O_SHAPE
    'J': J_SHAPE,  # TODO: Definir J_SHAPE
    'L': L_SHAPE   # TODO: Definir L_SHAPE
}

# Colores asociados a cada forma
# Estos colores se representan como tuplas RGB
COLORS = {
    'T': (128, 0, 128),  # Púrpura
    'Z': (255, 0, 0),  # Rojo
    'S': (0, 255, 0),  # Verde
    'I': (0, 255, 255),  # Cian
    'O': (255, 255, 0),  # Amarillo
    'J': (0, 0, 255),  # Azul
    'L': (255, 165, 0)  # Naranja
}