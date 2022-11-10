# Escribe una función lambda que calcule el cuadrado y el cubo de una lista de números enteros.

# Defino una funcion para calcular el cuadrado y el cubo de una lista de numeros enteros

def calcula_cuadrado_y_cubo(lista_numeros_entrada: list[int]):
    return [numero * numero for numero in lista_numeros_entrada], [numero * numero * numero for numero in
                                                                   lista_numeros_entrada]


def main():
    numero_entrada = None
    lista_numeros_entrada = []

    while numero_entrada != -1:
        numero_entrada = int(
            input("Introduzca los numeros al que quiera hacerle el cuadrado y el cubo o introduzca -1 para salir: "))
        lista_numeros_entrada.append(numero_entrada)
        if -1 in lista_numeros_entrada:
            lista_numeros_entrada.remove(-1)

    resultado_cuadrado, resultado_cubo = calcula_cuadrado_y_cubo(lista_numeros_entrada=lista_numeros_entrada)

    print("De la lista de numeros", lista_numeros_entrada, "se obtienen el cuadrado como", resultado_cuadrado,
          "y el cubo como", resultado_cubo)


if __name__ == '__main__':
    main()
