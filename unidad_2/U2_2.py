# Escribe un guión que elimine los elementos duplicados de una lista

# Para ello, vamos a crear una variable que sera la que nos sirva de comparacion en cada momento. Cuando recorremos la
# lista, vamos comparando el valor de la lista por orden con ese valor, de forma que, cuando el valor del elemento de la
# lista sea igual que el que estuviera guardado como superior, se almacenara este como espejo. Esto se ira haciendo
# continuamente hasta quedarnos finalmente con el ultimo valor que lo cumpla, que sera el valor repetido.

def main():
    lista_entrada = [1, 1, 1, 2, 3, 4, 4, 4, 5, 5]

    lista_sin_duplicados = []

    for numero in lista_entrada:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)

    print("La lista sin numeros duplicados es: ", lista_sin_duplicados)

    # print("La lista sin numeros duplicados es: ", list(set(lista_sin_duplicados))) # Al convertir la lista en set se
    # eliminan automaticamente los numeros repetidos, he vuelto a transformarla en lista para mantener la estructura.


if __name__ == '__main__':
    main()
