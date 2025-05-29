# def saludo(nombre):
#     print(F"hola {nombre}")

# saludo("andres")



# notas = [10, 5, 7, 8]
# suma = 0

# for nota in notas:
#     suma += nota

# promedio = suma / len(notas)

# print(f"suma: {suma}")
# print(f"notas: {len(notas)}")
# print(f"Promedio: {promedio}")


def promedio(notas):
    return sum(notas) / len(notas)

promedio_pablo = promedio([5, 6, 8, 9])
promedio_juan = promedio([10, 6, 3, 2])

print(f"promedio_pablo fue :{promedio_pablo}")
print(f"promedio_juan fue :{promedio_juan}")
