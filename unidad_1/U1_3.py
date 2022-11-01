# Escribe código para, dado un entero, generar una
# cadena con los dígitos incluidos al revés y separados por
# espacios en blanco (345636 → '6 3 6 5 4 3')

# Para ello, he creado una funcion que recibe un numero entero como argumento de entrada, lo convierto en formato string
# para poder operar con el mas facil, creo una nueva variable que tomara los valores desde el final hasta el inicio y
# les introduzco un espacio en blanco a cada uno a modo de separacion.
def voltear_entero(numero):
    numero = str(numero)
    numero_volteado = numero[::-1]
    numero_volteado_separado = ' '.join(numero_volteado)

    return numero_volteado_separado


def main():
    numero_introducido_usuario = int(input("Introduzca un número entero con varias cifras: "))

    print("El numero introducido es %i.\nEl numero volteado es %s." % (
        numero_introducido_usuario, voltear_entero(numero=numero_introducido_usuario)))


if __name__ == '__main__':
    main()
