# 1. Crear un diccionario simple
diccionario = {
    "nombre": "Juan Pérez",
    "edad": 25,
    "ciudad": "California",
    "profesion": "Mecanico",
    "hobbies": ["leer", "correr", "cocinar" "artes maciales"],
    "email": "juan.perez@gmail.com"
}

# 2. Menú interactivo
def mostrar_menu():
    print("\n" + "="*40)
    print("          DICCIONARIO INTERACTIVO")
    print("="*40)
    print("Claves disponibles:")
    
    # Mostrar las claves numeradas
    claves = list(diccionario.keys())
    for i, clave in enumerate(claves, 1):
        print(f"{i}. {clave}")
    
    print(f"{len(claves) + 1}. Salir")
    print("="*40)

# Programa principal
while True:
    mostrar_menu()
    
    try:
        opcion = int(input("Selecciona una opción (número): "))
        
        claves = list(diccionario.keys())
        
        if 1 <= opcion <= len(claves):
            clave_seleccionada = claves[opcion - 1]
            valor = diccionario[clave_seleccionada]
            
            print(f"\n📋 Clave: {clave_seleccionada}")
            print(f"📝 Valor: {valor}")
            print(f"📊 Tipo de dato: {type(valor).__name__}")
            
        elif opcion == len(claves) + 1:
            print("SALIENDO DEL SISTEMA 👋")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
            
    except ValueError:
        print("❌ Error: Debes ingresar un número.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    # Pausa antes de continuar
    input("\nPresiona Enter para continuar...")
