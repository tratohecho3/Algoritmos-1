"""
LABARATORIO # 2

REALIZADO POR CESAR COLINA 13-10299

EJERCICIO 4

Lab02Ejercicio4.py


DESCRIPCION: El algoritmo determina el monto a pagar por N hamburguesas de diferentes tipos considerando los 3 tipos de pagos

CONSTANTES:

VARIABLES:
N: int // numero de hamburguesas totales
pago: str // forma de pago
total: float // total a pagar
sencillas: int // cantidad de hamburguesas sencillas
dobles: int // cantidad de hamburguesas dobles
triples: int // cantidad de hamburguesas triples
"""
print(123456/100)
N = int(input("Ingrese el numero de hamburguesas"))
pago = (input("Ingrese su forma de pago: 1:Efectivo 2:Debito 3:Credito"))

sencillas = int(N / 10000)
dobles = str(N /100)
dobles = dobles.reverse
print(dobles)
total = sencillas * 20 + dobles + 25 + triples * 30

if pago == "2" and total < 250:
	total = total + total * 0.05

elif pago == "3" and total < 500:
	total = total + total * 0.1

print(total)

