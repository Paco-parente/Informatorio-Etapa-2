"""
un modulo es un archivo con contiene definiciones y funciones

Ejercicio con Funciones 🧩
1- Generador de hechizos aleatorios {
Escribe una función que combine aleatoriamente un prefijo y sufijo de listas dadas y cree un hechizo mágico (Usar módulo random)

"""

import random

def generar_hechizo():

   prefijos = ['Abra', 'Alakaza', 'Zendo', 'Foco', 'Magi']
   sufijos = ['cadabra', 'lumos', 'mora', 'nox', 'flama']

   prefijo_aleatorio = random.choice(prefijos)
   sufijo_aleatorio = random.choice(sufijos)
   hechizo = f"{prefijo_aleatorio} - {sufijo_aleatorio} "

   return hechizo

print(generar_hechizo())