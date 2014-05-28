#ejemplo while

respuesta = "no"
while respuesta != "si":
    respuesta = input("Te gusta Python? ")
    if respuesta == "si":
       print ("Eso es genial!")
    else:
       print ("Esa no es la respuesta correcta! Intentalo otra vez.")
