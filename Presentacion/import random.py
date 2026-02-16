import random

# Lista de opciones posibles
opciones = ["piedra", "papel", "tijera"]

# El usuario ingresa su elección
usuario = input("Elige piedra, papel o tijera: ").lower()

# La computadora genera una opción aleatoria
computadora = random.choice(opciones)

print("La computadora eligió:", computadora)

# Estructura lógica para determinar el resultado
if usuario == computadora:
    print("Es un empate.")

elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("Ganaste la ronda.")

else:
    print("Perdiste la ronda.")
    
    