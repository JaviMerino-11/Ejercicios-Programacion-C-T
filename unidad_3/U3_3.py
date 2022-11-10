# Escribe una función recursiva que calcule la suma desde 0 a n (n pasado como argumento).

# Para ello vamos a crear una funcion en la que vayamos sumando desde 0 hasta su valor


def suma_recursiva(numero_entrada: int):
    if numero_entrada <= 1:
        return numero_entrada
    return numero_entrada + suma_recursiva(numero_entrada - 1)


def main():
    numero_entrada = int(input("Introduzca un numero entero: "))

    print("La suma de todos los elementos desde 0 hasta %i es %i" % (
        numero_entrada, suma_recursiva(numero_entrada=numero_entrada)))


if __name__ == '__main__':
    main()
