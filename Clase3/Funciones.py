# Fucniones Nativas de python, son las que trae el lenguaje ya con una funcion definida.
# Bloque de codigo que lo puedo reutilizar las veces que quiera
#Funciones aritmeticas, tipos de datos, 

#Como definimos nuestra funcion en python con la palabra reservada def


precio = 140 

#declare y defini mi funcion
def sumar_iva():
    print(precio * 1.21) 

# ejecutarla
sumar_iva()



# ALGORITMO
#1. Entrada de Datos
#2. Procesamiento de Datos cuerpo de la funcion
#3. El retorno de Datos.

#una forma mas dinamica de definir una funcion, colocando un parametro dentro de def
def sumar_iva(precioInicial):   
    print(precioInicial * 1.21) 
    return
# el retorno es la posibilidad de que la funcion nos devuelva un valor.

sumar_iva(4500)
sumar_iva(12600)
sumar_iva(2900)


#La funcion de forma correcta queda asi:

def sumar_iva(precioInicial):   
     return precioInicial * 1.21

print(sumar_iva(4500))
print(sumar_iva(12600))
print(sumar_iva(2900))


def saludar(nombre, apellido, curso):
    saludo = f' Hola {nombre} {apellido}!'
    bienvenida = f' Bienvenido al curso de {curso}'
    return saludo + bienvenida

print(saludar("Pepe", "Martinez", "Python"))
print(saludar ("Tito", "Rodriguez", "Java"))