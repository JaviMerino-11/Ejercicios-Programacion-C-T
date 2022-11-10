# Escribe una función que reciba un número variable de parámetros clave valor y que devuelva
# un diccionario que los almacene.

# Creo un sistema para introducir cadenas (el requisito es que sea un numero par para poder separar en clave valor)
# hasta que introduzca fin. Como vamos a introducir clave,valor,clave,valor -- las claves estaran en las posiciones
# pares y los valores en las impares, las voy almacenando. Creo un diccionario auxiliar para almacenar estas parejas.


def crear_diccionario(*args: list[str]):
    claves = []
    valores = []

    diccionario_resultado = {}
    diccionario_auxiliar = {}

    for elementos_entrada in args:
        for contador_clave_valor in range(len(elementos_entrada)):
            if contador_clave_valor % 2 == 0:
                claves.append(elementos_entrada[contador_clave_valor])
            else:
                valores.append(elementos_entrada[contador_clave_valor])
        else:
            for clave in claves:
                for valor in valores:
                    if clave not in diccionario_auxiliar.keys() and valor not in diccionario_auxiliar.values():
                        diccionario_auxiliar = {
                            clave: valor
                        }
                        diccionario_resultado.update(diccionario_auxiliar)

    return diccionario_resultado


def main():
    valor_entrada = None
    lista_entrada = []

    while valor_entrada != 'Fin':
        valor_entrada = input("Introduzca un numero par de cadenas de caracteres o escriba Fin para terminar: ")
        lista_entrada.append(valor_entrada)
        if 'Fin' in lista_entrada:
            lista_entrada.remove('Fin')

    if len(lista_entrada) % 2 != 0:
        raise Exception("Introduzca un numero par de cadenas de entrada!!")

    print("Se ha formado", crear_diccionario(lista_entrada), "a partir de las entradas", lista_entrada)


if __name__ == '__main__':
    main()
