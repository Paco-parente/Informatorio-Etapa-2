# ------------------------------------------------------------------------------
# Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:

# Almacenar los números ingresados en una lista.

# Calcular la suma de todos los números pares.

# Contar cuántos números impares se ingresaron.

# Mostrar por pantalla:

# La lista completa de números ingresados.

# La cantidad de los números pares.

# La cantidad de números impares



numeros = []

cantidad_pares = 0
cantidad_impares = 0

for i in range (10):
     num = int(input("ingrese un numero"))
     numeros.append(num)

     

for x in numeros : 
     if x % 2 == 0 :   
          cantidad_pares += 1
     else: 
          cantidad_impares += 1





print ("la lista es:", numeros)
print ("la cantidad de numeros pares es:", cantidad_pares)
print ("la cantidad de numeros impares es:", cantidad_impares)
