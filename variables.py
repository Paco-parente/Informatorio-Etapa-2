# variable_global = 10

# def prueba():
#  print(variable_global)

# prueba()
# print(variable_global)

contador = 0
contador = 10

def prueba():
  global contador
  contador = 20
  print(contador)


prueba()
print(contador)


resultado = 0
resultado = 10

def prueba(num1, num2):
  #global resultado sin utiluzar la variable global. 
  resultado = 20
  print(f"Desde Adentro: {resultado}")


prueba(10, 20)
print(f"Desde Afuera: {resultado}")




def prueba(num1, num2):
  global resultado  #aqui lo utilizamos con la variable global
  resultado = 20
  print(f"Desde Adentro: {resultado}")


prueba(10, 20)
print(f"Desde Afuera: {resultado}")



def suma(num1, num2, num3):
  return num1 + num2 + num3

resultado = suma(23, 11, 12)

print(f"el resultado es: {resultado}")

# aqui empiezan a entrar en juego los ARGS:
#los ARGS nos permiten pasar a una funcion un numero variable/indeterminado de argumentos posicionales..


def suma(*numeros): #para definir un parametro variable debe llevar siempre el *
    print(numeros)   
    print(type(numeros))

    resultado = 0 
    for num in  numeros:
         resultado += num
    return resultado 

resultado = suma(22,33) #aca le podemos pasar la cantidad de valores que querramos.
print(f"el resultado es: {resultado}")


def suma(*args): #para definir un parametro variable debe llevar siempre el *
    print(args)   
    print(type(args))

    return sum(args)

resultado = suma(22,33, 21) #aca le podemos pasar la cantidad de valores que querramos.
print(f"el resultado es: {resultado}")


# *kwargs: permiten pasar a una funcion unn numero variable/indeterminado de argumentos
#con nombre (clave-valor)

def ver_persona(**kwargs):
   print(kwargs)
   print(type(kwargs))

   for clave, valor in kwargs.items():
      print(f"clave: {clave}, Valor: {valor}")

ver_persona (nombre= "Juan", edad= 25, ciudad= "resistencia", apodo= "juancho",)


# primero se debe pasar todos los ideterminados posisionales,
# luego los  determinados posicionales,
# luegos los nombrados determinados
#ultimo nombrados indeterminados
def mostrar_info(*args1, nombre1, edad=0, **kwargs1):
  print(f"posicionales indeterminados: {args1}")
  print(f"posicionales determinado: {nombre1}")
  print(f"Nombrados determinados: {edad}")
  print(f"Nombrados indeterminados: {kwargs1} ")

mostrar_info(50, True, "algo", nombre1="pablo", edad= 28, ciudad="resis")
