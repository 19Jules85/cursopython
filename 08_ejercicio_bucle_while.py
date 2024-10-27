#Adivina el número

import random

print("¡Bienvenido al juego de adivina un número!")
print("Trata de adivinar un número entre el 1 y el 5")

numero_secreto = random.randint(1,5)
adivinado = False
while not adivinado:
    numero_usuario = int(input("Ingresa un número: "))

    if(numero_usuario == numero_secreto):
        print("Felicidaes has acertado")
        adivinado =True
    elif numero_usuario < numero_secreto:
        print("El número secreto es mas alto")
    else:
        print("El número secreto es más bajo")