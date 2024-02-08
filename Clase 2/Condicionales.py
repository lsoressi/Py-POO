# Entrar al boliche 18 años o mas
# Entrar al matinee entre 13 y 17 años

# 12 años o menos nada
# 13, 14, 15, 16, 17 entran al matinee
# 18 o mas entran al boliche

edad = 15
esSuCumpleanios = True

print('inicio')
if (edad >= 18 ):
    print (f'Tenes {edad} anios, podes entrar al boliche')
    if(esSuCumpleanios):
        print(f'Feliz Cumple te ganaste un trago')
elif (edad >= 13 and edad <=17):
    print (f'Tenes {edad} anios, boliche NO, pero podes entrar a la matinee')
    if(esSuCumpleanios):
        print(f'Feliz Cumple te ganaste una gaseosa')

else:
    print (f'Tenes {edad} anios, NO podes entrar al boliche')

print('fin')