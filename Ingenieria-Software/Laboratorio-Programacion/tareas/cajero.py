
saldo = 1000  # Saldo inicial

print("=== CAJERO AUTOMÁTICO ===")
print("Bienvenido/a a su cajero automático")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saldo(tienes_lana)")
    print("2. Retirar(a_gastar)")
    print("3. Depositar(a-ahorrar)")
    print("4. Adios")
    
    opcion = input("Elegir una opción (1-4): ")
    
    if opcion == "1":¡Gracias por usar nuestro cajero automático!, vuelve pronto
        # consultar sueldo
        print(f"\nSu saldo actual es: ${saldo:.2f}")
    
    elif opcion == "2":
        # Retirar dinero
        try:
            monto = float(input("\nIngrese el monto a retirar: $"))
            if monto <= 0:
                print("Error: Escriba un valor correcto.")
            elif monto > saldo:
                print("Error: Saldo insuficiente.")
                print(f"Su saldo actual es: ${saldo:.2f}")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Ha retirado: ${monto:.2f}")
                print(f"Nuevo saldo: ${saldo:.2f}")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    elif opcion == "3":
        # Depositar dinero
        try:
            monto = float(input("\nIngrese el monto a depositar: $"))
            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
            else:
                saldo += monto
                print(f"Depósito exitoso. Ha depositado: ${monto:.2f}")
                print(f"Nuevo saldo: ${saldo:.2f}")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    elif opcion == "4":
        # Salir del programa
        print("\n¡Gracias por usar nuestro cajero automático!")
        print("Hasta pronto.")
        break
    
    else:
        print("\nOpción no válida. Por favor, seleccione 1, 2, 3 o 4.")
    
    # puasa antes de mostrar de nuevo el menú
    input("\nPresione Enter para continuar...")

print("Saliendo del sistema.")