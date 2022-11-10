# Escribe una función que reciba como parámetro una cadena de caracteres y devuelva un
# diccionario conteniendo el número de ocurrencias de cada carácter de la entrada.

# Vamos a crear una funcion que recibe como entrada una cadena de caracteres, vamos a crear un diccionario vacio sobre
# el que implementaremos el resultado final. Recorremos cada caracter de la cadena de entrada y creamos pareja de clave
# valor entre este caracter y el numero de veces que aparece en la cadena de entrada.

def numero_de_ocurrencias(cadena_entrada: str):
    numero_ocurrencias = dict()

    for caracter in cadena_entrada:
        diccionario_parejas = {
            caracter: cadena_entrada.count(caracter)
        }
        numero_ocurrencias.update(diccionario_parejas)

    return numero_ocurrencias


def main():
    cadena_entrada = input("Introduzca una cadena cualquiera: ")

    print("Cada caracter de %s aparece %s veces." % (
        cadena_entrada, numero_de_ocurrencias(cadena_entrada=cadena_entrada)))


if __name__ == '__main__':
    main()
