# Ejercicio 3: Diccionario de estudiante
#Dado este diccionario:
#estudiante = {
#"nombre": "Ana",
#"edad": 20,
#"materias": ["Matemática", "Historia"]
#}
#1- Mostrá el nombre y la edad
#2- Agregá una materia nueva a la lista materias
#3- Mostrá cuántas materias cursa con len()
#El objetivo es obtener acceso al diccionario, lista dentro de diccionario y aprender .get() y len()

estudiantes = {
"nombre": "Ana",
"edad": "20",
"materias": ["Matematica", "Historia"]
 }

print("nombre:", estudiantes["nombre"])
print("edad:", estudiantes["edad"])

estudiantes["materias"].append("Fisica")

print("Tu diccionario quedo de la siguiente manera: ", estudiantes)

cantidad_materias = len(estudiantes["mateiras"])

print("la cantidad de materias que cursa es: ", cantidad_materias)