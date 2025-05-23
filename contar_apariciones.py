# Ejercicio 2: Contar apariciones
#Dada la lista:
#colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
#1- Mostrá cuántas veces aparece “rojo” usando .count().
#2- Reemplazá el primer “verde” por “amarillo”
#3- Mostrá la lista final
#El objetivo es usar el método .count(), acceso por índice, asignación de valor

colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

cantidad_rojo = colores.count("rojo")

print("la cantidad de veces que se repite el color rojo es:  ", cantidad_rojo)

indice_primer_verde = colores.index("verde")

colores[indice_primer_verde] = "AMARIYOU"

print("la lista de colores es: ", colores)
