# Escribe una función que reciba dos parámetros numéricos y devuelva la suma y la resta
# de los mismos

# Vamos a crear una funcion que tenga como argumento de entrada dos numeros enteros y que devuelva su suma y su resta

def suma_y_resta(numero_1: int, numero_2: int):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2

    return suma, resta


def main():
    numero_1 = int(input("Introduzca un numero entero: "))
    numero_2 = int(input("Introduzca otro numero entero: "))

    suma, resta = suma_y_resta(numero_1, numero_2)

    print("La suma de %i y %i es %i" % (numero_1, numero_2, suma))
    print("La resta de %i y %i es %i" % (numero_1, numero_2, resta))


if __name__ == '__main__':
    main()
