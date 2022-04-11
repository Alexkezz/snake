from tkinter import *


ventana = Tk()
ventana.title("Porva de teclas")

def mostrarhola(event):
    if event.keysym == "Down":
        print("Hola")

ventana.bind("<Down>", mostrarhola)

ventana.mainloop()