"""
PRELABORATORIO Nº 7

PreLab7ejercicio1.py


Autores: 

	12-11499 - Chaparro Orlando
	13-10299 - Colina Cesar

Ultima modificacion: 31/10/2016



"""
#PRECONDICION
assert(True)


# CALCULOS:
archivo = open("input.txt","r")

lista = archivo.readlines()
lista2 = []
lista3 = []
lista4 = []

cadena = ""

for i in lista:
	cadena = cadena + i
lista2 = cadena.split()


contador = 0

for i in lista2:
	if contador == 0:
		pass

	if contador % 2 == 0:
		lista4.append(i)
	else:
		lista3.append(i)
	contador += 1


contador = 0

lista = []

for i in range(len(lista4)):
	if int(lista4[i]) < 0 or int(lista4[i]) > 50:
		lista.append("Linea erronea\n")

	else:
		lista.append(int(lista4[i]) * lista3[i] + "\n")
	contador += 1

cadena = ""
for i in lista:
	cadena = cadena + i


archivo.closed

salida = open("output.txt","w")

salida.write(cadena)

 
salida.closed

salida = open("output.txt","r")



#POSTCONDICION
assert(True)
#SALIDA

print(cadena)
