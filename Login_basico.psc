Algoritmo login
	Definir  user, password Como Cadena 
	Definir intentos Como Entero
	intentos = 3
	
	
	
	Mientras intentos > 0 Hacer
		Escribir "Ingrese su Usuario"
		Leer Usuario
		Escribir "Ingrese su Contrase�a"
		Leer Contrasenia
		
		Si Usuario =  "paco" y Contrasenia = "paco123" Entonces
			Escribir "Login exitoso. Bienbenido!" Usuario
			intentos =  0
		SiNo
			Escribir "Usuario o Contrae�a incorrecta" 
			intentos = intentos - 1 
			
		Fin Si
	Fin Mientras
	
	
FinAlgoritmo
