# Dado un número leído desde la entrada estándar,
# escribir el código que itere desde 1 hasta el número y haga y
# muestre la suma de los pares.

# Para ello, he creado una funcion que recibe como argumento un numero entero introducido por el usuario, de forma que
# hacemos un bucle que vaya desde 1 hasta ese numero y guardamos en una lista aquellos numeros cuyo resto al dividir
# entre 2 sea 0, es decir, sean pares. Tras tomar todos los numeros pares, haremos la suma de todos ellos, que sera lo
# que devolvamos.
def sumar_numeros_pares(numero_entrada: int):
    numeros_pares = []
    suma_numeros_pares = []

    for enumeracion in range(1, numero_entrada + 1):
        if enumeracion % 2 == 0:
            numeros_pares.append(enumeracion)
            suma_numeros_pares = sum(numeros_pares)

    print("La suma total de los numeros pares concentrados entre 1 y %i es: %i" % (
        numero_entrada, suma_numeros_pares))


def main():
    numero_entrada = int(input("Introduzca un número entero: "))
    sumar_numeros_pares(numero_entrada=numero_entrada)


if __name__ == '__main__':
    main()
