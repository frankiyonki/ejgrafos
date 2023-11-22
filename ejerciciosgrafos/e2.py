def buscar_entrada(mapa):
    """
    Esta función busca la entrada del laberinto.
    :param mapa: El laberinto a recorrer.
    :return: La posición de la entrada (fila, columna) o "NO" si no se encuentra.
    """

    columnas = len(mapa)
    filas = len(mapa[0])

    for i in range(columnas):
        for j in range(filas):
            if mapa[i][j] == "A":
                return buscar_salida(mapa, i, j, filas, columnas, 0, None)

    return "NO"


def buscar_salida(mapa, i, j, filas, columnas, contador, palabra):
    """
    Esta función busca la salida del laberinto desde la posición dada.
    :param mapa: El laberinto a recorrer.
    :param i: La fila de la posición actual.
    :param j: La columna de la posición actual.
    :param filas: El número total de filas del mapa.
    :param columnas: El número total de columnas del mapa.
    :param contador: El contador de pasos realizados.
    :param palabra: La dirección de la última acción (R, L, U, D).
    """

    salida = False
    if palabra == "R":
        lista_movimientos.append("R")
    elif palabra == "L":
        lista_movimientos.append("L")
    elif palabra == "U":
        lista_movimientos.append("U")
    elif palabra == "D":
        lista_movimientos.append("D")

    while True:
        if i < 0 or i >= columnas or j < 0 or j >= filas or mapa[i][j] == '#':
            if lista_movimientos:
                lista_movimientos.pop()
            break

        if mapa[i][j] == "B":
            salida = True
            print("SI", "contador:", contador, "movimientos:", lista_movimientos)
            break

        mapa[i][j] = '#'

        buscar_salida(mapa, i + 1, j, filas, columnas, contador + 1, "D")
        buscar_salida(mapa, i - 1, j, filas, columnas, contador + 1, "U")
        buscar_salida(mapa, i, j + 1, filas, columnas, contador + 1, "R")
        buscar_salida(mapa, i, j - 1, filas, columnas, contador + 1, "L")
        break

    if salida == False:
        return "NO"


lista_movimientos = []
mapa2 = [
    list("########"),
    list("#.A#...#"),
    list("#.##.#B#"),
    list("#......#"),
    list("########")
]

buscar_entrada(mapa2)
