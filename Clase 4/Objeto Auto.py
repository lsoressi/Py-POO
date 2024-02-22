class Auto:
    # PROPIEDADES / Atributos
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        
    # MÉTODOS - comportamientos, acciones
    # Getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAnio(self):
        return self.anio
    
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()}')
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()}')
        print(f'Anio: {self.getAnio()}')

auto1 = Auto("Toyota", "Prius", "Rojo", "2020")
auto2 = Auto("Peugeot", "208", "Azul", "2022")

auto1.mostrarAuto()
auto2.mostrarAuto()
    