import sys

"""
# Lab05Ejercicio3.py


# DESCRIPCION: 

Es un algoritmo que retorna una secuencia dado un numero n y luego proceder hacer los calculos necesarios para agregar los resultados a la lista.

si el numero es par, el siguiente agregar sera el numero // 2 y si el numero es impar el siguiente agregar sera el (numero * 3) + 1

# Versión de: 

	Cesar Colina 13-10299
	


# Ultima modificacion: 18/10/2016





# CONSTANTES:






# VARIABLES:

numero: int// numero que introduce el usuario
lista: lista // lista donde se almacenan los resultados
contador: int // contador
x: int // variable auxiliar

"""


# Valores iniciales:




lista = []
contador = 0
x = 0



# Precondicion: 
while True:
	try:
		numero = int(input("Introduce un numero natural"))
		assert(numero > 4)
		break
	except:
		print("Ha introducido un valor incorrecto")
		print("Debe introducir al sistema un numero natural mayor a tres (4)")

#Calculos


lista.append(numero)

while True:
	if lista[contador] == 4:
		break
	if lista[contador] % 2 == 0:
		x = int(lista[contador] / 2)
		lista.append(x)
	elif lista[contador] % 2 == 1:
		x = (lista[contador] * 3) + 1
		lista.append(x)
	contador = contador + 1
	print("\n",lista)

	print("la longitud de la lista en esta iteracion es", len(lista))

	print("El valor de x en esta iteracion es", x )






# Postcondicion: 
try:
	assert(len(lista) >= 2 and lista[-1] == 4)


except:
	print("Hubo un error en los calculos")
	print("El resultado de la operacion no ha podido ser realizada")
	print("Intente de nuevo")
	sys.exit()

