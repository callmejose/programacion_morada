#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa la librería de funciones llamada 'pygame'
import pygame

# Definimos algunos colores
NEGRO = [ 0, 0, 0]
BLANCO = [ 255, 255, 255]
VERDE = [ 0, 255, 0]
ROJO = [ 255, 0, 0]

# Constantes en mayúsculas

# Inicializa el motor de juegos
pygame.init()
h=32*20
g=32*16
dimensiones = [h, g]
# Abrir la pantalla (otra opción es open_window)
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Mi primer juego")

# ESTE ES EL BUCLE PRINCIPAL DEL PROGRAMA
pygame.mouse.set_visible(False)
#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
y = -128
x = -128
velocidad_x=0
velocidad_y=0

class SpriteSheet(object):
    """ Clase usada para sacar imágenes de la hoja de sprites."""
    # inicializamos la hoja de sprites
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Le entra el nombre de archivo de la hoja de sprites. """

        # Carga la hoja de datos completa.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, fila, columna, ancho, alto):
        """ retorna una única imagen
        se le pasa la posición (x, y)
        y el ancho y alto del sprite. """

        # Crea una imagen en blanco
        imagen = pygame.Surface([ancho, alto]).convert()

        # Copia una parte de la hoja de sprites a la imagen
        imagen.blit(self.sprite_sheet, (0, 0), (fila * ancho, columna * alto, ancho, alto))

        # Asume que el negro es el color transparente
        imagen.set_colorkey(NEGRO)

        # Retorna la imagen
        return imagen
        
hoja_completa = SpriteSheet("./imagenes/completa32.png")

principal = hoja_completa.get_image(1, 8, 32, 32)
pasto = hoja_completa.get_image(14, 1, 32, 32)
agua = hoja_completa.get_image(13, 7, 32, 32)
sombra_agua = hoja_completa.get_image(14, 7, 32, 32)
piedraroja = hoja_completa.get_image(14,0,32,32)
murorojo = hoja_completa.get_image(13,0,32,32)
madera=hoja_completa.get_image(4,4,32,32)
mecha_amari = hoja_completa.get_image(14,12,32,32)
trono = hoja_completa.get_image(10,6,32,32)
silla = hoja_completa.get_image(11,6,32,32)
cajon = hoja_completa.get_image(12,6,32,32)
cofre = hoja_completa.get_image(4,2,32,32)
def hacelo(que,mix,miy):
    pantalla.blit(que, [mix*32,miy*32])


    
def todo(pintura,x,y,baja,lado):
    for w in range(baja):
        for s in range(lado):
            hacelo(pintura,x+s,y+w)
        
def dibujar_fondo():
    #####todo(lo que quieres dibujar,su pos en x,su pos en y,cuanto de largo,cuanto de ancho):
    #todo(maderadiagonal,,,4,4)
    todo(piedraroja,2,1,1,7)
    todo(murorojo,1,1,10,1)
    todo(piedraroja,1,11,1,9)
    todo(madera,2,2,9,7)
    todo(murorojo,9,1,7,1)
    todo(madera,9,8,3,4)
    todo(piedraroja,9,7,1,5)
    todo(murorojo,12,1,7,1)
    todo(murorojo,13,1,1,6)
    todo(murorojo,18,2,9,1)
    todo(piedraroja,12,11,1,7)
    todo(madera,13,2,9,5)
    todo(murorojo,9,11,5,1)
    todo(murorojo,12,11,5,1)
    todo(madera,10,11,5,2)

    hacelo(mecha_amari,2,2)
    hacelo(mecha_amari,8,2)
    hacelo(mecha_amari,2,10)
    hacelo(mecha_amari,8,10)
    hacelo(mecha_amari,13,10)
    hacelo(mecha_amari,13,2)
    hacelo(mecha_amari,17,10)
    hacelo(mecha_amari,17,2)
    hacelo(trono,5,2)
    todo(silla,3,4,6,5)
    hacelo(cajon,4,2)
    hacelo(cajon,6,2)
    todo(cofre,14,3,1,3)
# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Marca que indica que hemos acabado y sale de este bucle
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_UP:
                
                velocidad_y=-2
            if evento.key==pygame.K_DOWN:
                velocidad_y=2
            if evento.key==pygame.K_RIGHT:
                velocidad_x=2
            if evento.key==pygame.K_LEFT:
                velocidad_x=-2
        if evento.type==pygame.KEYUP:
            if evento.key==pygame.K_UP:
                velocidad_y=0
            if evento.key==pygame.K_DOWN:
                velocidad_y=0
            if evento.key==pygame.K_RIGHT:
                velocidad_x=0
            if evento.key==pygame.K_LEFT:
                velocidad_x=0
            
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
    
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    x+=velocidad_x
    y+=velocidad_y
    
    pos = pygame.mouse.get_pos()
    xm = pos[0]
    ym = pos[1]
    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
   
    
    # Primero limpiamos pantalla. No dibujes por encima de esta linea
    # o todo lo que escribas sera borrado por este comando.
    pantalla.fill(NEGRO)
    dibujar_fondo()
    # pantalla.blit(pasto, [x, y])
    pantalla.blit(principal, [xm, ym])
    
    
    # DIBUJEMOS ALGUNAS FIGURAS
    # barquito(x-200,y-200)
    
    # Avanza y actualiza la pantalla con lo que hemos dibujado.
    pygame.display.flip()  
    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
    
    
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

# Cierra la ventana.
# Si olvidas poner esta linea el programa se 'colgara'.
pygame.quit()
