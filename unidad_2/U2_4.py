# Escribe un guión en el que se introduzca por la entrada estándar un número, n, se cree una
# lista con los enteros de 1 a n y genere otra con los primos mediante la criba de Eratóstenes.

# Para ello, el usuario va a introducir un numero entero cualquiera, creamos una lista que vaya desde 1 hasta ese mismo
# numero introducido. Por otro lado, vamos a crear otra lista que recoja los numeros primos desde 1 hasta n

def main():
    numero_introducido = int(input("Introduzca un numero entero cualquiera: "))

    lista_enteros = list()
    lista_primos = list()

    for numero in range(1, numero_introducido + 1):  # REVISAR
        lista_enteros.append(numero)
        if numero % numero != 0:
            lista_primos.append(numero)


if __name__ == '__main__':
    main()
