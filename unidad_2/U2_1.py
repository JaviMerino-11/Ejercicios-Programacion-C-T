# Escribe un guión que calcule el número mayor de una lista de enteros.

# Para ello, vamos a crear una variable que sera la que nos sirva de comparacion en cada momento. Cuando recorremos la
# lista, vamos comparando el valor de la lista por orden con ese valor, de forma que, cuando el valor del elemento de la
# lista sea mayor que el que estuviera guardado como superior, se almacenara este como maximo. Esto se ira haciendo
# continuamente hasta quedarnos finalmente con el ultimo valor que lo cumpla, que sera el maximo absoluto.

def main():
    lista_entrada = [1, 2, 3, 4, 5]
    maximo_auxiliar = None

    for numero in lista_entrada:
        if maximo_auxiliar is None or numero > maximo_auxiliar:
            maximo_auxiliar = numero

    print("El valor maximo es: ", maximo_auxiliar)

    # print("El valor maximo es: ", max(lista_entrada))  # Asi se haria directamente


if __name__ == '__main__':
    main()
