

"""
Se desea realizar un programa que permita seleccionar entre 3 opciones.
1) realizar la suma de 2 numeros
2) ingresar a y realizar ese numero al cuadrado
3) Verificar si ese numero es par o impar
debera permitir el ingreso de valores por teclado

"""

while True:
    
    while True:
        print("\nINGRESE QUÉ OPCIÓN DESEA REALIZAR")
        print("1) Sumar 2 números")
        print("2) Elevar un número al cuadrado")
        print("3) Verificar si un número es par o impar")

        try:
            opcion = int(input("Ingrese su opción (1, 2 o 3): "))
            if opcion in [1, 2, 3]:
                break  
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Tenes que ingresa un número. Intenta de nuevo.")

    
    if opcion == 1:
        num1 = int(input("Ingrese el primer número a sumar: "))
        num2 = int(input("Ingrese el segundo número a sumar: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")

    elif opcion == 2:
        num1 = int(input("Ingrese el número que desea elevar al cuadrado: "))
        cuadrado = num1 ** 2
        print(f"El cuadrado de {num1} es: {cuadrado}")

    elif opcion == 3:
        num1 = int(input("Ingrese el número que desea verificar: "))
        if num1 % 2 == 0:
            print(f"El número {num1} es par.")
        else:
            print(f"El número {num1} es impar.")

    
    while True:
        repetir = input("¿Querés realizar otra operación? (s/n): ").strip().lower()
        if repetir == 's':
            break  
        elif repetir == 'n':
            print("Bueno, nos vemos.")
            exit()
        else:
            print("Entrada no válida. Ingresá 's' para sí o 'n' para no.")