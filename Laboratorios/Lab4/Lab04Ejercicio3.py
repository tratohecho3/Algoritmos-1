'''
LABORATORIO Nº 4

Lab4Ejercicio3.py



DESCRIPCION: algoritmo que calcula la nota final de cada estudiante y los promedios de los parciales


Autores: 

	14-10192 - Gustavo Castellanos
	13-10299 - Colina Cesar

 Ultima modificacion: 11/10/2016'''


# CONSTANTES: 

#	nombre: str // Cadena que indica el nombre del estudiante ingresado

	
# VARIABLES:

#   N: int // Cantidad de estudiantes que seran ingresados al algoritmo

#	grupo: array // Arreglo que almacena los datos de cada estudiante

#   promedio1 : float // promedio del primer parcial

#   promedio2 : float // promedio del segundo parcial

#   total : int // variable que almacena la suma de los parciales para el i-esimo estudiante


# VALORES INICIALES:

class Estudiante:
	nombre = ' '
	indiceAcademico = 0
	parcial1 = 0
	parcial2 = 0

promedio1 = 0
promedio2 = 0 
N = int(input("Introduzca la cantidad de estudiantes: "))


# PRECONDICION:

assert(N > 0)


# CALCULOS:

grupo = [ Estudiante () for x in range(N) ]

for i in range(0, N):
	grupo[i].nombre = input("Introduzca el nombre del estudiante: ")
	grupo[i].parcial1 = int(input("Introduzca su nota del primer parcial"))
	assert(grupo[i].parcial1 <= 50 and grupo[i].parcial1 >= 0)
	grupo[i].parcial2 = int(input("Introduzca su nota del segundo parcial"))
	assert(grupo[i].parcial2 <= 50 and grupo[i].parcial2 >= 0)
	

for i in range (0, len(grupo)): 
	promedio1 += grupo[i].parcial1 
	promedio2 += grupo[i].parcial2 
	total = grupo[i].parcial1 + grupo[i].parcial2

	if total < 30:
		total = 1
	elif total >= 30 and total < 50:
		total = 2
	elif total >= 50 and total < 70:
		total = 3
	elif total >= 70 and total <85:
		total = 4
	else:
		total = 5
	grupo[i].IndiceAcademico = total

	
promedio1 = promedio1 / N
promedio2= promedio2 / N




# POSTCONDICION:
assert(promedio1 >= 0 and promedio2 >= 0)


# VALORES DE SALIDA:

for i in range(0, N):
	print("Estudiante: " + grupo[i].nombre + ". Indice: " + str(grupo[i].IndiceAcademico))

print("El promedio del parcial 1 fue ", promedio1, " y el promedio del parcial 2 fue ",promedio2 )