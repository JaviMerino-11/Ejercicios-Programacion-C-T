# Dado un conjunto compuesto por palabras vacías (aquellas que no tiene significado – preposiciones, determinantes,
# conjunciones, etc. – y una frase introducida por el usuario en la entrada estándar, crear un conjunto sólo con
# aquellas que no sean vacías.

# Voy a crear un set para todas las preposiciones, algunas conjunciones y algunos determinantes,
# tras ello voy a formar un set definitivo siendo este la union de estos tres primeros. A continuacion, le pedimos al
# usuario que cree una frase con las palabras que quiera pero que algunas sean las que aparece en el conjunto de
# palabras vacias. Normalizamos la frase a minuscula, separamos por espacios en blanco para formar la variable que
# recorriendo para hacer el check de si pertenece o no al conjunto de palabras vacias. Por ultimo, si no pertenece a
# este conjunto, se almacenara en una variable de resultado final que se mostrara por pantalla.
# Para que fuera ideal y funcionara siempre, habria que recoger todas las palabras que conforman las conjunciones, todos
# los tipos de determinantes... Sin embargo, solo he recogido algunos de los que conforman la lengua espaniola

def empty_words_handler():
    preposiciones = {"a", "ante", "bajo", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta",
                     "mediante", "para", "por", "segun", "sin", "sobre", "tras", "via"}
    conjunciones = {"y", "e", "ni", "o", "pero"}
    determinantes = {"este", "ese", "aquel", "mi", "tu", "su", "el", "lo", "más", "una"}

    palabras_vacias = preposiciones.union(conjunciones, determinantes)

    frase_usuario = input("Cree una frase cualquiera que esté compuesta por elementos que pertenezcan y otros que no a:"
                          " \n%s\n--" % palabras_vacias)
    frase_normalizada = frase_usuario.lower()
    frase_separada = frase_normalizada.split(' ')

    palabras_no_vacias = set()

    for palabra in frase_separada:
        if palabra not in palabras_vacias:
            palabras_no_vacias.add(palabra)

    print("La frase de entrada fue: \"%s\"\nTras quitarle determinantes, preposiciones... obtenemos: %s" % (
        frase_usuario, palabras_no_vacias))


def main():
    empty_words_handler()


if __name__ == '__main__':
    main()
