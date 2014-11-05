#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa la librería de funciones llamada 'pygame'
import pygame
import pytmx

# Definimos algunos colores
NEGRO = [ 0, 0, 0]
BLANCO = [ 255, 255, 255]
VERDE = [ 0, 255, 0]
ROJO = [ 255, 0, 0]

# Constantes en mayúsculas

# Inicializa el motor de juegos
pygame.init()
ancho = 6
alto = 6
ancho_pixeles = 32 * ancho
alto_pixeles = 32 * alto
dimensiones = [ancho_pixeles, alto_pixeles]
# Abrir la pantalla (otra opción es open_window)
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Mi primer juego")

# ESTE ES EL BUCLE PRINCIPAL DEL PROGRAMA
pygame.mouse.set_visible(False)
#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuán rápido se actualiza la pantalla
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

tmxdata = pytmx.load_pygame("plantilla.tmx")

principal = hoja_completa.get_image(1, 8, 32, 32)
pasto = hoja_completa.get_image(14, 1, 32, 32)
agua = hoja_completa.get_image(13, 7, 32, 32)
sombra_agua = hoja_completa.get_image(14, 7, 32, 32)

def llenar_fondo(fondo):
    for cuadro_x in range(ancho):
        for cuadro_y in range(alto):
            pantalla.blit(fondo, [cuadro_x * 32, cuadro_y * 32])

def pintar_mapa(tmxdata,pantalla):
    for capa in range(10):
        for x in range(6):
            for y in range(6):
                imagen = tmxdata.get_tile_image(x, y, capa)
                if imagen==None:
                    continue
                pantalla.blit(imagen, [x*32 , y*32])
        
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
            if evento.key==pygame.K_SPACE:
                print(tmxdata)
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
    pantalla.fill(BLANCO)
    pintar_mapa(tmxdata,pantalla)
    #llenar_fondo(pasto)
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
