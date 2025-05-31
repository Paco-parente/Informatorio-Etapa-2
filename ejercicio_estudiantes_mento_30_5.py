""" Sistema de calificaciones de estudiantes {
Creá un programa que guarde las notas de varios estudiantes en un diccionario.
Luego, crea funciones para:
A- Agregar estudiante con sus notas.
B- Calcular el promedio de un estudiante
C- Mostrar los estudiantes aprobados (promedio >= 6)"""


estudiantes = {
    'Ana': [9, 8, 10],
    'Luis': [4, 6, 5],
    'Carlos': [10, 10, 9]
}

def agregar_estudiante(nombre, notas, base):
    base[nombre] = notas

agregar_estudiante("Elias", [10, 10, 10], estudiantes)

print(estudiantes)

def promedio_estudiante(base, nombre):
    notas = base[nombre]
    
    return sum(notas) / len(notas)

print("el promedio del estudiante es:", promedio_estudiante(estudiantes,"Ana"))

def estudiantes_aprobados(base):
    aprobados = []
    for nombre, notas in base.items():
        promedio = sum(notas) / len(notas)
        if promedio >= 6:
            aprobados.append(nombre)

    return aprobados
    
print(estudiantes_aprobados(estudiantes))