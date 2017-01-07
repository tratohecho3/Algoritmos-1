'''
PRELABORATORIO Nº 4

Prelab4ejercicio1.py



DESCRIPCION: Algoritmo que recibe 10 enteros, los coloca en un arreglo /
			 y posteriormente calcula su suma.
	

Autores: 

	12-11499 - Chaparro Orlando
	13-10299 - Colina Cesar

 Ultima modificacion: 06/10/2016'''


	
# VARIABLES:

#	N: int // Cantidad de enteros que el usuario desea ingresar al arreglo A
#	A: array // Arreglo de enteros ingresados por el usuario
#	sumaFinal: int // Valor de la suma de los elementos del arreglo A


# VALORES INICIALES:


N = int(input("Indique el valor de N: "))

A = [ int(input("A[" + str(i) + "] = ")) for i in range(N) ]

sumaFinal = 0


#PRECONDICION:


assert(N < 11 and N > 0 and len(A) > 0)


# CALCULOS:


for i in A:
	sumaFinal = sumaFinal + i

# POSTCONDICION:


assert( sumaFinal == sum(i for i in A))


# VALORES FINALES:


print("La suma de los elementos ingresados al arreglo es: " + str(sumaFinal))

