# =============================================================
# TIC TAC TOE - Versión funcional
# =============================================================

def inicializar_tablero():
    """
    Inicializa un tablero vacío de 3x3.
    
    Returns:
        list: Tablero con 9 posiciones vacías.
    """
    return [" " for _ in range(9)]


def imprimir_tablero(tablero):
    """
    Muestra el tablero actual en la consola.
    
    Args:
        tablero (list): Estado actual del tablero.
    """
    print("\n   |   |   ")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("   |   |   \n")


def verificar_ganador(tablero, jugador):
    """
    Verifica si el jugador actual ha ganado.
    
    Args:
        tablero (list): Estado actual del tablero.
        jugador (str): Símbolo del jugador ('X' o 'O').
    
    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
    """
    # Combinaciones ganadoras
    lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for linea in lineas_ganadoras:
        if all(tablero[pos] == jugador for pos in linea):
            return True
    return False


def verificar_empate(tablero):
    """
    Verifica si el juego ha terminado en empate.
    
    Args:
        tablero (list): Estado actual del tablero.
    
    Returns:
        bool: True si hay empate, False en caso contrario.
    """
    return " " not in tablero


def obtener_movimiento_valido(tablero, jugador):
    """
    Solicita y valida el movimiento del jugador.
    
    Args:
        tablero (list): Estado actual del tablero.
        jugador (str): Símbolo del jugador actual.
    
    Returns:
        int: Posición válida seleccionada por el jugador.
    """
    while True:
        try:
            movimiento = int(input(f"Jugador {jugador}, elige una posición (1-9): ")) - 1
            if 0 <= movimiento <= 8 and tablero[movimiento] == " ":
                return movimiento
            else:
                print("Posición inválida o ocupada. Intenta nuevamente.")
        except ValueError:
            print("Por favor ingresa un número válido.")


def cambiar_jugador(jugador_actual):
    """
    Alterna entre los jugadores X y O.
    
    Args:
        jugador_actual (str): Jugador actual ('X' o 'O').
    
    Returns:
        str: Siguiente jugador.
    """
    return "O" if jugador_actual == "X" else "X"


def jugar_tictactoe():
    """
    Función principal que controla el flujo del juego Tic Tac Toe.
    """
    tablero = inicializar_tablero()
    jugador_actual = "X"
    juego_activo = True
    
    print("¡Bienvenido a Tic Tac Toe!")
    print("Posiciones del tablero:")
    print("\n 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("\n")
    
    while juego_activo:
        imprimir_tablero(tablero)
        
        # Obtener movimiento válido
        posicion = obtener_movimiento_valido(tablero, jugador_actual)
        tablero[posicion] = jugador_actual
        
        # Verificar si hay ganador
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Felicidades! Jugador {jugador_actual} ha ganado!")
            juego_activo = False
        # Verificar empate
        elif verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Empate! El juego ha terminado sin ganador.")
            juego_activo = False
        else:
            # Cambiar jugador
            jugador_actual = cambiar_jugador(jugador_actual)
    
    # Preguntar si desea jugar otra vez
    jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez == "s":
        jugar_tictactoe()
    else:
        print("¡Gracias por jugar!")


# Ejecutar el juego
if __name__ == "__main__":
    jugar_tictactoe()