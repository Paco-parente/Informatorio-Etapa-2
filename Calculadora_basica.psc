Algoritmo Calcula
	
	definir numero1, numero2, resultado Como real
	definir operacion Como Caracter
	
	Escribir "Hola, vamos a calcular"
	Escribir "ingresa los valores"
	Leer numero1
	leer numero2

	escribir "que operacion queres hacer (+,-,/,*) ?"
	leer operacion 
	
	si operacion = "+" Entonces
		resultado = numero1 + numero2 		
		
		 Escribir  "el resultado de la suma es" " " 	resultado
	 SiNo
	 
	
		 si  operacion = "-" entonces
			
			 resultado = numero1 - numero2
			 
			 Escribir "El resultado de la resta es" " " resultado
		 SiNo
			 si operacion = "*"  Entonces
				 resultado = numero1 * numero2
				 Escribir "el resultado del producto es" " " resultado
				 
			 sino 
				 si operacion = "/" 
					 si numero2 <> 0 Entonces
						resultado = numero1 / numero2
						 
						Escribir  "el resultado de la divison es" " " resultado
					SiNo
						Escribir "FATAL ERROR!!- no es posible dividir por 0"
				        
					FinSi
				siNo
					escribir "operacion incorrecta"  " " operacion " " "no es un carcter valido"
					Escribir "ingrese una operacion matematica"
				 FinSi
			 FinSi
		 FinSi
	 
		
FinSi
FinAlgoritmo
