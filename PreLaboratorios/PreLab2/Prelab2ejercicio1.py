""" PRELABORATORIO #2
PreLab2ejercicio.py

DESCRIPCION: Implementacion de un Algoritmo en Python para calcular
las raices del polinomio A*(x**2) + B*x +C

Autores:

12-11499 - Chaparro Orlando
13-10299 - Colina Cesar

Ultima modificacion: 22-09-2016

"""




import math 
"""
CONSTANTES

A: int; Valor del coeficiente asociado a la incognita al cuadrado
B: int; Valor del coeficiente	asociado a la incognita
C: int; Valor del termino independiente


VARIABLES

x1 : float; Primera Raiz del polinomio
x2 : float; Segunda Raiz del polinomio

"""
#VALORES INICIALES:

A = 1
B = 5 
C = 6 



#PRECONDICION
assert(A != 0 and (4*A*C) <= (B*B))

#ALGORITMO

x1 = (-B + math.sqrt(B ** 2 - 4*A*C)) / 2*A

x2 = (-B - math.sqrt(B ** 2 - 4*A*C)) / 2*A 


#POSTCONDICION

assert(A * x1 * x1 + B * x1 + C == 0 and A * x2 * x2 + B * x2 + C == 0)

# SALIDA:

print("x1 es: " + str(x1))

print(" ")

print("x2 es: " + str(x2))


