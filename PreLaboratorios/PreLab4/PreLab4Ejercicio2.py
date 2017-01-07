
"""
PRELABORATORIO Nº 4

PreLab4Ejercicio2.py



DESCRIPCION: Algoritmo que permite determinar el ganador en un concurso
			 de hamburguesas. Tenga en cuenta que el numero maximo de 
			 hamburguesas consumidas por jugador pueden ser 9.

Autores: 

	12-11499 - Chaparro Orlando
	13-10299 - Colina Cesar

 Ultima modificacion: 07/10/2016
 
 VARIABLES
 participantes : Arreglo // Lista de todos los participantes
 hamburguesas: Arreglo // Lista de la cantidad de hamburguesas digeridas por cada participante
 aux: int // auxiliar para los calculos
 aux2: str // auxiliar para los calculos


"""

#VALORES INICIALES

participantes = ["Yarima","Jawil","Marco","Miguel","Javier"]

hamburguesas = [int(input("Cuantas hamburguesas se comio " + i + " "))for i in participantes]

#Precondicion

assert(all(i for i in hamburguesas if i >= 0))

#CALCULOS

for i in range(4):
	for x in range(4):
		if hamburguesas[i] <= hamburguesas[i + 1]:
			aux = hamburguesas[i]
			hamburguesas[i] = hamburguesas[i + 1]
			hamburguesas[i + 1] = aux
			aux2 = participantes[x]
			participantes[x] = participantes[x + 1]
			participantes[x + 1] = aux2


#SALIDA

print("El primer lugar es para " + participantes[0] + "con un total de "  + str(hamburguesas[0]) + "hamburguesas")
print("El segundo lugar es para " + participantes[1] + " con un total de " + str(hamburguesas[1]) + "hamburguesas")
print("El tercer lugar es para " + participantes[2] + " con un total de " + str(hamburguesas[2]) + "hamburguesas")
print("El cuarto lugar es para " + participantes[3] + " con un total de " + str(hamburguesas[3]) + "hamburguesas")
print("El quinto lugar es para " + participantes[4] + " con un total de " + str(hamburguesas[4]) + "hamburguesas")

