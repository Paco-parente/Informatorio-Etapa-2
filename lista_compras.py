# Ejercicio 1: Gestión de una lista de compras
#Crea una lista vacía llamada lista_comprasLuego:
#1- Agregá 3 productos usando .append()
#2- Mostrá cuántos productos hay con len()
#3- Eliminá el último producto con .pop()
#4- Mostrá la lista actualizada
#El objetivo es aprender .append(), .pop() y .len()

lista_compras = []

lista_compras.append("manzana")
lista_compras.append("sandia")
lista_compras.append("naranja")

print("Esta es tu lista de compras: ",lista_compras)

cantidad_elementos = len(lista_compras)

print("La cantidad de elemntos que hay en tu lista de compra es: ", cantidad_elementos)

elemento_eliminado = lista_compras.pop()

print("El producto eliminado es: ", elemento_eliminado)

print("finalmente tu lista  de compras quedo asi: ", lista_compras)