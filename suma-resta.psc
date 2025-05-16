//Se desea realizar un programa que que permita el ingreso de 4 numeros y de ellos sacar el mayor, y la suma de todos.
//Tambien tiene que tener la caracteristica de pudeer repetir la operacion x veces
//Este programa tiene que tener un menu donde la opcion 1 sea realizar la operacion y  99 para salir
//el programa se puede ejecutar las veces que se quiera 
//otra opcion que se pide es. Opcion 2. la opcion 2 debe permitir restar todos los numeros que se ingrese

//Ademas se requiere una mejora que permita que el usuario le diga al programa cuantos numeros puede ingresar 

algoritmo Ejercicio
	Definir op,mayorc,sumac,ingreso_por_teclado,intentos,cuantos Como Entero
	op=0
	intentos=0
	cuantos=0
	
	Escribir "--Menu--"
	Escribir "Para iniciar ingrese  1"
	Escribir "2Para restar los numeros"
	Escribir "3Para sumar otra cantidad de numeros"
	
	Escribir " Para salir ingrese 99"
	Leer op
	
	
	Mientras op<> 99  Hacer 
		
		Segun op Hacer
			1:
		
				mayorn=-10 
				csuma=0
				i=0
				
				
				para i desde 1 hasta 4 Hacer
					Escribir "escribir el numero", i 
					Leer ingreso_por_teclado
					Si ingreso_por_teclado > mayorn Entonces
						mayorn=ingreso_por_teclado
						
					SiNo
						
					Fin Si
					csuma=csuma+ingreso_por_teclado
				FinPara
				Escribir "elayor es" mayorn
				Escribir "la suma de los enteros es" csuma
			2:
				mayorn=-10 
				csuma=0
				i=0
				
				
				para i desde 1 hasta 4 Hacer
					Escribir "escribir el numero", i 
					Leer ingreso_por_teclado
					Si ingreso_por_teclado > mayorn Entonces
						mayorn=ingreso_por_teclado
						
					SiNo
						
					Fin Si
					csuma=csuma-ingreso_por_teclado
				FinPara
				Escribir "elayor es" mayorn
				Escribir "la resta de enteros es:" csuma
				
			3:
				Escribir "Ingresa cuantos numeros queres procesar"
				leer cuantos
				Mientras cuantos > 0  Hacer 
					Leer ingreso_por_teclado
					Si ingreso_por_teclado > mayorn Entonces
						mayorn=ingreso_por_teclado
						
					SiNo
						
					Fin Si
					csuma=csuma+ingreso_por_teclado
					cuantos=cuantos-1
					Escribir "elayor es" mayorn
					
				FinMientras
				Escribir "la suma de los enteros es" csuma
			De Otro Modo:
				Escribir "opcion incorrecta mongolo!"
		Fin Segun
		
		
		
		
		
		
		
		Escribir "Para iniciar ingrese  1"
		Escribir "2Para restar los numeros"
		Escribir "3Para sumar otra cantidad de numeros"
		
		Escribir " Para salir ingrese 99"
		Leer op
		
	FinMientras
	escribir "chau nos vemos!"
	
FinAlgoritmo