# Escribe una función lambda que busque palíndromos en una lista de cadenas de caracteres

# Defino una funcion que reciba una cadena como argumento de entrada, comienzo a recorrerla y comparo la cadena de
# entrada en la ultima posicion con la primera, si coincide, suma un valor la variable "coincide" de forma que, si
# tras evaluar toda la palabra, "coincide" es igual a la longitud de la cadena de entrada, significa que la palabra
# introducida es palindroma.

def busca_palindromos(cadena_entrada: str):
    coincide = 0
    posicion_no_inversa = 0
    for posicion_caracter_inverso in reversed(range(len(cadena_entrada))):
        if cadena_entrada[posicion_caracter_inverso].lower() == cadena_entrada[posicion_no_inversa].lower():
            coincide = coincide + 1
        posicion_no_inversa = posicion_no_inversa + 1

    if len(cadena_entrada) == coincide:
        print("%s es una palabra palindroma" % cadena_entrada)
    else:
        print("%s no es una palabra palindroma" % cadena_entrada)


def main():
    cadena_entrada = input("Introduzca la cadena de caracteres que quiere evaluar: ")

    busca_palindromos(cadena_entrada=cadena_entrada)


if __name__ == '__main__':
    main()
