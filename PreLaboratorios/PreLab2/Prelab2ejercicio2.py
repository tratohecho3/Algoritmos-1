'''
PRELABORATORIO Nº 2

Prelab2ejercicio2.py



DESCRIPCION: Implementacion de un Algoritmo en Python para calcular \
	el monto total semanal de los jornadas diarias laboradas por los\
	empleados de una fabrica
	


Autores: 

	12-11499 - Chaparro Orlando
	13-10299 - Colina Cesar

 Ultima modificacion: 23/09/2016'''

""" VARIABLES: 

#	trabajador: int // Valor que el sistema pide para identificar el tipo de empleado

#	GERENTE: str // Palabra que denota si el empleado es un gerente de planta

#	SUPERVISOR: str // Palabra que denota si el empleado es un supervisor

#	TRABAJADOR: str // Palabra que denota si el empleado es un trabajador

#	TurnoG: int // Numero de horas trabajadas por el gerente

#	TurnoM: int // Numero de horas trabajadas en el turno matutino

#	TurnoV: int // Numero de horas trabajadas en el turno vespertino

#	TurnoN: int // Numero de horas trabajadas en el turno nocturno

#	TurnoMdelFDS: int // Numero de horas trabajadas en el fin de semana en horario matutino

#	TurnoVdelFDS: int // Numero de horas trabajadas en el fin de semana en horario vespertino

#	TurnoNdelFDS: int // Numero de horas trabajadas en el fin de semana en horario nocturno
	

#	GANANCIA: int // Pago que recibira el trabajador

#	BONO: float // Ganancia por trabajar en horario nocturno o fin de semana

#	PagoFDS: int // Pago que recibira el trabajador por trabajar un fin de semana

# Fin: str // Indica si el trabajador laboro el fin de semana

"""


# VALORES INICIALES:


BONO = 0

trabajador = int(input("Indique con el numero especificado si el empleado es GERENTE (1) si es SUPERVISOR (2) o si es TRABAJADOR (3): "))

TurnoG, TurnoM, TurnoV, TurnoN, TurnoMdelFDS, TurnoVdelFDS, TurnoNdelFDS = 0, 0, 0, 0, 0, 0, 0


# PRECONDICION:

assert(trabajador > 0 and trabajador < 4 and TurnoG >= 0 and TurnoM >= 0 and TurnoV >= 0 and TurnoN >= 0 and TurnoMdelFDS >= 0 and TurnoVdelFDS >= 0 and TurnoNdelFDS >= 0 ) 


# CALCULOS:

if trabajador == 1:								#EL SISTEMA PIDE QUE SE ESPECIFIQUE MEDIANTE UN NUMERO EL TIPO DE
	trabajador = str("GERENTE")					#EMPLEADO A CONSIDERAR PARA CALCULAR SU SALARIO SEMANAL
elif trabajador == 2:
	trabajador = str("SUPERVISOR")
elif trabajador == 3:
	trabajador = str("TRABAJADOR")
	
if trabajador == "GERENTE": 														#EL PAGO PARA EL GERENTE ES 950$ SEMANAL MAS 10$ POR CADA
	TurnoG = int(input("Indique el numero de horas extras trabajadas por el GERENTE: "))	#HORA TRABAJADA
	GANANCIA = 950 + TurnoG * 10
	print("El pago correspondiente al gerente es: " + str(GANANCIA) + "$")

elif trabajador == "SUPERVISOR" or trabajador == "TRABAJADOR":
	TurnoM = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno MATUTINO: "))    #EL SISTEMA PIDE QUE EL USUARIO INGRESE
	TurnoV = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno VESPERTINO: "))  #EL NUMERO DE HORAS TRABAJADAS EN CADA
	TurnoN = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno NOCTURNO: ")) 	  #HORARIO, POSTERIORMENTE SE PIDE QUE SE 
																														  #ESPECIFIQUE SI EL EMPLEADO TRABAJO EL FIN
	if trabajador == "SUPERVISOR": 																						  #DE SEMANA Y CUANTAS HORAS EN CADA HORARIO
		GANANCIA = (45 * TurnoM) + (50 * TurnoV) + (60 * TurnoN)
		Fin = input("¿El " + str(trabajador) + " realizo turno laborable el fin de semana: ? (s/n) ")
		if Fin == "s" or Fin == "S":
			TurnoMdelFDS = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno MATUTINO del FIN DE SEMANA: "))
			TurnoVdelFDS = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno VESPERTINO del FIN DE SEMANA: "))
			TurnoNdelFDS = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno NOCTURNO del FIN DE SEMANA: "))
			PagoFDS = TurnoMdelFDS * 45 + TurnoNdelFDS * 60 + TurnoVdelFDS * 50
			BONO = 30 * TurnoN * 60 / 100 + 50 * PagoFDS / 100
			print("El pago correspondiente al " + str(trabajador) + " es de: " + str(GANANCIA + PagoFDS) + "$ + un bono de: " + str(BONO) + "$")
		elif Fin == "n" or Fin == "N":
			BONO = 30 * TurnoN * 60 / 100
			print("El pago correspondiente al " + str(trabajador) + " es de: " + str(GANANCIA) + "$ + un bono de: " + str(BONO) + "$")
			
	elif trabajador == "TRABAJADOR":
		GANANCIA = (25 * TurnoM) + (30 * TurnoV) + (40 * TurnoN) 
		Fin = input("¿El " + str(trabajador) + " realizo turno laborable el fin de semana: ? (s/n) ")
		if Fin == "s" or Fin == "S":
			TurnoMdelFDS = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno MATUTINO del FIN DE SEMANA: "))
			TurnoVdelFDS = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno VESPERTINO del FIN DE SEMANA: "))
			TurnoNdelFDS = int(input("Indique el numero de horas trabajadas por el " + str(trabajador) + " en el turno NOCTURNO del FIN DE SEMANA: "))
			PagoFDS = TurnoMdelFDS * 25 + TurnoNdelFDS * 40 + TurnoVdelFDS * 30
			BONO = 30 * TurnoN * 40 / 100 + 50 * PagoFDS / 100
			print("El pago correspondiente al " + str(trabajador) + " es de: " + str(GANANCIA + PagoFDS) + "$ + un bono de: " + str(BONO) + "$")
		elif Fin == "n" or Fin == "N":
			BONO = 30 * TurnoN * 60 / 100
			print("El pago correspondiente al " + str(trabajador) + " es de: " + str(GANANCIA) + "$ + un bono de: " + str(BONO) + "$")
		
	
# POSTCONDICION:

assert(GANANCIA > 0 and GANANCIA >= BONO)


	
