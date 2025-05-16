//Se desea realizar un programa que que permita el ingreso de 4 numeros y de ellos sacar el mayor, y la suma de todos.
//Tambien tiene que tener la caracteristica de pudeer repetir la operacion x veces
//Este programa tiene que tener un menu donde la opcion 1 sea realizar la operacion y  99 para salir
//el programa se puede ejecutar las veces que se quiera 
//otra opcion que se pide es. Opcion 2. la opcion 2 debe permitir restar todos los numeros que se ingrese y mostrame el menor de todos

//Ademas se requiere una mejora que permita que el usuario le diga al programa cuantos numeros puede ingresar 

algoritmo Ejercicio
	Definir op,mayorc,sumac,ingreso_por_teclado,cantidad Como Entero
	op=0
	
	Escribir "--Menu--"
	Escribir "Para iniciar ingrese  1"
	Escribir " Para salir ingrese 99"
	Leer op
	
	
	Mientras op<> 99  Hacer 
		
		Segun op Hacer
			1:
				Escribir "para sumar ingrese 2"
				Escribir "para restar ingrese 3"
				Escribir "para salir ingrese 99"
				leer op
				segun op Hacer
					2: 
						Escribir "ingrese cuantos numeros va a sumar"
						leer cantidad
						mayorn=-10 
						csuma=0
						

						para i desde 1 hasta cantidad Hacer
							Leer ingreso_por_teclado
							Si ingreso_por_teclado > mayorn Entonces
								mayorn=ingreso_por_teclado
								
							SiNo
								
							Fin Si
							csuma=csuma+ingreso_por_teclado
						FinPara
						Escribir "el mayor es" mayorn
						Escribir "la suma de los enteros es" csuma
					3:					
						Escribir "ingrese cuantos numeros va a restar"
						leer cantidad
						mayorn=1000
						csuma=0
						
						
						para i desde 1 hasta cantidad Hacer
							Leer ingreso_por_teclado
							Si ingreso_por_teclado < mayorn Entonces
								mayorn=ingreso_por_teclado
								
							SiNo
								
							Fin Si
							csuma=csuma-ingreso_por_teclado
						FinPara
						Escribir "el menor es" mayorn
						Escribir "la resta de los enteros es" csuma
						
						
				FinSegun
				
			
			De Otro Modo:
				Escribir "opcion incorrecta mongolo!"
		Fin Segun
		
		
		
		
		
		
		
		Escribir "--Menu--"
		Escribir "Para iniciar Ingrese 1"
		Escribir " Para salir ingrese 99"
		Leer op
		
	FinMientras
	escribir "chau nos vemos!"
	
FinAlgoritmo


