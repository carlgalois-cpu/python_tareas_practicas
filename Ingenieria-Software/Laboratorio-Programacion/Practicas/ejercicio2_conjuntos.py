import random

# Generar conjunto de 10 boletos
boletos = set(random.sample(range(1, 101), 10))  # 10 números únicos
boleto_ganador = random.choice(list(boletos))    # Elegir ganador aleatorio

print("Boletos participantes:", boletos)
print("Boleto ganador:", boleto_ganador)

# Simular rifa con while
while True:
    boleto_sacado = random.choice(list(boletos))
    print("Saque el boleto:", boleto_sacado)
    
    if boleto_sacado == boleto_ganador:
        print("¡GANASTE! Encontré el boleto ganador")
        break
    else:
        boletos.remove(boleto_sacado)  # Eliminar boleto ya extraído