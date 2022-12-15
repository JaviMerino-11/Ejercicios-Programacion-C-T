# Escribe una función que reciba como argumento el nombre de un fichero de texto y devuelva una lista con su
# contenido.

from typing import List


# Para ello vamos a crear una funcion que reciba el nombre del archivo de texto de entrada, vamos a abrir ese fichero
# y vamos a ir recorriendo linea por linea su contenido, de forma que la salida de la propia función será una lista
# con el contenido del fichero de texto.

def leer_contenido_archivo(archivo_entrada: str) -> List[str]:
    contenido = []
    for line in open(archivo_entrada, 'r'):
        contenido.append(line)
    return contenido


def main():
    archivo_entrada = "archivo_texto.txt"

    print("El contenido del fichero introducido en formato de lista es:\n",
          leer_contenido_archivo(archivo_entrada=archivo_entrada))


if __name__ == '__main__':
    main()
