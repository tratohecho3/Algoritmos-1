


"""Autores: Cesar Colina 13-10299
			Francisco Marquez 12-11163

Lab8Ejercicio.py

Descripcion: Programa que lee una matriz en un archivo .txt y devuelve en otro
archivo .txt una serie de datos de interes.



"""


#CALCULOS
import pygame,sys, os.path
from pygame.locals import *
pygame.init()
while True:
	tiempo = pygame.time.get_ticks() / 1000
	if tiempo > 360:
		sys.exit()
		pygame.quit()
	x = int(input("Introduzca el valor de la fila donde se encuentra su numero: "))
	y = int(input("introduzca el valor de la columna donde se encuentra su numero: "))
	with open("matrix-entry.txt") as f:
		lineas = f.readlines()
	f.closed
	matriz = []
	for i in range(len(lineas)):
		matriz.append(lineas[i].split())
	for i in range(len(matriz)):		
		for j in range(len(matriz[i])):
			matriz[i][j] = int(matriz[i][j])
	Diag_ppal = []
	for i in range(len(lineas)):
		for j in range(len(matriz[i])):
			if i == j:
				if matriz[i][j] > 0 and matriz[i][j]% 2 == 0:
					Diag_ppal.append(matriz[i][j])
	Diag_sec = []
	for i in range(len(lineas)):
		for j in range(len(matriz[i])):
			if i + j == 5:
				if matriz[i][j] < 0 and matriz[i][j]% 2 != 0:
					Diag_sec.append(matriz[i][j])
	
	minimos = []
	for i in range(len(lineas)):
		for j in matriz[i]:
			if j % 2 != 0:
				minimos.append(j)
	valor = 1000
	for i in minimos:
		if i % 2 != 0:
			if i < valor:
				valor = i

	for i in range(len(lineas)):
		for j in range(len(matriz[i])):
			if matriz[i][j] == valor:
				#RESULTADO3
				posicion_impar_menor = [i, j]
			
	maximos = []
	for i in range(len(lineas)):
		for j in matriz[i]:
			if j % 2 == 0:
				maximos.append(j)

	valor2 = max(maximos)

	for i in range(len(lineas)):
		for j in range(len(matriz[i])):
			if matriz[i][j] == valor2:
				#RESULTADO3
				posicion_par_mayor = [i, j]
	
	columna0 = []
	columna1 = []
	columna2 = []
	columna3 = []
	columna4 = []
	columna5 = []

	for i in range(len(matriz)):
		columna0.append(matriz[i][0])
	
	for i in range(len(matriz)):
		columna1.append(matriz[i][1])

	for i in range(len(matriz)):
		columna2.append(matriz[i][2])

	for i in range(len(matriz)):
		columna3.append(matriz[i][3])

	for i in range(len(matriz)):
		columna4.append(matriz[i][4])

	for i in range(len(matriz)):
		columna5.append(matriz[i][5])	

	area1 = []
	for i in range(3):
		for j in range(3):
			area1.append(matriz[i][j])

	area2 = []
	for i in range(3):
		for j in range(3, 6):
			area2.append(matriz[i][j])	

	area3 = []
	for i in range(3, 6):
		for j in range(3):
			area3.append(matriz[i][j])

	area4 = []
	for i in range(3, 6):
		for j in range(3, 6):
			area4.append(matriz[i][j])	

	total = (sum(area1) + sum(area2) + sum(area3) + sum(area4))/ 4

	promedio = sum(Diag_ppal) / len(Diag_ppal)

	sumatoria = sum(Diag_sec)

	with open("report-output.txt", "w") as f:
		f.write("El promedio de los valores pares positivos de la diagonal principal es\n")
		f.write(str(promedio) + "\n")
		f.write("La suma de los valores impares negativos de la diagonal secundaria es \n")
		f.write(str(sumatoria) + "\n")
		f.write("El valor del impar menor de la matriz es" + "\n")
		f.write(str(valor) + "\n")
		f.write("La posicion, o posiciones, del impar menor es, o son" + "\n")
		for i in range(len(lineas)):
			for j in range(len(matriz[i])):
				if matriz[i][j] == valor:
					#RESULTADO3
					f.write("La fila" + "\n")
					f.write(str(i) + "\n")
					f.write("La columna" + "\n")
					f.write(str(j) + "\n")
		f.write("El valor del par mayor de la matriz es" + "\n")
		f.write(str(valor2) + "\n")
		f.write("La posicion, o posiciones, del par mayor es, o son" + "\n")
		for i in range(len(lineas)):
			for j in range(len(matriz[i])):
				if matriz[i][j] == valor2:
					#RESULTADO3
					f.write("La fila" + "\n")
					f.write(str(i) + "\n")
					f.write("La columna" + "\n")
					f.write(str(j) + "\n")
		f.write("El promedio de los valores de cada fila es" + "\n")
		for i in range(len(matriz)):
			#RESULTADO4
			f.write("El promedio de la fila " + str(i) + " es" + "\n")
			f.write(str(sum(matriz[i]) / len(matriz[i])) + "\n")
		f.write("El promedio de los valores de cada columna es" + "\n")
		f.write("Para la columna 0" + "\n")
		f.write(str(sum(columna0) / len(columna0)) + "\n")
		f.write("Para la columna 1" + "\n")
		f.write(str(sum(columna1) / len(columna1)) + "\n")
		f.write("Para la columna 2" + "\n")
		f.write(str(sum(columna2) / len(columna2)) + "\n")
		f.write("Para la columna 3" + "\n")
		f.write(str(sum(columna3) / len(columna3)) + "\n")
		f.write("Para la columna 4" + "\n")
		f.write(str(sum(columna4) / len(columna4)) + "\n")
		f.write("Para la columna 5" + "\n")
		f.write(str(sum(columna5) / len(columna5)) + "\n")
		f.write("La suma de los valores de cada una de las subregiones de la matriz es" + "\n")
		f.write("Para la subregion A" + "\n")
		f.write(str(sum(area1)) + "\n")
		f.write("Para la subregion B" + "\n")
		f.write(str(sum(area2)) + "\n")
		f.write("Para la subregion C" + "\n")
		f.write(str(sum(area3)) + "\n")
		f.write("Para la subregion D" + "\n")
		f.write(str(sum(area4)) + "\n")
		f.write("El promedio de la suma total de las subregiones es" + "\n")
		f.write(str(total))
	f.closed
	print(matriz[x][y])


