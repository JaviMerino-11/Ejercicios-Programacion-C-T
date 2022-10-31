# Escribe un guión que almacene varias
# palabras en español y su traducción al inglés. El
# usuario podrá introducir por la entrada estándar
# palabras a traducir hasta que teclee “fin”.
import sys


# Para ello voy a crear un diccionario en el que las claves sean palabras en espaniol y los valores sean su traduccion
# al ingles. Teniendo ese diccionario de modelo, voy a pedirle al usuario que introduzca una palabra cualquiera, si esa
# palabra coincide con el valor de la clave, nos devolvera su traduccion al ingles asociada a ese valor de la clave. Por
# otro lado, si la palabra introducida es "fin", saldremos del bucle de iteracion. Si introduce una palabra que no
# pertenece a este modelo, pedira que revise.

def traductor_esp_to_ing():
    spanish_english_words = {
        "hola": "hello",
        "adios": "goodbye",
        "sol": "sun",
        "nube": "cloud",
        "arbol": "tree"
    }

    palabra_introducida = input(
        "Elija una opcion entre %s para obtener su traduccion, o escriba \"fin\" para salir -- "
        % spanish_english_words.keys())

    if palabra_introducida in spanish_english_words.keys():
        print("La traduccion en ingles de %s es %s" % (palabra_introducida, spanish_english_words[palabra_introducida]))
    elif palabra_introducida == "fin":
        sys.exit("Has decidido salir del programa")
    else:
        print("Por favor, introduce una palabra que pertenezca a %s" % spanish_english_words.keys())


def main():
    traductor_esp_to_ing()


if __name__ == '__main__':
    main()
