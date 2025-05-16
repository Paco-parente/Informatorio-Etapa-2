
//Se desea realizar un programa que que permita el ingreso de 4 numeros y de ellos sacar el mayor, 



Algoritmo sin_titulo
	Definir ingreso_por_teclado,mayorn,csuma,i  Como Entero
	Escribir "Ingrese 4  numeros enteros"
	mayorn=-10 
	csuma=0
	para i desde 1 hasta 4 Hacer
		Leer ingreso_por_teclado
		Si ingreso_por_teclado > mayorn Entonces
			mayorn=ingreso_por_teclado
			
		SiNo
			
		Fin Si
		//csuma=csuma+ingreso_por_teclado
    FinPara
	
	Escribir "el numero mayor es " mayorn
FinAlgoritmo


