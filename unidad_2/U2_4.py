# Escribe un guión en el que se introduzca por la entrada estándar un número, n, se cree una
# lista con los enteros de 1 a n y genere otra con los primos mediante la criba de Eratóstenes.

# Para ello, el usuario va a introducir un numero entero cualquiera, aplicamos la criba de eratostenes: introducimos
# los numeros naturales entre 2 y el numero que introduzca el usuario, y voy quitando los numeros que no son primos --
# cuando se encuentra un número entero que no ha sido tachado, ese número es declarado primo, y se procede a tachar
# todos sus múltiplos. El proceso termina cuando el cuadrado del mayor número confirmado como primo es mayor que el
# numero introducido.

def criba_eratostenes(numero_entero: int):
    multiplos = set()
    for numero in range(2, numero_entero + 1):
        if numero not in multiplos:
            print("Los numeros primos son: ", numero)
            multiplos.update(range(numero * numero, numero_entero + 1, numero))


def main():
    numero_introducido = int(input("Introduzca un numero entero cualquiera: "))
    criba_eratostenes(numero_entero=numero_introducido)


if __name__ == '__main__':
    main()
