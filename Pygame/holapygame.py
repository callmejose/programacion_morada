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

dimensiones = [600, 400]
# Abrir la pantalla (otra opción es open_window)
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Mi primer juego")

# ESTE ES EL BUCLE PRINCIPAL DEL PROGRAMA

#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Marca que indica que hemos acabado y sale de este bucle
            
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
    
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
    
    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # Primero limpiamos pantalla. No dibujes por encima de esta linea
    # o todo lo que escribas sera borrado por este comando.
    pantalla.fill(BLANCO)
    
    # DIBUJEMOS ALGUNAS FIGURAS
    pygame.draw.line(pantalla, VERDE, [0, 0], [100, 100], 5)
    pygame.draw.rect(pantalla, NEGRO, [150, 10, 50, 20], 2)
    pygame.draw.ellipse(pantalla, ROJO, [225, 10, 50, 20])

    # DIBUJEMOS ALGUN TEXTO
    # Seleccionamos la fuente, tamaño, negrita, acostada
    fuente = pygame.font.SysFont('Calibri', 25, True, False) 
    # Rendirazar, mi texto, suavizado, color
    texto = fuente.render("Este es mi texto", True, NEGRO) 
    # Poner en pantalla el texto
    pantalla.blit(texto, [250, 250])
    
    # Avanza y actualiza la pantalla con lo que hemos dibujado.
    pygame.display.flip()  
    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
    
    
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

# Cierra la ventana.
# Si olvidas poner esta linea el programa se 'colgara'.
pygame.quit()
