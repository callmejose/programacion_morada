#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importa la librería de funciones llamada 'pygame'
import pygame
import pytmx 
import copy

# Definimos algunos colores
NEGRO = [ 0, 0, 0]
BLANCO = [ 255, 255, 255]
VERDE = [ 0, 255, 0]
ROJO = [ 255, 0, 0]

# Constantes en mayúsculas

# Inicializa el motor de juegos
pygame.init()
ancho = 40
alto = 22
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
informacion = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

class SpriteSheet(object):
    """ Clase usada para sacar imágenes de la hoja de sprites."""
    # inicializamos la hoja de sprites
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Le entra el nombre de archivo de la hoja 
        de sprites. """

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

class mapa(object):
    """en esta clase se definira el mapa"""
    
    xmin = 0
    xmax = 32*ancho
    ymin = 0
    ymax = 32*alto
    
    #capas = 15
    #personaje = 9
    
    #datos = pytmx.load_pygame("./jardin.tmx")
    
    def pintar_mapa(self,pantalla):
        for capa in range(self.capas):
            if capa == self.personaje:
                for personaje in personajes:
                    personaje.pintese(pantalla)
            else:
                for x in range(ancho):
                    for y in range(alto):
                        imagen = self.datos.get_tile_image(x, y, capa)
                        if imagen==None:
                            continue
                        pantalla.blit(imagen, [x*32 , y*32])
                        
    def __init__(self, ruta, n_capas, c_personaje):
        self.datos = pytmx.load_pygame(ruta)
        self.capas = n_capas
        self.personaje = c_personaje
    
    def cambiar_mapa(self, ruta, n_capas, c_personaje):
        self.datos = pytmx.load_pygame(ruta)
        self.capas = n_capas
        self.personaje = c_personaje
        print("cambie el mapa, ", self)


class personaje(object):
    """este es tu personaje
    le puedes dar atributos"""
    
    direccion=""
    x = ancho*16
    y = alto*16
    velocidad_x = 0
    velocidad_y = 0
    
    adelante = hoja_completa.get_image(3, 8, 32, 32)
    derecha = hoja_completa.get_image(3,10,32,32)
    izquierda = hoja_completa.get_image(3,9,32,32)
    atras = hoja_completa.get_image(3,11,32,32)
    imagen_actual = adelante
    
    def cambiar_direccion(self,nueva_direccion):
        if nueva_direccion == "derecha":
            self.imagen_actual = self.derecha
            self.direccion = "derecha"
        if nueva_direccion == "izquierda":
            self.imagen_actual = self.izquierda
            self.direccion = "izquierda"
        if nueva_direccion == "adelante":
            self.imagen_actual = self.adelante
            self.direccion = "adelante"
        if nueva_direccion == "atras":
            self.imagen_actual = self.atras
            self.direccion = "atras"

    def cambiar_velocidad(self, direccion, velocidad):
        self.cambiar_direccion(direccion)
        self.pare_seguro()
        if direccion == "derecha":
            self.velocidad_x += velocidad
        if direccion == "izquierda":
            self.velocidad_x -= velocidad
        if direccion == "adelante":
            self.velocidad_y += velocidad
        if direccion == "atras":
            self.velocidad_y -= velocidad
    
    def pare(self, direccion):
        if direccion == self.direccion:
            self.velocidad_x = 0
            self.velocidad_y = 0
            
    def pare_seguro(self):
        self.velocidad_x = 0
        self.velocidad_y = 0
    
    def muevase(self, mapa):
        if (self.x + self.velocidad_x >= mapa.xmin 
        and self.x + self.velocidad_x + 16 <= mapa.xmax 
        and self.y + self.velocidad_y >= mapa.ymin 
        and self.y + self.velocidad_y + 16 <= mapa.ymax): #dentro del mapa
            imagen = mapa.datos.get_tile_image((self.x+self.velocidad_x)//32, (self.y+self.velocidad_y)//32, 0)
            if imagen==None:
                self.x += self.velocidad_x
                self.y += self.velocidad_y

    def pintese(self, ventana):
        ventana.blit(self.imagen_actual, [(self.x//32)*32, (self.y//32)*32]) #solo se pinta centrado en los cuadros, múltiplos de 32
        
    def cambiar_apariencia(self, disfraz):
        if disfraz == "niño":
            self.adelante = hoja_completa.get_image(0, 8, 32, 32)
            self.derecha = hoja_completa.get_image(0,10,32,32)
            self.izquierda = hoja_completa.get_image(0,9,32,32)
            self.atras = hoja_completa.get_image(0,11,32,32)
        elif disfraz == "esqueleto":
            self.adelante = hoja_completa.get_image(6, 8, 32, 32)
            self.derecha = hoja_completa.get_image(6,10,32,32)
            self.izquierda = hoja_completa.get_image(6,9,32,32)
            self.atras = hoja_completa.get_image(6,11,32,32)
        elif disfraz == "baba":
            self.adelante = hoja_completa.get_image(0, 12, 32, 32)
            self.derecha = hoja_completa.get_image(0,14,32,32)
            self.izquierda = hoja_completa.get_image(0,13,32,32)
            self.atras = hoja_completa.get_image(0,15,32,32)
        elif disfraz == "murcielago":
            self.adelante = hoja_completa.get_image(3, 12, 32, 32)
            self.derecha = hoja_completa.get_image(3,14,32,32)
            self.izquierda = hoja_completa.get_image(3,13,32,32)
            self.atras = hoja_completa.get_image(3,15,32,32)
        elif disfraz == "fantasma":
            self.adelante = hoja_completa.get_image(6, 12, 32, 32)
            self.derecha = hoja_completa.get_image(6,14,32,32)
            self.izquierda = hoja_completa.get_image(6,13,32,32)
            self.atras = hoja_completa.get_image(6,15,32,32)
        elif disfraz == "araña":
            self.adelante = hoja_completa.get_image(12, 12, 32, 32)
            self.derecha = hoja_completa.get_image(12,14,32,32)
            self.izquierda = hoja_completa.get_image(12,13,32,32)
            self.atras = hoja_completa.get_image(12,15,32,32)
        else:
            self.adelante = hoja_completa.get_image(3, 8, 32, 32)
            self.derecha = hoja_completa.get_image(3,10,32,32)
            self.izquierda = hoja_completa.get_image(3,9,32,32)
            self.atras = hoja_completa.get_image(3,11,32,32)
            
violeta = personaje()

monstruo1 = personaje()
monstruo1.cambiar_apariencia("esqueleto")
monstruo1.cambiar_velocidad("adelante", 5)

monstruo2 = personaje()
monstruo2.cambiar_apariencia("baba")
monstruo2.cambiar_velocidad("derecha", 5)

monstruo3 = personaje()
monstruo3.cambiar_apariencia("murcielago")
monstruo3.cambiar_velocidad("izquierda", 5)

monstruo4 = personaje()
monstruo4.cambiar_apariencia("fantasma")
monstruo4.cambiar_velocidad("atras", 5)

personajes = [violeta, monstruo1, monstruo2, monstruo3, monstruo4]

mapa_actual = mapa("./jardin.tmx", 15, 9)

jardin = mapa("./jardin.tmx", 15, 9)

laberinto = mapa("./laberinto.tmx", 13, 8)


def pintar_texto():
    # Seleccionamos la fuente, tamaño, negrita, acostada
    fuente = pygame.font.SysFont('Calibri', 25, True, False) 
    # Rendirazar, mi texto, suavizado, color
    texto = fuente.render(str(violeta.x) + "   " + str(violeta.y), True, NEGRO) 
    # Poner en pantalla el texto
    pantalla.blit(texto, [0,0])
    
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
                violeta.cambiar_velocidad("atras", 5)
            if evento.key==pygame.K_DOWN:
                violeta.cambiar_velocidad("adelante", 5)
            if evento.key==pygame.K_RIGHT:
                violeta.cambiar_velocidad("derecha", 5)
            if evento.key==pygame.K_LEFT:
                violeta.cambiar_velocidad("izquierda", 5)
            if evento.key==pygame.K_F3:
                informacion = not informacion
                mapa_actual = laberinto
            if evento.key==pygame.K_F2:
                mapa_actual = jardin
        if evento.type==pygame.KEYUP:
            if evento.key==pygame.K_UP:
                violeta.pare("atras")
            if evento.key==pygame.K_DOWN:
                violeta.pare("adelante")
            if evento.key==pygame.K_RIGHT:
                violeta.pare("derecha")
            if evento.key==pygame.K_LEFT:
                violeta.pare("izquierda")
            
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
    
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    for personaje in personajes:
        personaje.muevase(mapa_actual)
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
   
    
    # Primero limpiamos pantalla. No dibujes por encima de esta linea
    # o todo lo que escribas sera borrado por este comando.
    pantalla.fill(BLANCO)
    #todo(pasto,0,0,16,20)
    #todo(pasto,0.5,0.5,15,19)
    # pantalla.blit(pasto, [x, y])
    mapa_actual.pintar_mapa(pantalla)
    
    
    # DIBUJEMOS ALGUNAS FIGURAS
    # DIBUJEMOS ALGUN TEXTO
    if informacion:
        pintar_texto()
            
    # Avanza y actualiza la pantalla con lo que hemos dibujado.
    pygame.display.flip()  
    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
    
    
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(30)

# Cierra la ventana.
# Si olvidas poner esta linea el programa se 'colgara'.
pygame.quit()
