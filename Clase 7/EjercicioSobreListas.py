# Una fábrica de instrumentos musicales posee una lista con todas sus sucursales.
# Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta.
# De cada uno de ellos se sabe su ID alfanumérico, su precio y su tipo
# (Percusión, Viento o Cuerda).
# class padre Fabrica
    #-Sucursales, que es una lista 

# Puntos a desarrollar
# 1)Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten
# las clases con sus atributos, métodos y relaciones (los constructores pueden omitirse).

# 2) Crear un proyecto en Python que resuelva:
    # A) método listarInstrumentos que muestre en la consola todos los
    # datos de cada uno de los instrumentos. - DEVOLVEME TODOS LOS INSTRUMENTOS
    # B) método instrumentosPorTipo que devuelva una lista de 
    # instrumentos cuyo tipo coincida con el recibido por parámetro. ... DE CUERDAS (FILTRO)
    # C) método borrarInstrumento que reciba un ID y elimine el
    #instrumento asociado a tal ID de la sucursal donde se encuentre.
    # D) método porcInstrumentosPorTipo que reciba el nombre de una
    # sucursal y retorne los porcentajes de instrumentos por tipo que hay para tal sucursal.


from enum import Enum

class TipoInstrumento(Enum):
    PER = "Percusion"
    VIE = "Viento"
    CUE = "Cuerda" 


class Fabrica:
    def __init__(self, sucursales):
        self.sucursales = sucursales

    def listarInstrumentos():
        print()

    def instrumentosPorTipo():
        print()


class Sucursal:
    def __init__(
        self,
        nombre,
        instrumento 
        ):
        self.nombre = nombre
        self.instrumento = instrumento

    def borrarInstrumento():
        print

    def porcInstrumentoPorTipo ():
        print()
        

class Instrumento:
     def __init__(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo


        
        
        
        


