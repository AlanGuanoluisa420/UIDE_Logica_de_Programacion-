import random

opciones = ["piedra", "papel", "tijera"]

jugar = "si"

while jugar == "si":

    usuario = input("Elige piedra, papel o tijera: ").lower()

    if usuario not in opciones:
        print("Opción inválida.\n")
        continue

    computadora = random.choice(opciones)

    print("La computadora eligió:", computadora)

    if usuario == computadora:
        print("Es un empate.")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("Ganaste la ronda.")
    else:
        print("Perdiste la ronda.")
    while True:
        jugar = input("\n¿Quieres jugar otra vez? (si/no): ").lower()
        
        if jugar == "si" or jugar == "no":
            break
        else:
            print("Ingrese solo 'si' o 'no'.")

print("Gracias por jugar 🎮")