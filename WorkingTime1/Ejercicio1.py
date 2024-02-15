contador = 1
acumulador = 0
while contador <= 100:    
    print('Valor del Contador', contador)
    print('Valor del Acumulador', acumulador)

    acumulador = (contador + acumulador)  
    print('acumulador', acumulador)
    
    contador +=1