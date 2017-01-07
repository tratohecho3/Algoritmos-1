'''
PRELABORATORIO Nº 4

PreLab4Ejercicio3.py



DESCRIPCION: Algortimo que calcula el promedio de notas de los estudiantes
			 ingresados mediante la consola utilizando clases en Python


Autores: 

	12-11499 - Chaparro Orlando
	13-10299 - Colina Cesar

 Ultima modificacion: 09/10/2016'''


# CONSTANTES: 

#	nombre: str // Cadena que indica el nombre del estudiante ingresado

#	edad: int // Edad del estudiante ingresado

#	indiceAcademico: float // Indice del estudiante

	
# VARIABLES:

#   sumaEdad: int // Sumatoria de todas las edades

#	sumaIndice: int // Sumatoria de todos los indices academicos

#   N: int // Cantidad de estudiantes que seran ingresados al algoritmo

#	grupo: array // Arreglo que almacena los datos de cada estudiante

#	promedioIndice: float // Promedio del indice academico de todos los estudiantes

#	promedioEdad: float // Promedio de las edades de todos los estudiantes


# VALORES INICIALES:

class Estudiante:
	nombre = ' '
	edad = 0
	indiceAcademico = 0

sumaEdad = 0 
sumaIndice = 0

N = int(input("Introduzca la cantidad de estudiantes: "))


# PRECONDICION:

assert(N > 0)


# CALCULOS:

grupo = [ Estudiante () for x in range(N) ]

for i in range(0, N):
	grupo[i].nombre = input("Introduzca el nombre del estudiante: ")
	grupo[i].edad = int(input("Introduzca la edad del estudiante: "))
	grupo[i].indiceAcademico = float(input("introduzca el indice academico del estudiante: "))
	

for i in range (0, len(grupo)): 
	sumaEdad += grupo[i].edad
	sumaIndice += grupo[i].indiceAcademico
	
promedioEdad = sumaEdad / N
promedioIndice = sumaIndice / N


# POSTCONDICION:

# assert(True)


# VALORES DE SALIDA:

print("El promedio de notas de los estudiantes ingresados al sistema fue de: " + str(promedioIndice))
print("El promedio de edades de los estudiantes ingresados al sistema fue de: " + str(promedioEdad))


#POSTCONDICION
assert(promedioEdad > 0 and promedioIndice > 0)
#ESTA ERA LA QUE QUERIA PERO ME DA ERROR
#assert(((promedioEdad == sum(grupo[i].edad for i in range(len(grupo)))) / N) and (promedioIndice == ((sum(grupo[i].indiceAcademico for i in range(len(grupo)))) / N )))