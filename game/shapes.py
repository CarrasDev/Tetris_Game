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
    ]
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
    'T': T_SHAPE

    # TODO: Añadir el resto de piezas con sus formas
}

# Colores asociados a cada forma
# Estos colores se representan como tuplas RGB
COLORS = {
    'T': (128, 0, 128)  # Púrpura

    # TODO: Añadir el resto de colores para las piezas
}