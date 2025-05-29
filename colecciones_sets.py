 #Se definen con llaves pueden contener cualquier tipo de elemento
#no permite otras listas, tampoco diccionarios. si tuplas
# son desordenados es decir NO tienen indice y son mutables ( se pueden modificar)
# no pueden contener elementos duplicados

colores_set = { "rojo", "azul", "verde", ("algo", "algo")}
print(f"conjunto set: {colores_set}, {type(colores_set)}")

#print (f"intento acceder al primer elemento:{colores_set[0]}) # no se puede acceder con 
# indices porque no tienen (son desordenados)

colores_set.add("amarisho")
print(f"set luego del add: {colores_set}")

colores_set.add("amarisho")
print(f"set luego del add: {colores_set}")

colores_set.remove("verde")
print(f"set luego del remove: {colores_set}")

colores_set.discard("verde")
print(f"set luego del discard: {colores_set}")

elemento_eliminado = colores_set.pop()
print(f"elemnto eliminado: {elemento_eliminado}")
print(f"set luego del pop: {colores_set}")

colores_set.clear()
print(f"Set luego del clear: {colores_set}")

colores_set = { "rojo", "azul", "verde", }
print(f"el color 'rojo' esta en el set?: {"rojo" in colores_set}")

print(f"el color 'violeta' esta en el set?: {"violeta" in colores_set}")





lista_con_duplicados = [1, 1, 2, 4, 9, 5, 9, 6, 7, 8, 0]

lista_sin_duplicados = list(set(lista_con_duplicados))

print(f"lista sin duplicados: {lista_sin_duplicados}")