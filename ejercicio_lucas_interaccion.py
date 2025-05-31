

"""
Se desea realizar un programa que permita seleccionar entre 3 opciones.
1) realizar la suma de 2 numeros
2) ingresar a y realizar ese numero al cuadrado
3) Verificar si ese numero es par o impar
debera permitir el ingreso de valores por teclado

"""


print("INGRESE QUE OPCION DESEA REALIZAR")
print("Para sumar 2 numeros ingrese 1")
print("Para elevar al Cuadrado un numero ingrese 2")
print("Para verificar si un numero es par o impar ingrese 3")
opcion = int(input("Ingrese su Opcion 1, 2 o 3: "))
if opcion == 1:
     num1 = int(input("ingrse el primer numero a sumar: "))
     num2 = int(input("ingrse el segundo numero a sumar: "))

     resultado = num1 + num2
     print(f"el resultado de tu suma es: {resultado}")

elif opcion == 2:
     num1 = int(input("ingrese el numero que desea elevar al cuadrado: "))
     cuadrado = num1 ** num1
     print(f"el resultado del cuadrado de {num1} es: {cuadrado}")

elif opcion == 3:
     num1 = int(input("ingrese el numero que desea verificar: "))
     if num1 % 2 == 0:
        print(f"el numero {num1} es par.")
     else:
        print(f"el numero {num1} es impar")

else:
     print("opcion no valida. ingrese 1, 2, o 3.")