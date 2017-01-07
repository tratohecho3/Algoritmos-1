import sys
"""
# Exejercicio1.py


# DESCRIPCION: 

Es un algoritmo que dados los precios de los productos ingresados por el usuario, el programa calcula el promedio

# Versión de: 

	Cesar Colina 13-10299
	



# Ultima modificacion: 25/10/2016





# CONSTANTES:







# VARIABLES:
lista: lista// Lista donde se almacena los precios de los productos
contador: int // contador que nos sirve para iterar
suma: float // variable donde se ira guardando el resultado de la suma
x: float // variable donde el usuario ingresa el precio
promedio: float // variable donde se guarda el promedio de la suma de los precios

"""


# Valores iniciales:
lista = []
cota = 100
contador = 0
suma = 0

#Precondicion:

while contador < cota:
	
	x = float(input("Introduzca los precios de los articulos: "))
	assert(x >= 0)
	if x == 0:
		break
	lista.append(x)
	contador = contador + 1
	
	

#Calculos

for i in lista:
	suma = suma + i


promedio = suma / len(lista)


# Postcondicion: 

assert(suma == sum(x for x in lista) and (promedio== (sum(x for x in lista) / len(lista))) )


 # Salida:

print("El promedio es ",promedio)

