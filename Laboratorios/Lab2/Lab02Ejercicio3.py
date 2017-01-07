"""
LABARATORIO # 2

REALIZADO POR CESAR COLINA 13-10299

EJERCICIO 2

Lab02Ejercicio2.py


DESCRIPCION: El algoritmo determina la beca otorgada

CONSTANTES:

VARIABLES:

edad: int // Edad de la persona
indice: float // indice de la persona 
beca: int // Total de la beca otorgada
carta: bool // Booleano que nos dice si se envia carta o no
"""

edad = int(input("Ingrese su edad"))
indice = float(input("Ingrese su indice"))
beca = 0
carta = False 

#PRECONDICION

assert(edad > 0 and indice > 0)
if edad > 18:
	if 4.5 <= indice <= 5:
		beca = 2000
	elif 4.1 < indice < 4.5:
		beca = 1000
	elif 3 < indice < 3.9:
		beca = 500
	else:
		carta = True 
elif edad <= 18:
	if 4.5 <= indice <= 5:
		beca = 3000
	elif 4.1 < indice < 4.5:
		beca = 2000
	elif 3 < indice < 3.9:
		beca = 500
	elif indice < 3:
		carta = True

#POSTCONDICION
assert(beca >= 0)
#RESULTADOS
print("La beca otorgada es",beca)
print("Se envia carta:",carta) 
