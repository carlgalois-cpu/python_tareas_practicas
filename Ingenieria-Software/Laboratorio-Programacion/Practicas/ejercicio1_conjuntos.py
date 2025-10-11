import random

# Generar dos conjuntos aleatorios
conjunto1 = set(random.sample(range(1, 31), 8))  # 8 números únicos entre 1-30
conjunto2 = set(random.sample(range(1, 31), 8))

# Unir los conjuntos
union_conjuntos = conjunto1 | conjunto2

# Mostrar números mayores a 10 usando for
print("Números mayores a 10 en la unión:")
for numero in union_conjuntos:
    if numero > 10:
        print(numero)