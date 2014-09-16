# Importa la libraría de funciones llamada 'pygame'
import pygame

# Definimos algunos colores
NEGRO = [ 0, 0, 0]
BLANCO = [ 255, 255, 255]
VERDE = [ 0, 255, 0]
ROJO = [ 255, 0, 0]

# Constantes en mayúsculas

# Inicializa el motor de juegos
pygame.init()
h=256
g=256
dimensiones = [h, g]
# Abrir la pantalla (otra opción es open_window)
pantalla = pygame.display.set_mode(dimensiones)

pasto = pygame.image.load("grass.png").convert()
avatar = pygame.image.load("james.png").convert()
avatar.set_colorkey(NEGRO)

musica = pygame.mixer.Sound("Collision.ogg")

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
def barquito(x, y):
    pygame.draw.line(pantalla, NEGRO,[x+200, y+0], [x+200, y+200], 2)
    pygame.draw.line(pantalla, NEGRO,[x+200, y+0], [x+300, y+50])
    pygame.draw.line(pantalla, NEGRO,[x+200, y+100], [x+300, y+50])
    pygame.draw.line(pantalla, NEGRO,[x+0, y+200], [x+400, y+200])
    pygame.draw.line(pantalla, NEGRO,[x+0, y+200], [x+100, y+400])
    pygame.draw.line(pantalla, NEGRO,[x+100, y+400], [x+300, y+400])
    pygame.draw.line(pantalla, NEGRO,[x+300, y+400], [x+400, y+200])

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
    pantalla.fill(BLANCO)
    pantalla.blit(pasto, [x, y])
    pantalla.blit(avatar, [xm, ym])
    
    
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
