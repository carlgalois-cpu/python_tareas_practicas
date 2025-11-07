import random

# Inicializar lista con 10 valores aleatorios del 1 al 10
valores = [random.randint(1, 10) for _ in range(10)]
print("Lista de valores:", valores)

# Mostrar cada elemento con su cuadrado y cubo
print("\nValor | Cuadrado | Cubo")
print("-" * 25)
for num in valores:
    cuadrado = num ** 2
    cubo = num ** 3
    print(f"{num:5} | {cuadrado:8} | {cubo:4}")
