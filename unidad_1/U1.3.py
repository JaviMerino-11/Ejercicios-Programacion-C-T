# Escribe código para, dado un entero, generar una
# cadena con los dígitos incluidos al revés y separados por
# espacios en blanco (345636 → '6 3 6 5 4 3')

def voltear_entero(numero):
    numero = str(numero)
    numero_volteado = numero[::-1]
    numero_volteado_separado = ' '.join(numero_volteado)

    return numero_volteado_separado


def main():
    numero_pensado_usuario = int(input("Introduzca un número entero con varias cifras: "))

    print("El numero pensado es %i.\nEl numero volteado es %s." % (
        numero_pensado_usuario, voltear_entero(numero=numero_pensado_usuario)))


if __name__ == '__main__':
    main()
