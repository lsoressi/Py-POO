# Colecciones de datos (facilita el manejo de la info) / tipos complejos

#[]Listas 

diasSemana = [      #posiciones     #elementos
    "Lunes",        #0              #1
    "Martes",       #1              #2
    "Miercoles",    #2              #3
    "Jueves",       #3              #4
    "Viernes",      #4              #5
    "Sabado",       #5              #6
    "Domingo"       #6              #7
    ]

meses = [
    "Enero",
    "Febrero",
    "Marzo"
    ]

#print(diasSemana)

# acceder individualmente a un elemento
#diasSemana[2]
#print(diasSemana[2])

# modificar individualmente un elemento
#diasSemana[2] = "Cualquier cosas"
#print(diasSemana)

# agregar elemento al final de la lista
#Ahora la lista tiene 7 posiciones y 8 elementos por el append
diasSemana.append("Feriado")


# añade una lista a otra preexistente
diasSemana.extend(meses)

# agregar un elemento en un index expecifico
diasSemana.insert(0, "Feriadoooo")

# eliminar un elemento el ultimo o el aclarado en index
diasSemana.pop(5)

# elimina elemento si consigue elemento especifico, tiene que coincidir exact el nombre
diasSemana.remove("Feriado")





# por cada dia de la semana...
for dia in diasSemana:
    # hace un print de ese dia
    print(dia)


listNums = [4, 2, 6, 5, 9, 34, 85, 254, 1234, 65, 43 ]

#sort ordena los numeros de menor a mayor
listNums.sort()

listNums.reverse()

for numero in listNums:
    print(numero)

    