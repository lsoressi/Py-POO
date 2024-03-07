# Ejemplo de Libreria que vende LIBROS-DISCOS-PELICULAS
# Herencia y Encapsulamiento
# Creamos la estructura de la libreria en base a los productos (libros,discos,peliculas)

from enum import Enum

class GeneroLiterario(Enum):
    NOVELA = "Novela"
    ENSAYO = "Ensayo"
    BIOGRAFIA = "Biografia"

class GenerosCine (Enum):
    POLICIAL = "POLICIAL"
    DOCUMENTAL = "DOCUMENTAL"
    INFANTIL = "INFANTIL"

class GenerosMusica (Enum):
    ROCK = "ROCK"
    CLASICA = "CLASICA"
    TRAP = "TRAP"

class TiposTapa (Enum):
    DURA = "DURA"
    BLANDA = "BLANDA"
    


class Producto:
# todos los productos tendran estas prop
    def __init__(self, id, titulo, autor, precio, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio        
        self.stock = stock

    def mostrarProducto(self):
        pass
    # pass significa pasar la funcionalidad a los hijos, 

class Libro(Producto):
    def __init__(
            self,
            id, 
            titulo, 
            autor, 
            precio, 
            stock, 
            editorial, 
            tapa, 
            generoliterario
            ):
        super().__init__(id, titulo, autor, precio, stock)
        self.editorial = editorial
        self.tapa = tapa
        self.generoliterario = generoliterario

    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Editorial: {self.editorial}')
        print(f'Tapa: {self.tapa}')  #enums
        print(f'Genero Literario: {self.generoliterario}')  #enums

class Musica(Producto):
    def __init__(
            self,
            id, 
            titulo, 
            autor, 
            precio, 
            stock, 
            duracionMinutos,
            formato,
            sello
        ):
        super().__init__(id, titulo, autor, precio, stock)  #lo que se hereda del Padre
        self.duracionMinutos = duracionMinutos
        self.formato = formato
        self.sello = sello

    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Duracion Minutos: {self.duracionMinutos}')
        print(f'Formato: {self.formato}')  #enums
        print(f'Sello: {self.sello}')    #enums

class Pelicula(Producto):
    def __init__(
            self,
            id, 
            titulo, 
            autor, 
            precio, 
            stock, 
            calificacion,
            estudio,
            fuePremiada
        ):
        super().__init__(id, titulo, autor, precio, stock)  #lo que se hereda del Padre
        self.calificacion = calificacion
        self.estudio = estudio
        self.fuePremiada = fuePremiada

    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Calificacion: {self.calificacion}')
        print(f'Estudio: {self.estudio}')  #enums
        print(f'Fue Premiada: {self.fuePremiada}')    #True/False




libro1 = Libro('1', 'Quijote', 'Cervantes', 15000, 10, 'Anagrama', TiposTapa.DURA.value, GeneroLiterario.NOVELA.value)
libro2 = Libro('2', '1984', 'Orwell', 20000, 45, 'De Bolsillo', TiposTapa.BLANDA.value, GeneroLiterario.NOVELA.value)


class FormatoDiscos(Enum):
    CD = 'CD'
    VINILO = 'Vinilo'

musica1 = Musica('1', 'Fix You', 'Coldplay', 3000, 15, 60, FormatoDiscos.VINILO.value, 'Sony')
musica2 = Musica('2', 'The Scientist', 'Coldplay', 2700, 15, 75, FormatoDiscos.CD.value, 'Warner')
musica3 = Musica('3', 'In my place', 'Coldplay', 3100, 15, 65, FormatoDiscos.CD.value, 'Sony')

class CalificacionesCine(Enum):
    ATP = 'ATP'
    Mas13 = '+13'
    Mas16 = '+16'
    Mas18 = '+18'

pelicula1 = Pelicula('1', 'Spiderman', 'Sam Raini', 15000, 20, CalificacionesCine.Mas13.value, 'Disney', False)
pelicula2 = Pelicula('2', 'EL Exsorcista', 'John Borman', 14500, 10, CalificacionesCine.Mas18.value, 'Dreamworks', True)


print('LIBROS')
libro1.mostrarProducto()
print('------')
libro2.mostrarProducto()
print('------')
print('DISCOS')
musica1.mostrarProducto()
print('------')
musica2.mostrarProducto()
print('------')
print('PELICULAS')
pelicula1.mostrarProducto()
print('------')
pelicula2.mostrarProducto()
print('------')




    
               
    