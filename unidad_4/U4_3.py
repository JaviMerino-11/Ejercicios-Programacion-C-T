# Escribe varias clases para representar canciones, artistas, álbumes y listas de reproducción, estableciendo
# relaciones entre ellas. Se pueden asumir la siguientes restricciones: cada canción o álbum tiene un solo cantante,
# puede haber álbumes de compilación con varios artistas. Escribe un programa para ejemplificar el uso de todas las
# clases.

class Artista:
    def __init__(self, nombre_artista: str, genero_musical: str):
        self.nombre_artista = nombre_artista
        self.genero_musical = genero_musical

    def mostrar_datos_artista(self):
        print("Nombre del artista: %s\nGenero musical: %s" % (self.nombre_artista, self.genero_musical))


class Cancion(Artista):
    def __init__(self, nombre_cancion: str, fecha_lanzamiento: int, nombre_artista: str, genero_musical: str):
        super().__init__(nombre_artista, genero_musical)
        self.nombre_cancion = nombre_cancion
        self.fecha_lanzamiento = fecha_lanzamiento

    def mostrar_informacion_cancion(self):
        print(self.mostrar_datos_artista(), "Nombre cancion: %s\nFecha de lanzamiento: %i" % (
            self.nombre_cancion, self.fecha_lanzamiento))


class Album(Cancion):
    def __init__(self, fecha_publicacion_album: int, puntuacion: float, nombre_cancion: str, fecha_lanzamiento: int,
                 nombre_artista: str, genero_musical: str):
        super().__init__(nombre_cancion, fecha_lanzamiento, nombre_artista, genero_musical)
        self.fecha_publicacion_album = fecha_publicacion_album
        self.puntuacion = puntuacion

    def mostrar_informacion_album(self):
        print(self.mostrar_informacion_cancion(), "Fecha publicacion album: %s\nPuntuacion obtenida sobre 5: %i" % (
            self.fecha_publicacion_album, self.puntuacion))


class ListaReproduccion(Album):
    def __init__(self, nombre_lista_reproduccion: str, fecha_publicacion_album: int, puntuacion: float,
                 nombre_cancion: str, fecha_lanzamiento: int, nombre_artista: str, genero_musical: str):
        super().__init__(fecha_publicacion_album, puntuacion, nombre_cancion, fecha_lanzamiento, nombre_artista,
                         genero_musical)
        self.nombre_lista_reproduccion = nombre_lista_reproduccion

    def mostrar_informacion_lista_reproduccion(self):
        print(self.mostrar_informacion_album(), "Nombre de la lista: %s" % self.nombre_lista_reproduccion)


def main():
    nombre_artista = input("Introduzca el nombre del artista: ")
    genero_musical = input("Introduzca el genero musical del artista: ")
    nombre_cancion = input("Introduzca el nombre de la cancion del artista: ")
    fecha_lanzamiento_cancion = int(input("Introduzca la fecha de lanzamiento de la cancion: "))
    fecha_publicacion_album = int(input("Introduzca la fecha de publicacion del album: "))
    puntuacion_album = float(input("Introduzca la puntuacion sobre 5 del album: "))
    nombre_lista_reproduccion = input("Introduzca el nombre de la lista de reproduccion: ")

    lista_reproduccion_1 = ListaReproduccion(nombre_lista_reproduccion=nombre_lista_reproduccion,
                                             fecha_publicacion_album=fecha_publicacion_album,
                                             puntuacion=puntuacion_album, nombre_cancion=nombre_cancion,
                                             fecha_lanzamiento=fecha_lanzamiento_cancion, nombre_artista=nombre_artista,
                                             genero_musical=genero_musical)

    album_1 = Album(fecha_publicacion_album=fecha_publicacion_album, puntuacion=puntuacion_album,
                    nombre_cancion=nombre_cancion, fecha_lanzamiento=fecha_lanzamiento_cancion,
                    nombre_artista=nombre_artista, genero_musical=genero_musical)

    album_1.mostrar_informacion_album()

    lista_reproduccion_1.mostrar_informacion_lista_reproduccion()


if __name__ == '__main__':
    main()
