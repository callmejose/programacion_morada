#!/usr/bin/env python
# -*- coding: utf-8 -*-

### clases y funciones

class Tiempo():
    """ representa el tiempo
        atributos: horas, minutos, segundos"""
        
ahora = Tiempo()
ahora.horas = 11
ahora.minutos = 59
ahora.segundos = 30

def print_tiempo(tiempo):
    print("%.2d:%.2d:%.2d" % (tiempo.horas, tiempo.minutos, tiempo.segundos))
    
print("\nahora:")
print_tiempo(ahora)

def time2int(tiempo):
    segundos = tiempo.segundos
    segundos += tiempo.minutos * 60
    segundos += tiempo.horas * 60**2
    return segundos
    
def int2time(segundos):
    tiempo = Tiempo()
    tiempo.segundos = segundos % 60
    minutos = segundos // 60
    tiempo.minutos = minutos % 60
    tiempo.horas = minutos // 60
    return tiempo
    
def es_despues(t1, t2):
    return time2int(t1) > time2int(t2)
    
despues = Tiempo()
despues.horas = 12
despues.minutos = 59
despues.segundos = 37

print("\ndespues:")
print_tiempo(despues)

print("\ndespues es luego de ahora?")
print(es_despues(despues, ahora))

def sumar_tiempos(t1, t2):
    suma = Tiempo()
    suma = int2time(time2int(t1)+time2int(t2))
    return suma
    
def incrementar(tiempo, segundos):
    suma = Tiempo()
    suma = int2time(time2int(tiempo)+segundos)
    tiempo.horas = suma.horas
    tiempo.minutos = suma.minutos
    tiempo.segundos = suma.segundos
    
duracion = Tiempo()
duracion.horas = 2
duracion.minutos = 25
duracion.segundos = 35

print(u"\nduracion:")
print_tiempo(duracion)

###antes de la película
fin = sumar_tiempos(ahora, duracion)
print("\nla pelicula terminara a las:")
print_tiempo(fin)

###después de la película
duracion_segundos = time2int(duracion)
incrementar(ahora, duracion_segundos)
print("\nahora son las:")
print_tiempo(ahora)