turno = 0
goles0 = goles1 = 0
faltantes0 = faltantes1 = 5
ganador = -1

while ganador == -1: #mientras nadie gane o la serie no termine
    if turno == 0: #turno del equipo0
        gol = input("\nmetio gol el equipo 0? ")
        if gol == "si":
            goles0 += 1 #si hubo gol incremento los goles del equipo respectivo
        faltantes0 -= 1 #meta o no gol le disminuyo a los tires faltantes
        if goles1 + faltantes1 < goles0: #si se cumple esto ya gané
            ganador = 0
        turno = 1 #en la siguiente iteración le toca al equipo0
    else: #en este else se hace algo equivalente pero para el equipo1
        gol = input("metio gol el equipo 1? ")
        if gol == "si":
            goles1 += 1
        faltantes1 -= 1
        if goles0 + faltantes0 < goles1:
            ganador = 1
        turno = 0
            
    if faltantes0 == faltantes1 == 0 and goles0 == goles1: #si la serie termina en empate
        ganador = 3

print(ganador) #prueba, esta linea no quedará en el algoritmo final
        

            
        
