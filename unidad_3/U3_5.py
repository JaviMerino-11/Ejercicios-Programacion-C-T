# Escribe una función generadora que devuelva números pares cada vez que se invoque.

# Generamos una funcion generadora que basicamente vaya sumandole dos desde el principio al final para obtener la
# secuencia de numeros pares.

def generador_numeros_pares(principio=1, final=None):
    while True:
        if final is not None and principio >= final:
            break
        yield principio
        principio += 2


def main():
    numero_principio = int(input("Introduzca el inicio de la secuencia: "))
    numero_final = int(input("Introduzca el final de la secuencia: "))

    lista_numeros_pares = []

    for numeros_pares in generador_numeros_pares(numero_principio, numero_final):
        lista_numeros_pares.append(numeros_pares)

    print("Los numeros pares comprendidos entre %i y %i son" % (numero_principio, numero_final), lista_numeros_pares)


if __name__ == '__main__':
    main()
