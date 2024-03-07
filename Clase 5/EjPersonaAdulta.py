

class PersonaAdulta:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f' Hola, mi nombre es {self.nombre} y tengo {self.edad} anios')


persona1 = PersonaAdulta ('Luciana', '43 anios')
print(persona1.nombre)
print(persona1.edad)

persona1.saludar()

