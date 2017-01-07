#	Lab7Ejercicio1.py

#	DESCRIPCIÓN: El programa leerá el contenido del archivo "calculo-nomina-usb.txt",
#	que proporcionará las horas trabajadas de un empleado, y la canditad que le
#	pagan por hora. El programa devolverá un archivo "nomina-trabajadores-usb.txt"
#	con la cantidad de horas trabajadas y el monto total de esas horas.


#	AUTOR: David Segura 13-11341 y Cesar Colina 13-10299


#	VARIABLES:

#	archivo1 : funcion // Abre el archivo "calculo-nomina-usb.txt" para leer

#	datos : list // Lista que almacena las lineas del archivo

# 	datos2 : list // Lista que elimina la primera linea del archivo

#	montototal : int // Calcula el monto total de las horas trabajadas por empleado

#	horastotal : int // Calcula las horas totales trabajadas por los empleados

#	nueva: lista // almacena los datos de salida

#	horas: int // Almacena las horas trabajadas por el empleado

#	sueldoph: int // Almacena el sueldo por hora del empleado

#	sueldototal: int // Almacena el sueldo obtenido por horas trabajadas

#	salida : funcion // Abre el archivo "nomina-trabajadores-usb.txt" para escribir

#	lista: lista // Particiona los elementos de la lista datos


#	VALORES INICIALES:

archivo1=open("calculo-nomina-usb.txt","r")
datos=archivo1.readlines()
datos2 = []

for i in range(1,len(datos)):
	datos2.append(datos[i])
datos = datos2

montototal = 0
horastotal = 0
nueva = []

#	PRECONDICION:

assert(len(datos) > 0)

#	PROGRAMA:

for elemento in datos:
	lista = elemento.split()
	horas = int(lista[2])
	sueldoph = int(lista[3])
	sueldototal = sueldoph * horas
	montototal = montototal + sueldototal
	horastotal = horastotal + horas

nueva.append(horastotal)
nueva.append(montototal)

archivo1.close()

#	POSTCONDICION:

assert(len(nueva) > 0)

#	SALIDA:

with open("nomina-trabajadores-usb.txt","w") as salida:
	salida.write("CANTIDAD HORAS		MONTO TOTAL"+"\n"+str(nueva[0])+"			"+str(nueva[1]))
salida.close()




