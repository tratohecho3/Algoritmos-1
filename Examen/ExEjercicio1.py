import sys
"""
# Exejercicio1.py


# DESCRIPCION: 

Es un algoritmo que dado los valores de los angulos de un triangulo, nos muestra que 
tipo de triangulo es(Rectangulo,Acutangulo,Obtusangulo)

# Versión de: 

	Cesar Colina 13-10299
	



# Ultima modificacion: 25/10/2016





# CONSTANTES:







# VARIABLES:
resultado: str// Variable donde se almacena el tipo de triangulo

grado1: int // variable donde se almacena el valor en grados del angulo 1

grado2: int // variable donde se almacena el valor en grados del angulo 2

grado3: int // variable donde se almacena el valor en grados del angulo 3


"""


# Valores iniciales:
resultado = ""

#Precondicion:
while True:
	try:
		grado1 = int(input("Por favor introducir  el valor del grado en el angulo 1: "))
		grado2 = int(input("Por favor introducir  el valor del grado en el angulo 2: "))
		grado3 = int(input("Por favor introducir  el valor del grado en el angulo 3: "))
		assert(grado1 + grado2 + grado3 == 180)
		break
	except:
		print("Recuerde que la suma de los angulos de un triangulo debe ser 180")






#Calculos

if (grado1 < 90) and (grado2 < 90) and (grado3 < 90):
	resultado = "Acutangulo"

elif (grado1 > 90) and (grado2 < 90) and (grado3 < 90):
	resultado = "Obtusangulo"

elif (grado2 > 90) and (grado1 < 90) and (grado3 < 90):
	resultado = "Obtusangulo"

elif (grado3 > 90) and (grado2 < 90) and (grado1 < 90):
	resultado = "Obtusangulo"

elif (grado1 == 90) and (grado2 != 90) and (grado3 != 90):
	resultado = "Rectangulo"

elif (grado2 == 90) and (grado1 != 90) and (grado3 != 90):
	resultado = "Rectangulo"

elif (grado3 == 90) and (grado2 != 90) and (grado1 != 90):
	resultado = "Rectangulo"





# Postcondicion: 
try:
 	assert(grado1 + grado2 + grado3 == 180)
except:
 	print("Ha ocurrido un error en el programa, intente de nuevo")
 	sys.exit()



 # Salida:
print("El triangulo es de tipo ",resultado)

