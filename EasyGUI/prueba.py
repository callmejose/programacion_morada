# guarda este archivo como ......| prueba1.py
# corre este archivo desde la consola de esta forma..| python  prueba1.py
import easygui as eg
import sys

while 1:
    title = "Mensaje de prueba1.py"
    eg.msgbox("Hola, mundo!", title)

    msg ="Cuál es tu sabor favorito?"
    title = "Encuesta sobre helado"
    choices = ["Vanilla", "Chocolate", "Fresa", "Brownie"]
    choice = eg.choicebox(msg, title, choices)

    # note que se convirtio la variable choice a string,
    # si el usuario cancela la variable choice contendra "None".
    eg.msgbox("Tu elección: " + str(choice), "resultado de la encuesta")

    msg = "Deseas continuar?"
    title = "Porfavor confirma"
    if eg.ccbox(msg, title):     # muestra la ventana de  Continue/Cancel
        pass  # si el usuario continua
    else:
        sys.exit(0)           # si elije cancelar