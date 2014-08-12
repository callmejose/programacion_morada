class Punto(object): #esta es la definición de la clase Punto, "object" es una palabra reservada de python
    """Representa un punto"""

print(Punto)

blanco = Punto() #creo un objeto de tipo Punto

print(blanco)

###atributos

blanco.x = 3 #dentro del objeto "blanco" creo el atributo "x" y lo hago igual a 3
blanco.y = 4

print(blanco.x) #¿qué crees que se imprima?

def print_punto(p): #creo una función a la que le entra un objeto tipo punto
    print("(%.1f, %.1f)" %(p.x, p.y))
    
print_punto(blanco) #utilizo la función con el objeto que antes habia creado


class Rectangulo(object): #defino una nueva clase
    """Representa un rectangulo.
    
    atributos: ancho, alto, esquina.
    """

caja = Rectangulo() #creo un objeto tipo Rectangulo, este objeto se llama "caja"
caja.ancho = 100 #dentro del objeto caja creo una variable llamada "ancho" y la hago 100
caja.alto = 200 #lo mismo para "alto"

caja.esquina = Punto() #dentro del objeto caja creo un objeto de tipo Punto, este nuevo objeto se llama "esquina"
caja.esquina.x = 0 #a ese objeto que acabo de crear dentro de "caja" le creo una variable "x"
caja.esquina.y = 0

def encontrar_centro(rect): #definición de función a la que le entra un objeto tipo Rectangulo y retorna un objeto tipo Punto
    p = Punto()
    p.x = rect.esquina.x + rect.ancho/2
    p.y = rect.esquina.y + rect.alto/2.0
    return p
    
centro = encontrar_centro(caja) #utilizo la función con el objeto "caja" que habia creado antes
print_punto(centro)

###copia de objetos

caja2 = caja

caja2.ancho = 200
caja2.alto = 400
caja2.esquina = Punto()
caja2.esquina.x = 50
caja2.esquina.y = 50

print_punto(caja.esquina)
print_punto(caja2.esquina)

import copy

caja3 = copy.copy(caja)
caja4 = copy.deepcopy(caja)

print(caja is caja2)
print(caja is caja3)
print(caja.esquina is caja3.esquina)
print(caja is caja4)
print(caja.esquina is caja4.esquina)