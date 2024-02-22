#defino la funcion
def funcionejercicio1(num1, num2, selector):
    if (selector==1):
        return (num1 + num2)

    elif (selector==2):
        return (num1 * num2) 
    
    else:
       return (f'La operacion es incorrecta')
        

resultado= funcionejercicio1(5, 10, 4)  
print(resultado)
    