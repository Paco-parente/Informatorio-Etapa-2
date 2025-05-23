#Se definen con [] y pueden contener cualquier tipo de elementos
#incluso otras listas dentro de ellas o cualquier otra coleccion
#son ordenadas (sus elementos tienen indice) el primer elemento siempre es el 0
# y sus elementos son mutables (se pueden eliminar, agregar, quitar )

numeros = [1, 2, 3, 4, 5]

#primer elemento
print(numeros[0])

#ultimo elemnto

print(numeros[-1])

#sublistas (slicing)

#separador es ":" lado izquierdo inicia lado derecho termina
print(f"primeros 3 elementos {numeros[:3]}")
print(f"elementos del medio elementos {numeros[-2:]}")    
print(f"primeros elementos del medio {numeros[1:-1]}")

print(f"la lingitud de la lista es {len(numeros)}")
      


print(f"####### METODOS ########")

print(f"cuantas veces aparece el elemento con valor 3 {numeros.count(3)}")

print(f"cual es el indicie del elemento con valor 3 {numeros.index(3)}")

numeros.append(6)

print(f"lista luego del append {numeros} ")

##como agregar en una ubicacion diferente al final

numeros [0] = 99 
print(f"lista luego del modificar: {numeros} ")

numeros.insert(3, 8)
print(f"lista luego del insert: {numeros} ")

#como borrar un elemento. si no ponemos indicie saca el ultimo

numeros.pop(2)
print(f"lista luego del pop: {numeros} ")

#como borrar un elemento en especifico
numeros.remove(2)
print(f"lista luego del remove {numeros} ")

#como ordenar una lista de menor a mayor

numeros.sort()
print(f"lista luego del sort {numeros} ")

numeros.sort(reverse=True)
print(f"lista luego del sort reverse {numeros} ")


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(f"matriz:{matriz}")
print(f"elemento [2][2]: {matriz[2][2]}")

print(f"Elemento con valor 5 esta en la lista?: {"SI" if 5 in numeros else "NO"}")

