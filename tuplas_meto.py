#una tupla es un tipo de datos que permite ordenar una coleccion ordenada
# e inmutable que no permite modificar elementos ni agregar ni quitar

print("------ TUPLAS ------")

frutas = ("manzana", "naranja", "sandia", "cereza", "naranja", "naranja" )
verduras = ("cebolla", "lechuga", "zapallo")


print(f"Frutas (tupla) {frutas}, tipo: {type(frutas)}")

print("Elementos del indice 1", frutas[0])
print("Elementos del indice 2", frutas[1])

print("la longitud de la tupla es:", len(frutas))

print("la fruta naranja aparece,", frutas.count("naranja"))

print("el indice de la sandiaes:", frutas.index("sandia"))

uno, dos, tres, cuatro, cinco, seis = frutas

print("la fruta individual que elegiste es:", uno)


tupla3 = frutas + verduras 

print(f"concatenacion de tuplas: {tupla3}")

