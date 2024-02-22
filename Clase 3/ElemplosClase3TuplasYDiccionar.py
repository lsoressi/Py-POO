
# TUPLAS
# Es una coleccion que no se puede modificar e inmutable, la listas si son mutables

preposiciones = (
        "A",
        "Ante",
        "Bajo",
        "Con",
        "Contra"
    )

print(preposiciones.count("Bajo"))

# me indica la posicion del elemento
print(preposiciones.index("Bajo"))

# DICCIONARIO son dinamicos pueden mutar
# objetos - entidades con caracteristicas

# KEY  -  VALUE

persona = {
    #Key                Value       Key+Value=ITEM
    "nombre"         : "Juan",
    "apellido"       : "Gomez",
    "edad"           : 23,  
    "altura"         : 1.80,
    "promedioNotas"  : [9,6,8],
    "esEstudiante"   : False
}
print(persona["nombre"])
print(persona["promedioNotas"])

#Get
resultado = persona.get("nombre")
print(resultado)


print(persona.keys())
print(persona.values())
print(persona.items())

# persona.pop("promedioNotas") (borra un solo item)
print(persona.items())

#clear borra todos los items
persona.clear()
print(persona.items())