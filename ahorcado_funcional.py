import random

# =============================================================
# AHORCADO - Versión funcional
# =============================================================

def cargar_palabras():
    """
    Carga y retorna una lista de palabras para el juego.
    
    Returns:
        list: Lista de palabras para adivinar.
    """
    return [
        "python", "programacion", "computadora", "algoritmo", 
        "variable", "funcion", "diccionario", "lista", 
        "cadena", "entero", "flotante", "booleano",
        "juego", "ahorcado", "desarrollo", "software"
    ]


def seleccionar_palabra(palabras):
    """
    Selecciona una palabra aleatoria de la lista.
    
    Args:
        palabras (list): Lista de palabras disponibles.
    
    Returns:
        str: Palabra seleccionada al azar.
    """
    return random.choice(palabras)


def inicializar_tablero(palabra):
    """
    Inicializa el tablero con guiones bajos para cada letra.
    
    Args:
        palabra (str): Palabra a adivinar.
    
    Returns:
        list: Tablero inicial con guiones.
    """
    return ["_" for _ in palabra]


def mostrar_estado(tablero, letras_incorrectas, intentos_restantes):
    """
    Muestra el estado actual del juego.
    
    Args:
        tablero (list): Estado actual del tablero.
        letras_incorrectas (list): Letras incorrectas ya intentadas.
        intentos_restantes (int): Número de intentos restantes.
    """
    print("\n" + "="*50)
    print(f"Palabra: {' '.join(tablero)}")
    print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
    print(f"Intentos restantes: {intentos_restantes}")
    print("="*50)


def dibujar_ahorcado(intentos):
    """
    Dibuja el estado del ahorcado según los intentos fallidos.
    
    Args:
        intentos (int): Número de intentos fallidos.
    """
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(estados[intentos])


def obtener_letra_valida(letras_intentadas):
    """
    Solicita y valida una letra del jugador.
    
    Args:
        letras_intentadas (list): Letras ya intentadas.
    
    Returns:
        str: Letra válida ingresada por el jugador.
    """
    while True:
        letra = input("\nIngresa una letra: ").lower()
        
        if len(letra) != 1:
            print("Por favor ingresa solo una letra.")
        elif not letra.isalpha():
            print("Por favor ingresa una letra válida.")
        elif letra in letras_intentadas:
            print("Ya has intentado con esa letra.")
        else:
            return letra


def procesar_intento(letra, palabra, tablero, letras_incorrectas):
    """
    Procesa el intento del jugador y actualiza el estado del juego.
    
    Args:
        letra (str): Letra ingresada por el jugador.
        palabra (str): Palabra a adivinar.
        tablero (list): Estado actual del tablero.
        letras_incorrectas (list): Lista de letras incorrectas.
    
    Returns:
        tuple: (tablero_actualizado, letras_incorrectas_actualizadas, acierto)
    """
    acierto = False
    
    if letra in palabra:
        # Actualizar tablero con la letra correcta
        for i, char in enumerate(palabra):
            if char == letra:
                tablero[i] = letra
        acierto = True
    else:
        # Agregar a letras incorrectas
        letras_incorrectas.append(letra)
    
    return tablero, letras_incorrectas, acierto


def verificar_victoria(tablero):
    """
    Verifica si el jugador ha adivinado toda la palabra.
    
    Args:
        tablero (list): Estado actual del tablero.
    
    Returns:
        bool: True si ha ganado, False en caso contrario.
    """
    return "_" not in tablero


def verificar_derrota(intentos_restantes):
    """
    Verifica si el jugador ha perdido.
    
    Args:
        intentos_restantes (int): Intentos restantes.
    
    Returns:
        bool: True si ha perdido, False en caso contrario.
    """
    return intentos_restantes <= 0


def jugar_ahorcado():
    """
    Función principal que controla el flujo del juego Ahorcado.
    """
    palabras = cargar_palabras()
    palabra = seleccionar_palabra(palabras)
    tablero = inicializar_tablero(palabra)
    
    letras_intentadas = []
    letras_incorrectas = []
    intentos_maximos = 6
    intentos_restantes = intentos_maximos
    juego_activo = True
    
    print("¡Bienvenido al Ahorcado!")
    print("Adivina la palabra antes de que se complete el ahorcado.")
    
    while juego_activo:
        mostrar_estado(tablero, letras_incorrectas, intentos_restantes)
        dibujar_ahorcado(len(letras_incorrectas))
        
        # Obtener letra válida
        letra = obtener_letra_valida(letras_intentadas)
        letras_intentadas.append(letra)
        
        # Procesar intento
        tablero, letras_incorrectas, acierto = procesar_intento(
            letra, palabra, tablero, letras_incorrectas
        )
        
        if not acierto:
            intentos_restantes -= 1
            print(f"¡Incorrecto! La letra '{letra}' no está en la palabra.")
        else:
            print(f"¡Correcto! La letra '{letra}' está en la palabra.")
        
        # Verificar condiciones de término
        if verificar_victoria(tablero):
            mostrar_estado(tablero, letras_incorrectas, intentos_restantes)
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            juego_activo = False
        elif verificar_derrota(intentos_restantes):
            mostrar_estado(tablero, letras_incorrectas, intentos_restantes)
            dibujar_ahorcado(len(letras_incorrectas))
            print(f"¡Game Over! La palabra era: {palabra}")
            juego_activo = False
    
    # Preguntar si desea jugar otra vez
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez == "s":
        jugar_ahorcado()
    else:
        print("¡Gracias por jugar!", "¡adios!")


# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()