# Administrador de calificaciones

print("=== ADMINISTRADOR DE CALIFICACIONES ===")
print("Bienvenido al sistema de admistración de calificaciones")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular promedio simple")
    print("2. Calcular calificación final con ponderaciones")
    print("3. Mostrar mayor y menor calificación")
    print("4. Verificar aprobación/reprobación")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        # sacando el promedio
        try:
            print("\n--- PROMEDIO SIMPLE ---")
            p1 = float(input("Ingrese calificación del parcial 1: "))
            p2 = float(input("Ingrese calificación del parcial 2: "))
            p3 = float(input("Ingrese calificación del parcial 3: "))
            
            if p1 < 0 or p1 > 100 or p2 < 0 or p2 > 100 or p3 < 0 or p3 > 100:
                print("Error: Las calificaciones deben estar entre 0 y 100")
            else:
                promedio = (p1 + p2 + p3) / 3
                print(f"Promedio simple: {promedio:.2f}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "2":
        # Calculando calificación final con ponderaciones
        try:
            print("\n--- CALIFICACIÓN FINAL CON PONDERACIONES ---")
            p1 = float(input("Ingrese calificación del parcial 1: "))
            p2 = float(input("Ingrese calificación del parcial 2: "))
            p3 = float(input("Ingrese calificación del parcial 3: "))
            
            print("\nIngrese las ponderaciones (deben sumar 100%):")
            pond1 = float(input("Ponderación parcial 1 (%): "))
            pond2 = float(input("Ponderación parcial 2 (%): "))
            pond3 = float(input("Ponderación parcial 3 (%): "))
            
            if p1 < 0 or p1 > 100 or p2 < 0 or p2 > 100 or p3 < 0 or p3 > 100:
                print("Error: Las calificaciones deben estar entre 0 y 100")
            elif pond1 + pond2 + pond3 != 100:
                print("Error: Las ponderaciones deben sumar 100%")
            else:
                final = (p1 * pond1/100) + (p2 * pond2/100) + (p3 * pond3/100)
                print(f"Calificación final: {final:.2f}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "3":
        # Mostrar mayor y menor calificación
        try:
            print("\n--- MAYOR Y MENOR CALIFICACIÓN ---")
            p1 = float(input("Ingrese calificación del parcial 1: "))
            p2 = float(input("Ingrese calificación del parcial 2: "))
            p3 = float(input("Ingrese calificación del parcial 3: "))
            
            if p1 < 0 or p1 > 100 or p2 < 0 or p2 > 100 or p3 < 0 or p3 > 100:
                print("Error: Las calificaciones deben estar entre 0 y 100")
            else:
                mayor = p1
                menor = p1
                
                if p2 > mayor:
                    mayor = p2
                if p3 > mayor:
                    mayor = p3
                
                if p2 < menor:
                    menor = p2
                if p3 < menor:
                    menor = p3
                
                print(f"Mayor calificación: {mayor}")
                print(f"Menor calificación: {menor}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "4":
        # Verificar aprobación/reprobación
        try:
            print("\n--- VERIFICAR APROBACIÓN ---")
            p1 = float(input("Ingrese calificación del parcial 1: "))
            p2 = float(input("Ingrese calificación del parcial 2: "))
            p3 = float(input("Ingrese calificación del parcial 3: "))
            
            if p1 < 0 or p1 > 100 or p2 < 0 or p2 > 100 or p3 < 0 or p3 > 100:
                print("Error: Las calificaciones deben estar entre 0 y 100")
            else:
                # Primero calcular promedio simple para verificar
                promedio = (p1 + p2 + p3) / 3
                
                if promedio >= 60:
                    print(f"APROBADO - Promedio: {promedio:.2f}")
                else:
                    print(f"REPROBADO - Promedio: {promedio:.2f}")
                
                # También verificar si hay algún parcial reprobado (menos de 60)
                if p1 < 60:
                    print(f"Parcial 1 reprobado: {p1}")
                if p2 < 60:
                    print(f"Parcial 2 reprobado: {p2}")
                if p3 < 60:
                    print(f"Parcial 3 reprobado: {p3}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "5":
        # Salir del programa
        print("¡Gracias por usar el Gestor de Calificaciones!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione 1-5")
    
    # Pausa antes de seguir
    input("\nPresione Enter para continuar...")

print("Saliendo del programa")