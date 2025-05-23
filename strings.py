print ("### SRTRINGS ###")


nombre = "Andres"
edad = 34
saludo = "hola me llamo {} y tengo {} años".format(nombre, edad)

print (saludo)

saludo = f"hola me llamo {nombre} y tengo {edad} años"
print(saludo)

a= 25
b= 9
saludo = f"hola me llamo {nombre} y tengo {a+b} años"

print (saludo)

print ("###### OPERACIONES CON STRINGS#####" )

cadena1= "Hola"
cadena2= "info"

cadena_concatenada = cadena1 + "  " + cadena2
print (cadena_concatenada)


cadena_repetida = cadena2 * 3
print (cadena_repetida)


cadena = "Hola Mundo soy tu padre"
print (cadena)
longitud = len (cadena)

print(longitud)

subcadena = cadena [0:6]
print (subcadena)

cadena_invertida = cadena [::-1]
print (cadena_invertida)



cadena_mayusc = cadena.upper()

print (cadena_mayusc)

cadena_minusc = cadena_mayusc.lower()
print(cadena_minusc + " " + cadena_mayusc + " " + cadena_invertida ) 

cadena_capitalize = cadena_minusc.capitalize()
print(cadena_capitalize)

cadena_reemplazo = cadena.replace("Hola", "nadie")
print (cadena_reemplazo)