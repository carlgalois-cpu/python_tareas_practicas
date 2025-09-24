# Tienda / Cotizador 

print("=== TIENDA ===")
print("Bienvenido al sistema de cotizaciones")

# Definir el porcentaje de IVA (16%)
IVA = 0.16

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular total con IVA")
    print("2. Calcular total con descuento + IVA")
    print("3. Calcular precio unitario")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        # Calcular total con IVA
        try:
            print("\n--- CALCULAR TOTAL CON IVA ---")
            precio = float(input("Ingrese el precio del producto: $"))
            cantidad = int(input("Ingrese la cantidad: "))
            
            if precio <= 0 or cantidad <= 0:
                print("Error: El precio y la cantidad deben ser mayores a cero")
            else:
                subtotal = precio * cantidad
                iva_monto = subtotal * IVA
                total = subtotal + iva_monto
                
                print(f"\n--- FACTURA ---")
                print(f"Precio unitario: ${precio:.2f}")
                print(f"Cantidad: {cantidad}")
                print(f"Subtotal: ${subtotal:.2f}")
                print(f"IVA (16%): ${iva_monto:.2f}")
                print(f"TOTAL: ${total:.2f}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "2":
        # Calcular total con descuento + IVA
        try:
            print("\n--- CALCULAR TOTAL CON DESCUENTO + IVA ---")
            precio = float(input("Ingrese el precio del producto: $"))
            cantidad = int(input("Ingrese la cantidad: "))
            
            if precio <= 0 or cantidad <= 0:
                print("Error: El precio y la cantidad deben ser mayores a cero")
            else:
                # Mostrar cupones disponibles
                print("\nCupones disponibles:")
                print("VERANO = 10% de descuento")
                print("SALDOS = 35% de descuento")
                print("BBVA = 5% de descuento")
                print("BANORTE25 = 25% de descuento")
                
                cupon = input("Ingrese el código del cupón: ").upper()
                
                # Definir descuentos según cupón
                descuento = 0
                if cupon == "VERANO":
                    descuento = 0.10
                elif cupon == "SALDOS":
                    descuento = 0.35
                elif cupon == "BBVA":
                    descuento = 0.05
                elif cupon == "BANORTE25":
                    descuento = 0.25
                else:
                    print("Cupón no válido. Se aplicará 0% de descuento")
                
                subtotal = precio * cantidad
                descuento_monto = subtotal * descuento
                subtotal_con_descuento = subtotal - descuento_monto
                iva_monto = subtotal_con_descuento * IVA
                total = subtotal_con_descuento + iva_monto
                
                print(f"\n--- FACTURA CON DESCUENTO ---")
                print(f"Precio unitario: ${precio:.2f}")
                print(f"Cantidad: {cantidad}")
                print(f"Subtotal: ${subtotal:.2f}")
                print(f"Descuento ({descuento*100}%): -${descuento_monto:.2f}")
                print(f"Subtotal con descuento: ${subtotal_con_descuento:.2f}")
                print(f"IVA (16%): ${iva_monto:.2f}")
                print(f"TOTAL: ${total:.2f}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "3":
        # Calcular precio unitario
        try:
            print("\n--- CALCULAR PRECIO UNITARIO ---")
            total = float(input("Ingrese el total pagado: $"))
            cantidad = int(input("Ingrese la cantidad de productos: "))
            
            if total <= 0 or cantidad <= 0:
                print("Error: El total y la cantidad deben ser mayores a cero")
            else:
                precio_unitario = total / cantidad
                print(f"Precio unitario: ${precio_unitario:.2f}")
        except:
            print("Error: Ingrese valores numéricos válidos")
    
    elif opcion == "4":
        # Salir del sitema

        print("¡Gracias por usar el sistema")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione 1-4")
    
    # Pausa antes de continuar
    input("\nPresione Enter para continuar...")

print("Saliendo del sistema")