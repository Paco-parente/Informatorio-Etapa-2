# ejercicio 4: blucle para (for)
#consigna
# Pedir al usuario un numero X y mostrar la tabla de multiplicar del 1 al 10 de ese numero.



numero = int(input("Ingrese un numero: \n"))

print(f"--- Tabla de Multiplicar del {numero} --- \n")

for i in range (1,11):
    resultado = numero * i 
    print(f"{numero} x {i} = {resultado}")
