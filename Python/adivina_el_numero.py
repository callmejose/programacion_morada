# este programa juega contigo a adivina el número

import random 	#sin esta linea no se pueden generar números aleatorios

numero_intentos = 0	#se inicializa el número de intentos

print('Hola, cuál es tu nombre?')	#pregunta por tu nombre
mi_nombre = input()	#lo que el usuario responda la lleva a la variable "mi_nombre"

numero = random.randint(1, 20)	#genera un número aleatorio entre 1 y 20
print('Hola ' + mi_nombre + ', estoy pensando en un número entre 1 y 20') #impresión

while numero_intentos < 5:	#ciclo que se repetirá 6 veces
    print('Intenta adivinarlo')	#impresión
    intento = input()	#lee un número ingresado por el usuario
    intento = int(intento)	#lo convierte a entero

    numero_intentos = numero_intentos + 1 #aumenta en 1 el numero de intentos actuales

    if intento > numero:	#si el intento es mayor al número secreto
        print('Más pequeño')	#le dice al usuario que se paso
    elif intento < numero:	#si el intento es menor al número secreto
        print('Más grande')		#le dice al usuario que quedo por debajo
    else:	#sino
        break	#se sale del ciclo while

if intento == numero:	#si el último número es igual al número secreto
    numero_intentos = str(numero_intentos)	#convierte a un "string" el número de intentos
    print('Buena esa :D ' + mi_nombre + '!, adivinaste en ' + numero_intentos + ' intentos!') #mensaje de victoria

if intento != numero:	#si el último número es diferente del número secreto
    numero = str(numero)	#convierte el número secreto a "string"
    print('Nop. Habia pensado en el número ' + numero)	#mensaje de derrota
