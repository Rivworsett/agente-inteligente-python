# ==========================================
# AGENTE INTELIGENTE CON HEURÍSTICA
# ==========================================

# Tablero:
# 0 = espacio libre
# 1 = obstáculo
# A = agente
# G = objetivo

tablero = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

inicio = (0, 0)
objetivo = (5, 5)

# Movimientos posibles:
# arriba, abajo, izquierda y derecha
movimientos = [
    (-1, 0),  # arriba
    (1, 0),   # abajo
    (0, -1),  # izquierda
    (0, 1)    # derecha
]


# ------------------------------------------
# FUNCIÓN HEURÍSTICA
# ------------------------------------------

def heuristica(posicion, objetivo):
    """
    Calcula la distancia Manhattan entre
    la posición actual y el objetivo.
    """
    x1, y1 = posicion
    x2, y2 = objetivo

    return abs(x1 - x2) + abs(y1 - y2)


# ------------------------------------------
# COMPROBAR SI UNA POSICIÓN ES VÁLIDA
# ------------------------------------------

def posicion_valida(posicion):
    x, y = posicion

    # Comprobar límites del tablero
    if x < 0 or x >= len(tablero):
        return False

    if y < 0 or y >= len(tablero[0]):
        return False

    # Comprobar obstáculos
    if tablero[x][y] == 1:
        return False

    return True


# ------------------------------------------
# MOSTRAR TABLERO
# ------------------------------------------

def mostrar_tablero(posicion_agente):
    for i in range(len(tablero)):
        fila = ""

        for j in range(len(tablero[0])):

            if (i, j) == posicion_agente:
                fila += " A "

            elif (i, j) == objetivo:
                fila += " G "

            elif tablero[i][j] == 1:
                fila += " # "

            else:
                fila += " . "

        print(fila)

    print()


# ------------------------------------------
# AGENTE INTELIGENTE
# ------------------------------------------

def agente_inteligente():

    posicion = inicio
    camino = [posicion]

    print("===================================")
    print("     AGENTE INTELIGENTE")
    print("===================================")

    print("\nTablero inicial:")
    mostrar_tablero(posicion)

    while posicion != objetivo:

        opciones = []

        # Analizar movimientos posibles
        for movimiento in movimientos:

            nueva_posicion = (
                posicion[0] + movimiento[0],
                posicion[1] + movimiento[1]
            )

            if posicion_valida(nueva_posicion):

                # Calcular valor heurístico
                h = heuristica(nueva_posicion, objetivo)

                opciones.append((h, nueva_posicion))

        # Si no existen movimientos disponibles
        if not opciones:
            print("El agente no puede continuar.")
            return

        # Ordenar opciones por valor heurístico
        opciones.sort(key=lambda x: x[0])

        # Seleccionar la mejor opción
        mejor_heuristica, mejor_posicion = opciones[0]

        print(
            f"Agente en {posicion} -> "
            f"se mueve a {mejor_posicion} "
            f"(h = {mejor_heuristica})"
        )

        posicion = mejor_posicion
        camino.append(posicion)

        mostrar_tablero(posicion)

    print("===================================")
    print("¡OBJETIVO ALCANZADO!")
    print("===================================")

    print("\nCamino recorrido:")
    print(camino)

    print(f"\nNúmero de movimientos: {len(camino) - 1}")


# ------------------------------------------
# EJECUTAR PROGRAMA
# ------------------------------------------

if __name__ == "__main__":
    agente_inteligente()
