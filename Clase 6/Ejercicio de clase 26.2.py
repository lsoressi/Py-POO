# Enunciado
# Cierta empresa requiere una aplicación informática  para administrar los datos de su personal, del
# cual se conoce:

# - número de DNI
# - nombre
# - apellido 
# - año de ingreso.

# Existen dos categorías de empleados:-
# - con salario fijo
# - a comisión.

# Los empleados a comisión tienen
# - un salario mínimo, 
# - un número de clientes captados
# - un monto a cobrar por cada cliente captado.
# El salario = clientes captados * monto por cliente

# Si el salario obtenido por los clientes
# captados no llega a cubrir el salario mínimo, cobrará
# el salario mínimo. 

# Los empleados con salario fijo tienen un sueldo básico y un porcentaje adicional
# en función del número de años que llevan la empresa: 
# • Menos de 2 años: Nada
# • De 2 a 5 años: 5% más.
# • Más de 5 años: 10% más.

# Basado en el enunciado descripto, realizá:

# A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
# B) La implementación del método mostrarSalarios que imprima por consola el nombre
# completo de cada empleado junto a su salario.
# C) La implementación del método empleadoConMasClientes que devuelva al empleado con 
# mayor cantidad de clientes captados (se supone único).

# creen 10 empleados


from enum import Enum

class TipoContrato(Enum):
    COMI = "Comision"
    FIJO = "Fijo"

class Antiguedad(Enum):
    CAT1 = "Menos de 2 anios"
    CAT2 = "De 2 a 5 anios"
    CAT3 = "Mas de 5 anios"


class Empleado:
    def __init__(self, nombre, apellido, dni, anioIngreso, tipoContrato):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.anioIngreso = anioIngreso
        self.tipoContrato = tipoContrato

        def mostrarSalario(self):
            pass




class EmpleadoFijo(Empleado):
    def __init__(
        self, 
        nombre, 
        apellido, 
        dni, 
        anioIngreso,
        tipoContrato,
        salarioBasico,
        antiguedad
                ):
        super().__init__(nombre, apellido, dni, anioIngreso, tipoContrato)
        self.salarioBasico = salarioBasico
        self.antiguedad = antiguedad


    def mostrarSalario(self):
        self.antiguedad = 2024 - self.anioIngreso

        if self.antiguedad < 2:
            montoSalario = self.salarioBasico
        elif self.antiguedad >= 2 and self.antiguedad < 5:
            montoSalario = (self.salarioBasico + (self.salarioBasico * 0.05))
        else:
            montoSalario = self.salarioBasico + (self.salarioBasico * 0.1)
        return print(f'El salario de {self.nombre} {self.apellido} es {montoSalario}')



        #Los empleados con salario fijo
#tienen un sueldo básico y un porcentaje adicional
#en función del número de años que llevan la empresa: 
#• Menos de 2 años: Nada
#• De 2 a 5 años: 5% más.
# Más de 5 años: 10% más.


class EmpleadoComision(Empleado):
    def __init__(
        self, 
        nombre, 
        apellido, 
        dni, 
        anioIngreso,
        tipoContrato,
        salarioMinimo,
        clientesCaptados,
        montoPorClientes
        ):
        super().__init__(nombre, apellido, dni, anioIngreso, tipoContrato)  
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorClientes = montoPorClientes

    def mostrarSalario(self):
        montoSalario = self.clientesCaptados * self.montoPorClientes
        
        if (montoSalario < self.salarioMinimo):
            return print(f'El salario de {self.nombre} {self.apellido} es {self.salarioMinimo}')        
        else:
            return print(f'El salario de {self.nombre} {self.apellido} es {montoSalario}')
        

def empleadoConMasClientes(empleados):
    max_Clientes = 0
    for empleado in empleados:
        if empleado.tipoContrato == "Comision":
            if empleado.clientesCaptados > max_Clientes:
                max_Clientes = empleado.clientesCaptados
                empleado_Con_Mas_Clientes = empleado
    return print(f'El empleado con mas clientes captados es {empleado_Con_Mas_Clientes.nombre} {empleado_Con_Mas_Clientes.apellido} con {max_Clientes} clientes')


def mostrarSalarios(empleados):
    for empleado in empleados:
        empleado.mostrarSalario()



empleados = [
    EmpleadoFijo('Guillermo', 'lalo','12345678', 2014, TipoContrato.FIJO.value, 30000, 0),
    EmpleadoFijo('Julian','Pixel','14344678', 2020, TipoContrato.FIJO.value, 30000, 3),
    EmpleadoFijo('Agustina', 'Nunez','22345678',  2022, TipoContrato.FIJO.value, 30000, 5),
    EmpleadoFijo('Ignacio', 'Gutierrez', '13345678', 2020, TipoContrato.FIJO.value, 30000, 10),
    EmpleadoFijo('Luciana',  'Zapata', '13355678', 2023, TipoContrato.FIJO.value, 30000, 4),
    EmpleadoComision('Guido', 'Pasciucco', '23456789', 2012, TipoContrato.COMI.value, 20000, 30, 1500),    
    EmpleadoComision('Ezequiel', 'Remus', '24456789', 2014, TipoContrato.COMI.value, 20000, 2, 1500),    
    EmpleadoComision('Ana', 'Gomez', '24456489', 2014, TipoContrato.COMI.value, 20000, 8, 1500),    
    EmpleadoComision('Ana2', 'Gomez', '22456789', 2021, TipoContrato.COMI.value, 20000, 28, 1500),    
    EmpleadoComision('Ana3', 'Gomez', '23432789', 2018, TipoContrato.COMI.value, 20000, 45, 1500),
    
    ]

mostrarSalarios(empleados)
empleadoConMasClientes(empleados)

                



