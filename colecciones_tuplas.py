#Se definen con parentesis pueden contener cualquier tipo de elemento
#incluso otras tuplas o colecciones
# son ordenadas es decir tienen indice y son inmutables (no se pueden modificar)

numeros_tupla = (1, 2, 3, 4, 5)
print(f" Numeros (tupla): {numeros_tupla}, tipo: {type(numeros_tupla)}")


#1er elemento
print(numeros_tupla[0])

#ultimo elemento
print(numeros_tupla[-1])


#slicing subtuplas
#separador es ":" lado izquierdo inicia lado derecho termina
print(f"primeros 3 elementos {numeros_tupla[:3]}")
print(f"elementos del medio elementos {numeros_tupla[-2:]}")    
print(f"primeros elementos del medio {numeros_tupla[1:-1]}")

print(f"la lingitud de la lista es {len(numeros_tupla)}")

#desempaquetado de tuplas 

a, b, c, d, e = numeros_tupla

print(f"desempaquetado: a={a} b={b}   c={c} d={d} e={e} ")

primer_elemento, *resto_elementos = numeros_tupla

print(f" Desempaquetado: Primero ={primer_elemento} \nResto={resto_elementos}")

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)


print(f"Matriz: {matriz}")
print(f"elemento [2][2]: {matriz[1][1]}")