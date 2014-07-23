# corre este archivo desde la consola de esta forma..| python  maquina.py
import easygui as eg
import sys

dinero = 0
montos = [50, 100, 200, 500, 1000, 1000, 2000, 5000, 10000]
cantidades = [10, 10, 10, 10, 0, 0, 0, 0, 0]
productos = ["dulce\n200","chocolatina\n2500","gaseosa\n1200"]
precios = [200, 2500, 1200]

imagenes = ["""
       ___      .-""-.      ___ 
       \  "-.  /      \  .-"  / 
        > -=.\/        \/.=- <  
        > -='/\        /\'=- <  
       /__.-'  \      /  '-.__\ 
                '-..-'          
""", """
    ___  ___  ___  ___  ___.---------------.     
  .'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \    
  |\/ __\/ __\/ __\/ __\/ _:\   |:.  \  \___ \   
   \\'\__\'\__\'\__\'\__\'\_`.__|  `. \  \___ \  
    \\/ __\/ __\/ __\/ __\/ __:                \ 
     \\'\__\'\__\'\__\ \__\'\_;-----------------`
      \\/   \/   \/   \/   \/ :                 |
       \|______________________;________________|
""", """
            __        
        .-"`` _``"-.  
       /'.   '.(##)'\ 
       |  `'----'`  | 
       |        ----| 
       |        . .-| 
       | .::::. |_| | 
       |::::''':.-. | 
       |;,,;;;;;|_|_| 
       | ';;;;' . . | 
       |        |_|_| 
       |        .-. | 
       \        |_|_/ 
        `.________.'  
"""]

def comprobar_devuelta(devuelta, montos, cantidades):

    total = 0
    
    for i in range(len(montos)):
        total += montos[i] * cantidades[i]
    
    if total > devuelta:
        return True
    else:
        return False

while 1:
    title = "Maquina Morada"
    eg.msgbox("Bienvenido a la maquina morada!", title)
        
    msg = "cuánto dinero ingresaras?"
    dinero += eg.integerbox(msg, title, upperbound = 10000)
    
    msg = "elige un producto" + "\tdinero: " + str(dinero)
    respuesta = eg.buttonbox(msg,choices=productos, title = title)
    
    iproducto = productos.index(respuesta)
    devuelta = dinero - precios[iproducto]
    
    if devuelta < 0:
        devuelta_str = str(dinero)
        eg.msgbox("no tiene suficiente dinero!", title)
    else:
        if comprobar_devuelta(devuelta, montos, cantidades):
            devuelta_str = str(devuelta)
            dinero = devuelta
            print(imagenes[iproducto])
            # devuelta_str = devolver()
        else:
          devuelta_str = str(dinero)
          eg.msgbox("la maquina no tiene suficiente dinero para devolverte!", title)
    
    msg = "Deseas continuar comprando?"
    if eg.ccbox(msg, title):     # muestra la ventana de  Continue/Cancel
        pass  # si el usuario continua
    else:
        eg.msgbox("devuelta: " + devuelta_str, title)
        sys.exit(0)           # si elije cancelar
        