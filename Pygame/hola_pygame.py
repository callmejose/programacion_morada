# Importa la librar�a de funciones llamada 'pygame'
import pygame

# Definimos algunos colores
NEGRO = [ 0, 0, 0]
BLANCO = [ 255, 255, 255]
VERDE = [ 0, 255, 0]
ROJO = [ 255, 0, 0]

# Inicializa el motor de juegos
pygame.init()

dimensiones = [400, 500]
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("mi primer juego")

#Itera hasta que el usuario pincha sobre el bot�n de cierre.
hecho = False

# Se usa para gestionar cuan r�pido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBER�AN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Marca que indica que hemos acabado y sale de este bucle
            
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBER�AN IR ENCIMA DE ESTE COMENTARIO
    
    
    # TODA LA L�GICA DEL JUEGO DEBER�A IR DEBAJO DE ESTE COMENTARIO
    
    # TODA LA L�GICA DEL JUEGO DEBER�A IR ENCIMA DE ESTE COMENTARIO
    
    
    # TODO EL C�DIGO DE DIBUJO DEBER�A IR DEBAJO DE ESTE COMENTARIO

    # Primero limpiamos pantalla. No dibujes por encima de esta linea
    # o todo lo que escribas sera borrado por este comando.
    pantalla.fill(BLANCO)
    
    # Dibuja una linea desde (0,0) hasta (100,100)
    # con 5 pixeles de ancho.
    pygame.draw.line(pantalla, VERDE, [0, 0], [100, 100], 5)    
    
    # Avanza y actualiza la pantalla con lo que hemos dibujado.
    pygame.display.flip()  
    
    # TODO EL C�DIGO DE DIBUJO DEBER�A IR ENCIMA DE ESTE COMENTARIO
    
    
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

# Cierra la ventana.
# Si olvidas poner esta linea el programa se 'colgara'.
pygame.quit()