import random

# =============================================================
# TIC TAC TOE- Versión funcional con múltiples modos
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


def mostrar_posiciones():
    """
    Muestra el mapa de posiciones del tablero.
    """
    print("\nPosiciones del tablero:")
    print("\n 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("\n")


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
    Solicita y valida el movimiento del jugador humano.
    
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


def obtener_movimiento_maquina_facil(tablero):
    """
    La máquina elige una posición aleatoria disponible (modo fácil).
    
    Args:
        tablero (list): Estado actual del tablero.
    
    Returns:
        int: Posición seleccionada por la máquina.
    """
    posiciones_disponibles = [i for i, pos in enumerate(tablero) if pos == " "]
    return random.choice(posiciones_disponibles)


def obtener_movimiento_maquina_dificil(tablero, jugador_maquina):
    """
    La máquina usa estrategia básica (modo difícil).
    Prioriza: ganar > bloquear > centro > esquinas > lados.
    
    Args:
        tablero (list): Estado actual del tablero.
        jugador_maquina (str): Símbolo de la máquina ('X' o 'O').
    
    Returns:
        int: Posición seleccionada por la máquina.
    """
    jugador_oponente = "O" if jugador_maquina == "X" else "X"
    
    # 1. Buscar posición para ganar
    for i in range(9):
        if tablero[i] == " ":
            tablero_temp = tablero.copy()
            tablero_temp[i] = jugador_maquina
            if verificar_ganador(tablero_temp, jugador_maquina):
                return i
    
    # 2. Buscar posición para bloquear al oponente
    for i in range(9):
        if tablero[i] == " ":
            tablero_temp = tablero.copy()
            tablero_temp[i] = jugador_oponente
            if verificar_ganador(tablero_temp, jugador_oponente):
                return i
    
    # 3. Tomar el centro si está disponible
    if tablero[4] == " ":
        return 4
    
    # 4. Tomar esquinas disponibles
    esquinas = [0, 2, 6, 8]
    esquinas_disponibles = [e for e in esquinas if tablero[e] == " "]
    if esquinas_disponibles:
        return random.choice(esquinas_disponibles)
    
    # 5. Tomar lados disponibles
    lados = [1, 3, 5, 7]
    lados_disponibles = [l for l in lados if tablero[l] == " "]
    if lados_disponibles:
        return random.choice(lados_disponibles)
    
    
    return obtener_movimiento_maquina_facil(tablero)


def cambiar_jugador(jugador_actual):
    """
    Alterna entre los jugadores X y O.
    
    Args:
        jugador_actual (str): Jugador actual ('X' o 'O').
    
    Returns:
        str: Siguiente jugador.
    """
    return "O" if jugador_actual == "X" else "X"


def seleccionar_modo_juego():
    """
    Permite al usuario seleccionar el modo de juego.
    
    Returns:
        str: Modo seleccionado ('1', '2', o '3').
    """
    print("\n=== MODOS DE JUEGO ===")
    print("1. Jugador vs Jugador")
    print("2. Jugador vs Máquina (Fácil)")
    print("3. Jugador vs Máquina (Difícil)")
    
    while True:
        modo = input("Selecciona el modo de juego (1-3): ").strip()
        if modo in ["1", "2", "3"]:
            return modo
        else:
            print("Por favor selecciona una opción válida (1, 2 o 3).")


def jugar_turno(tablero, jugador_actual, modo_juego):
    """
    Ejecuta un turno completo según el modo de juego.
    
    Args:
        tablero (list): Estado actual del tablero.
        jugador_actual (str): Jugador del turno actual.
        modo_juego (str): Modo de juego seleccionado.
    
    Returns:
        list: Tablero actualizado después del movimiento.
    """
    imprimir_tablero(tablero)
    
    if modo_juego == "1":  # Jugador vs Jugador
        posicion = obtener_movimiento_valido(tablero, jugador_actual)
    
    elif modo_juego == "2":  # Jugador vs Máquina (Fácil)
        if jugador_actual == "X":  # Jugador humano
            posicion = obtener_movimiento_valido(tablero, jugador_actual)
        else:  # Máquina
            print("Turno de la máquina (fácil)...")
            posicion = obtener_movimiento_maquina_facil(tablero)
    
    else:  # Jugador vs Máquina (Difícil)
        if jugador_actual == "X":  # Jugador humano
            posicion = obtener_movimiento_valido(tablero, jugador_actual)
        else:  # Máquina
            print("Turno de la máquina (difícil)...")
            posicion = obtener_movimiento_maquina_dificil(tablero, jugador_actual)
    
    # Aplicar el movimiento
    tablero[posicion] = jugador_actual
    return tablero


def mostrar_resultado(tablero, jugador_actual, modo_juego):
    """
    Muestra el resultado final del juego.
    
    Args:
        tablero (list): Estado final del tablero.
        jugador_actual (str): Último jugador en mover.
        modo_juego (str): Modo de juego seleccionado.
    """
    imprimir_tablero(tablero)
    
    if verificar_ganador(tablero, jugador_actual):
        if modo_juego == "1":
            print(f"¡Felicidades! Jugador {jugador_actual} ha ganado!")
        else:
            if jugador_actual == "X":
                print("¡Felicidades! Has ganado contra la máquina!","¡eres un genio en potencia!")
            else:
                print("¡La máquina ha ganado! Mejor suerte la próxima vez jaja.")
    else:
        print("¡Empate! El juego ha terminado sin ganador:(.")


def jugar_tictactoe():
    """
    Función principal que controla el flujo completo del juego Tic Tac Toe.
    """
    # Configuración inicial
    print("\n=== BIENVENIDO A TIC TAC TOE===")
    mostrar_posiciones()
    
    # Selección de modo de juego
    modo_juego = seleccionar_modo_juego()
    
    # Inicializar juego
    tablero = inicializar_tablero()
    jugador_actual = "X"
    juego_activo = True
    
    # Bucle principal del juego
    while juego_activo:
        # Ejecutar turno
        tablero = jugar_turno(tablero, jugador_actual, modo_juego)
        
        # Verificar condiciones de término
        if verificar_ganador(tablero, jugador_actual):
            mostrar_resultado(tablero, jugador_actual, modo_juego)
            juego_activo = False
        elif verificar_empate(tablero):
            mostrar_resultado(tablero, jugador_actual, modo_juego)
            juego_activo = False
        else:
            # Cambiar jugador
            jugador_actual = cambiar_jugador(jugador_actual)
    
    # Preguntar si desea jugar otra vez
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez == "s":
        jugar_tictactoe()
    else:
        print("¡Gracias por jugar!","saliendo del sistema")


# Función para ejecutar directamente
if __name__ == "__main__":
    jugar_tictactoe()