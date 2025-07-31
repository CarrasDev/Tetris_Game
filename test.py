from game import Piece, Board, Game, SHAPES, COLORS


# Prueba de movimiento y rotación de una pieza
# Verifica que las claves 'T' existan en SHAPES y COLORS antes de usarlas
if 'T' in SHAPES and 'T' in COLORS:
    piece = Piece(3, 0, SHAPES['T'], COLORS['T'])
    print("Forma actual:")
    for row in piece.get_current_shape():
        print(row)

    piece.rotate()
    print("Forma despues de rotar:")
    for row in piece.get_current_shape():
        print(row)
else:
    print("Error: La clave 'T' no existe en SHAPES o COLORS.")