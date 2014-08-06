class Punto(object):
    """Representa un punto"""

print(Punto)

blanco = Punto()

print(blanco)

###atributos

blanco.x = 3
blanco.y = 4

print(blanco.x)

def print_punto(p):
    print("(%.1f, %.1f)" %(p.x, p.y))
    
print_punto(blanco)


class Rectangulo(object):
    """Representa un rectangulo.
    
    attributes: ancho, alto, esquina.
    """

caja = Rectangulo()
caja.ancho = 100
caja.alto = 200

caja.esquina = Punto()
caja.esquina.x = 0
caja.esquina.y = 0

def encontrar_centro(rect):
    p = Punto()
    p.x = rect.esquina.x + rect.ancho/2
    p.y = rect.esquina.y + rect.alto/2.0
    return p
    
centro = encontrar_centro(caja)
print_punto(centro)

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