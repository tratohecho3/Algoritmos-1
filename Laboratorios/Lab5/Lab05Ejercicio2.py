import sys 

"""
# Lab05Ejercicio2.py


# DESCRIPCION: 

Es un algoritmo que 

# Versión de: 

	Cesar Colina 13-10299
	


# Ultima modificacion: 18/10/2016





# CONSTANTES:






# VARIABLES:
lista: lista // lista donde se almacena la secuencia
n: int // cota superior
contador: int // contador para iterar
contador2: int // contador para iterar
x

"""


# Valores iniciales:

lista = []
n = 100
contador = 0
contador2 = 0


# Precondicion: 


while contador2 < n:
	try:
		x = int(input("Introduce un numero no negativo"))
		assert(x > -1)
		if x == 0:
			break
		lista.append(x)
	except:
		print("Ha introducido un valor incorrecto")
		print("Debe introducir al sistema un numero mayor a  -1")


	
#Calculos




while contador <= len(lista) - 2:  
		
	
	if lista[contador] < lista[contador + 1]:
		contador = contador + 1
		if contador > len(lista) - 2:
			print("La secuencia esta ordenada")

	elif lista[contador] > lista[contador + 1]:
		print("La secuencia no esta ordenada")
		break








# Postcondicion: 

try:
	assert(len(lista) > 0)

except:
	print("Hubo un error en los calculos")
	print("El resultado de la operacion no ha podido ser realizada")
	print("Intente de nuevo")
	sys.exit()

