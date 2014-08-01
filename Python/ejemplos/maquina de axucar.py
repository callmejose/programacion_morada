precios = [3000, 1200, 45900, 4900, 5050, 5100, 99950, 150] #vector de precios de productos
productos = ("1.gaseosa\t3000\n 2.chocolatina\t1200\n 3.caramelo raro\t45900\n" + 
            " 4.nutella\t4900\n 5.nutella blanca\t5050\n 6.nutella edición limitada\t5100\n" +
            " 7.donación\t99950\n 8.menta\t150")
montos = [50, 100, 200, 500, 1000, 1000, 2000, 5000, 10000, 20000, 50000, 1000000] #montos que manejamos en monedas y billetes
cantidades = [200, 200, 200, 100, 200, 200, 200, 200, 100, 50, 0] #cantidades que tenemos de cada monto
variable=1
fondos=0
caja=0
seguir="si"

fondos = int(input("\ningrese fondos: "))
seguir = input("\n¿va a seguir metiendo fondos?(si/no): ")
while seguir == "si":
    fondos += int(input("\nmeta más fondos: "))
    seguir=input("\n¿va a seguir metiendo fondos?(si/no): ")

print("\nsu fondo es de: ", fondos)
print("\n",productos)
productoquiere=int(input("\ningrese el número del pruducto: "))
precioproducto=precios[productoquiere-1]
faltatantaplata=precioproducto-fondos

if fondos >= precioproducto:
    alcanza="si"
else:
    alcanza="no"

devuelta = fondos - precioproducto

if alcanza=="no":
    print("\nle faltan",(faltatantaplata))
    devuelta = fondos

for i in range(len(cantidades)):
    if devuelta >= montos[i]:
        caja += montos[i] * cantidades[i]
if caja < devuelta:
    caja = fondos


while devuelta != 0:
    for i in range(len(montos)-1):
        if devuelta >= montos[i] and devuelta < montos[i+1]:
            if cantidades[i] > 0:
                devuelta=devuelta-montos[i]
                cantidades[i]-=1
                print(montos[i])
                break
            else:
                while cantidades[i]==0:
                    i-=1
                devuelta-=montos[i]
                cantidades[i]-=1
                print(montos[i])
                break