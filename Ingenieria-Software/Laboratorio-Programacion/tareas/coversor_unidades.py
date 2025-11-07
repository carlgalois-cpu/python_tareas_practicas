# Conversor de Unidades Simple

print("=== CALCULAR UNIDADES ===")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Temperatura: Celsius → Fahrenheit")
    print("2. Temperatura: Fahrenheit → Celsius")
    print("3. Longitud: Metros → Centímetros")
    print("4. Longitud: Centímetros → Metros")
    print("5. Masa: Kilogramos → Gramos")
    print("6. Masa: Gramos → Kilogramos")
    print("7. Salir")
    
    opcion = input("Seleccione una opción (1-7): ")
    
    if opcion == "1":
        # Celsius a Fahrenheit
        try:
            celsius = float(input("Ingrese los grados Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        except:
            print("Error: Ingrese un valor numérico válido")
    
    elif opcion == "2":
        # Fahrenheit a Celsius
        try:
            fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        except:
            print("Error: Ingrese un valor numérico válido")
    
    elif opcion == "3":
        # Metros a Centímetros
        try:
            metros = float(input("Ingrese la longitud en metros: "))
            centimetros = metros * 100
            print(f"{metros} m = {centimetros} cm")
        except:
            print("Error: Ingrese un valor numérico válido")
    
    elif opcion == "4":
        # Centímetros a Metros
        try:
            centimetros = float(input("Ingrese la longitud en centímetros: "))
            metros = centimetros / 100
            print(f"{centimetros} cm = {metros} m")
        except:
            print("Error: Ingrese un valor numérico válido")
    
    elif opcion == "5":
        # Kilogramos a Gramos
        try:
            kg = float(input("Ingrese la masa en kilogramos: "))
            gramos = kg * 1000
            print(f"{kg} kg = {gramos} g")
        except:
            print("Error: Ingrese un valor numérico válido")
    
    elif opcion == "6":
        # Gramos a Kilogramos
        try:
            gramos = float(input("Ingrese la masa en gramos: "))
            kg = gramos / 1000
            print(f"{gramos} g = {kg} kg")
        except:
            print("Error: Ingrese un valor numérico válido")
    
    elif opcion == "7":
        # Salir del programa
        print("¡Gracias por usar el conversor!")
        break
    
    else:
        print("Opción no válida. Por favor, elija de 1-7")
    
    # Pausa antes de seguier
    input("\nPresione Enter para continuar...")

print("Saliendo del programa.")