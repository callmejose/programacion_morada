#!/usr/bin/env python
# -*- coding: utf-8 -*-

### clases y métodos

def int2time(segundos):
    tiempo = Tiempo()
    tiempo.segundos = segundos % 60
    minutos = segundos // 60
    tiempo.minutos = minutos % 60
    tiempo.horas = minutos // 60
    return tiempo

class Tiempo():

    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        
    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.horas, self.minutos, self.segundos)

    def __add__(self, otro):
        return int2time(self.time2int() + otro.time2int())
    
    def print_tiempo(self):
        print("%.2d:%.2d:%.2d" % (self.horas, self.minutos, self.segundos))
        
    def time2int(self):
        segundos = self.segundos
        segundos += self.minutos * 60
        segundos += self.horas * 60**2
        return segundos
        
    def incrementar(self, segundos):
        suma = Tiempo()
        suma = int2time(self.time2int() + segundos)
        self.horas = suma.horas
        self.minutos = suma.minutos
        self.segundos = suma.segundos
        
    def es_despues(self, otro):
        return self.time2int() > otro.time2int()
        

inicio = Tiempo()
inicio.print_tiempo()

inicio = Tiempo(6)
inicio.print_tiempo()

inicio = Tiempo(6, 15)
inicio.print_tiempo()

bano = Tiempo(0, 45)

fin_bano = inicio + bano

print(fin_bano)

print(fin_bano.es_despues(inicio))

