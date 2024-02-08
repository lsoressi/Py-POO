# Matinee entre 13 y 17 años
# 1. edad tiene que ser mayor o igual que 13
# 2. edad tiene que ser menor o igual que 17

edad = 21 
print ((edad >= 13) and (edad <= 17))

# Con el operador AND nos da FALSE (correcto)
# Si uso el operador OR nos da TRUE (Incorrecto)

edad = 21 
print ((edad >= 13) or (edad <= 17))


# AND - INTERSECCION (CONJUNCION)
# V + V = V
# V + F = F
# F + V = F
# F + F = F

# OR - UNION (DISYUNCION)
# V + V = V
# V + F = v
# F + V = v
# F + F = F

edad = 21 
print (edad is not 12)


nombre = "Juan"
apellido = "Perez"
edad = 21 

nombre_entero = nombre + " " + apellido

saludo = f'Hola! Mi nombre es {nombre_entero} y tengo {edad} anios'
print(saludo)
