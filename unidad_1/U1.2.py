# Dado un número leído desde la entrada estándar,
# escribir un programa que adivine en el menor número de pasos
# posible un número pensado por el usuario desde 0 al número
# leído.

import random


def adivinar_numero(numero_pensado_usuario: int):
    numero_pensado_usuario_list = [numero_pensado_usuario]
    for enumeracion in range(numero_pensado_usuario + 1):
        if enumeracion in numero_pensado_usuario_list:
            print("He adivinado el numero que introdujiste en la iteraccion numero %i!" % enumeracion)
            break
        else:
            print("Aun no he adivinado el numero que introdujiste :(")


def main():
    # numero_pensado_usuario = int(input("Introduzca un número entero: "))

    numero_pensado_usuario = random.randint(1, 20)  # Esto lo hago en el caso en el que el numero introducido sea random
    adivinar_numero(numero_pensado_usuario=numero_pensado_usuario)


if __name__ == '__main__':
    main()
