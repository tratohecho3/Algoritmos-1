"""
LABARATORIO # 2

REALIZADO POR CESAR COLINA 13-10299

EJERCICIO 2

Lab02Ejercicio2.py


DESCRIPCION: El algoritmo determina cuánto debe pagar por cada concepto una persona que realiza una llamada, si Cuando se realiza una llamada,
 el cobro es por el tiempo que esta dura, de tal forma que los primeros cinco minutos cuestan $ 1.00 c/u, los siguientes tres, 80￠c/u,
 los siguientes dos minutos, 70￠c/u, y a partir del décimo minuto, 50￠c/u. 
Además, se carga un impuesto de 3 % cuando es domingo, y si es dia hábil, en turno matutino, 15 %, y en turno vespertino, 10 %. 


CONSTANTES:

VARIABLES:

dia: str // Turno en que se realizo la llamada
minutos: int // Numero de minutos realizados en la llamada
total : float // Total del costo de la llamada 
"""



dia = input("Por favor ingrese el numero correspondiente segun el turno en que esta realizando la llamada: \n 1: Domingo  \n 2: Dia Habil Matutino \n 3: Dia Habil vespertino")

minutos = int(input("Ingrese el numero de minutos realizados en la llamada"))
total = 0

#PRECONDICION

assert( minutos > 0 )

#CALCULO
if minutos <= 5:
	total = minutos 

elif minutos > 5 and minutos <= 8:
	total = 5 + ((minutos -5)  * (0.8)) 

elif minutos > 8 and minutos <= 10:
	total = 7.4 + ((minutos - 8)* 0.7)
elif minutos > 10:
	total = 8.8 + ((minutos -10)* 0.5)

if dia == "1":
	total = total + total *0.03
elif dia == "2":
	total = total + total * 0.15
elif dia == "3":
	total = total + total * 0.1
#POSTCONDICION
assert( total > 0)

#RESULTADO

print(total, "$")


