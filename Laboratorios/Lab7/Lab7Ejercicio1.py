#	Lab7Ejercicio1.py

#	DESCRIPCIÓN: El programa leerá el contenido del archivo "datos-dace.txt",
#	que proporcionará el carnet, el nombre, el índice y el sexo y devolverá un
#	archivo "reporte-dace-txt" con el promedio del indice, la cantidad de 
#	estudiantes con carnet menor a 91, cantidad de estudiantes con carnet mayor 
#	a 91, cantidad de estudiantes masculinos con indice mayor a 3.5 y la 
#	cantidad de estudiantes femeninos con índice superior a 4.

#	AUTOR: David Segura 13-11341 y Cesar Colina 13-10299


#	VARIABLES:

#	archivo1 : funcion // Abre el archivo "datos-dace.txt" para leer

#	datos : list // Lista que almacena las lineas del archivo

# 	datos2 : list // Lista que elimina la primera linea del archivo

#	indice : float // Indice del estudiante

#	cantidad : int // Calcula la cantidad de estudiantes con carnet < 91

#	cantidad2 : int // calcula la cantidad de estudiantes con carnet > 91

#	masculinos : int // calcula la cantidad de estudiantes masculinos con indice > 3.5

#	femeninos :	int // calcula la cantidad de estudiantes femeninos con indice > 4.0

#	nueva: lista // almacena los datos de salida

#	indices: float // Calcula la suma de los indices

#	lista: lista // Particiona los elementos de la lista datos

#	carnet: str // indica el carnet del estudiante

#	carnet2: int // indica los dos primeros numeros del carnet

#	sexo: str // indica el sexo del estudiante

#	promedio: float // calcula el promedio de los indices de los estudiantes

#	salida : funcion // Abre el archivo "reporte-dace.txt" para escribir


#	VALORES INICIALES:

archivo1=open("datos-dace.txt","r")
datos=archivo1.readlines()
datos2 = []

for i in range(1,len(datos)):
	datos2.append(datos[i])
datos = datos2

indice = 0
cantidad = 0
cantidad2 = 0
masculinos = 0
femeninos = 0
nueva = []
indices = 0

#	PRECONDICION:

assert(len(datos) > 0)


#	PROGRAMA:

for elemento in datos:
	lista = elemento.split()
	indice = lista[3]
	indice = float(indice)
	indices = indices + indice
	carnet = lista[0]
	carnet2 = int(carnet[:2])
	if carnet2 < 91:
		cantidad = cantidad + 1 
	elif carnet2 > 91:
		cantidad2 = cantidad2 + 1
	sexo = lista[4]
	if sexo == "M":
		if indice > 3.5:
			masculinos = masculinos + 1
		else:
			pass
	elif sexo == "F":
		if indice > 4:
			femeninos = femeninos + 1
promedio=indices/len(datos)

nueva.append(promedio)
nueva.append(cantidad)
nueva.append(cantidad2)
nueva.append(masculinos)
nueva.append(femeninos)

archivo1.close()

#	POSTCONDICION:

assert(len(nueva) > 0)

#	SALIDA:

with open("reporte-dace.txt","w") as salida:
	salida.write("Indice promedio de los estudiantes: "+str(nueva[0])+ "\n" + "Cantidad de estudiantes con carnet menor a 91: "+str(nueva[1])+ "\n" +"Cantidad de estudiantes con carnet mayor a 91: "+str(nueva[2])+ "\n" +"Cantidad de estudiantes masculinos con indice superior a 3.5: "+str(nueva[3])+ "\n" +"Cantidad de estudiantes femeninos con indice superior a 4.0: "+str(nueva[4]))
salida.close()
