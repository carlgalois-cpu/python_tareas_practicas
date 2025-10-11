# Crear tuple con números
numeros = (3, 8, 15, 22, 7, 14, 9, 6, 11)

# Mostrar solo los números pares usando for
print("Números pares:")
for num in numeros:
    if num % 2 == 0:  # Si el número dividido entre 2 da residuo 0, es par
        print(num)
