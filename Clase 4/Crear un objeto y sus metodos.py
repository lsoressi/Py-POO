# Introduccion a la POO, que es un objeto - entidad- atributos
# Clases (es el molde de los objetos)
# el constructor, ded_init_ ponemos los atributos que usaremos en ntra clase
# INSTANCIAS, ejemplar de un objeto, basado en la clase.
# definicion de los atributos/propiedades

class Auto:
    # PROPIEDADES / Atributos
    def __init__(self, marca, modelo, color, anio, estado, motorPrendido):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.estado = estado
        self.motorPrendido = motorPrendido
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
    def getEstado(self):
        return self.estado
    def getMotorPrendido(self):
        return self.motorPrendido
    
    def mostrarAuto(self):
        print("Marca: " + self.getMarca())
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()}')
        print(f'Anio: {self.getAnio()}')
        print(f'Estado: {self.getEstado()}')
        print(f'Estado Motor: {self.getMotorPrendido()}')

    def repararAuto(self):
        if(self.estado == "Daniado"):
            print("Ya lo estoy arreglando")
            self.estado = "Funcionando"
            print("Ya funciona")
        else:
            print("No hace falta arregarlo")
    
    def modificarEstadoMotor(self):
        if(self.motorPrendido):
            print("Esta prendido, lo apago")
            self.motorPrendido = False
            print("Lo apague")
        else:
            print("Esta apagado, lo prendo")
            self.motorPrendido = True
            print("ya este prendido")

auto1 = Auto("Toyota", "Prius", "Rojo", "2020", "Funcionando", False)
auto2 = Auto("Peugeot", "208", "Azul", "2022", "Daniado", True)

auto1.modificarEstadoMotor()
auto2.modificarEstadoMotor()