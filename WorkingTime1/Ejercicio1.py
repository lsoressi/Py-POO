contador = 0
acumulador = 0
while contador <= 100:
    contador +=1    
    print('Valor del Contador', contador)
    print('Valor del Acumulador', acumulador)

    acumulador = (contador + acumulador)  
    print('acumulador', acumulador)
