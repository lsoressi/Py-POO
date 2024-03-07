# Crear una clase Bicicleta y luego aplica los sgtes adicionales
# Agregar al menos 3 atributos
# Agregar al menos 3 metodos
# Agregar el metodo constructor de la clase

class Bicicleta:
    def __init__(self, marca, cambios, rodado, color, precio, stock, velocidad):
        self.marca = marca
        self.cambios = cambios
        self.rodado = rodado
        self.color = color
        self.precio = precio
        self.stock = stock
        self.velocidad = velocidad 
        

    def bajarVelocidad(self):
        while (self.velocidad > 0):
            self.velocidad -= 1
            print (f'Bajando velocidad {self.velocidad}')
        print(f'Paraste completamente')
    



    
bici = Bicicleta('Venzo', 18, 29, 'Rojo', 250000, 5, 20)
bici.bajarVelocidad()
