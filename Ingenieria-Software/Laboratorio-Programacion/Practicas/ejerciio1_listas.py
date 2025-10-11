# Inicializar y filtrar en una línea
numeros = list(range(1, 21))
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Lista solo con pares:", numeros_pares)
