# Escribe una función que reciba como argumento el nombre de un fichero csv de números enteros (10 filas de 10
# enteros separados por comas) y devuelva una matriz con el contenido.

from typing import List


# Para ello vamos a crear una funcion que reciba el nombre de un archivo csv formado por 10 filas y 10 columnas de
# numeros enteros separados por comas para devolver una matriz 10x10 con ese contenido.
# Vamos a utilizar un context manager para que, una vez manipulado el propio archivo csv, este se cierre
# automaticamente. Tras crear el csv de 10 filas x 10 columnas, vamos a ir recorriendo cada valor de cada fila y le
# vamos a ir quitando las comas que lo separan. Por ultimo, esos valores sin comas, vamos a quitarle el salto de linea
# para que no haya problema a la hora de crear la matriz resultante en formato lista.

def crear_matriz_fichero_csv(archivo_entrada: str) -> List[List[str]]:
    matriz_resultante = []

    with open(archivo_entrada) as input_file:
        for fila in input_file:
            matriz_sin_comas = fila.replace(',', '')
            matriz_auxiliar = [numero_matriz for numero_matriz in matriz_sin_comas] # Comprehension list para optimizar la creacion de esta lista

            for elemento_matriz in matriz_auxiliar:
                if elemento_matriz == '\n':
                    matriz_auxiliar.remove(elemento_matriz)

            matriz_resultante.append(matriz_auxiliar)

    return matriz_resultante


def main():
    archivo_entrada = "matriz_entrada.csv"

    print("El contenido del fichero introducido es:\n", crear_matriz_fichero_csv(archivo_entrada=archivo_entrada))


if __name__ == '__main__':
    main()
