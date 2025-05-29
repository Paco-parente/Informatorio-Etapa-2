 #se definen con llaves {} y estan compuestos por pares (clave-valor / key-value)
#las claves son unicas, y los valores pueden ser cualquier tipo de datos, 
# incluso otros diccionarios
#son desordenados. (sus elementos no tienen indices) 
# son mutables (podemos agregar, eliminar, modificar etc)

estudiante = {
    "nombre": "Ana",
    "edad": 23,
    "curso": "Matematicas",
}

print(f"Conjunto diccionario: {estudiante}, {type(estudiante)} ")

print(f"Conjunto diccionario: {estudiante["edad"]}")

estudiante["carrera"] = "ing"

print(f"estudiante: {estudiante}")

del estudiante["carrera"]
print(f"estudiante: {estudiante}")

print(f"Claves (keys) del diccionario: {list(estudiante.keys())}")
print(f"Valores (values) del diccionario: {list(estudiante.values())}")

estudiante_dos = {
    "nombre": "Juan",
    "edad": 23,
    "curso": {
        "nombre": "programacion web",
        "tags": ["PW", "Programacion", "Web", "Python", "Django"] 
    }
}

print(f"Estudiante_dos: {estudiante_dos['curso']["nombre"]}")
print(f"Estudiante_dos: {estudiante_dos['curso']["nombre"]}")