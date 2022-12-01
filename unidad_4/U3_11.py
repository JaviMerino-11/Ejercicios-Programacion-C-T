# Escribe una función que reciba como parámetros una
# lista y una posición y muestre por la salida estándar el contenido
# de dicha posición de la lista y gestione el caso de que la posición
# no exista.

from typing import List


# Para ello vamos a crear una funcion que reciba dos parametros: Una lista, y la posicion sobre la que queremos
# evaluarla, de forma que, si esa posicion no esta dentro del limite que permite la lista, muestre una excepcion

def mostrar_elemento_lista(lista_entrada: List, posicion_elemento: int):
    if posicion_elemento > len(lista_entrada) - 1:
        raise Exception("La posicion que se quiere evaluar no está dentro del dominio de la lista introducida")
    else:
        print("La lista", lista_entrada, "evaluada en la posicion", posicion_elemento, "tiene el siguiente valor:",
              lista_entrada[posicion_elemento])


def main():
    lista_entrada = [2, 4, 10, 6]
    posicion_elemento = int(input("Introduzca la posición del elemento en el que quiere evaluar la lista: "))

    mostrar_elemento_lista(lista_entrada=lista_entrada, posicion_elemento=posicion_elemento)


if __name__ == '__main__':
    main()
