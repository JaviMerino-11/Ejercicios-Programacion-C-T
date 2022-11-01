# Escribe un guión que genere una lista con la diferencia de los listas

# Para ello, defino dos listas para restar una con otra. Defino una nueva lista para recoger el resultado obtenido tras
# hacer la diferencia. Aplico comprehension list porque es el metodo mas optimo para declaracion de estructuras de
# datos. Hago el min(range) para que no tengan que tener el mismo tamaño obligatoriamente

def main():
    lista_entrada_1 = [1, 2, 3, 4]
    lista_entrada_2 = [4, 3, 2, 1]

    lista_diferencias = [lista_entrada_1[numero] - lista_entrada_2[numero] for numero in
                         range(min(len(lista_entrada_1), len(lista_entrada_2)))]

    print("La lista obtenida tras haber restado ambas es: ", lista_diferencias)  # Esta forma tambien es la elegida como
    # algoritmo alternativo, ya que es el mas eficiente.


if __name__ == '__main__':
    main()
