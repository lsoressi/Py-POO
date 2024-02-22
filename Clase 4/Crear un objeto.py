class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
        

def comer(self):
    print (f'estoy comiendo') 
    pass

class Perro (Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        
        super().__init__(cantidad_patas, tipo, nombre, raza)
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
        self.nombre = nombre
        self.raza = raza
    
 def correr(self):
    return (f'estoy corriendo')

class Aguila (Animal)
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo) 
        self.cantidad_patas = cantidad_patas 
        self.tipo = tipo
def volar(self):
    return (f'estoy volando')      


        from enum import Enum

class Tipo(Enum):
    VERTEBRADO = "vertebrado"
    INVERTEBRADO = "invertebrado"
class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        print("estoy comiendo")
    
class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        print("estoy corriendo")

class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)
    
    def volar(self):
        print("estoy volando")