# Crear un algoritmo para calcular la sumatoria de los primeros cien
# números (del 01 al 100) con un ciclo while.
# Guardar el algoritmo en un archivo llamado ejercicio1.py


contador = 0
acumulador = 0
while contador <= 100:
    contador +=1    
    print('Valor del Contador', contador)
    print('Valor del Acumulador', acumulador)

    acumulador = (contador + acumulador)  
    print('acumulador', acumulador)
