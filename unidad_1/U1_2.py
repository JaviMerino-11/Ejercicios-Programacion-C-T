# Dado un número leído desde la entrada estándar,
# escribir un programa que adivine en el menor número de pasos
# posible un número pensado por el usuario desde 0 al número
# leído.

import random

#Para ello, he creado un metodo que recibe como argumento un numero (he creado la opcion de que sea aleatorio o que
# sea introducido por el usuario, sólo hay que descomentar una y comentar la otra). Meto ese valor en una lista para que
# sea mas facil de iterar; la recorro y voy comprobando si el valor de iteraccion coincide con el numero, en el momento
# en el que si coincida salgo del bucle y muestro por pantalla a que intento lo he encontrado.
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
