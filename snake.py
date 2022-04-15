from tkinter import *
import random

ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(0, 0)
ventana.title("SNAKE")
posx = 0
posy = 0
posicion_siguiente = ""

def mover_serpiente():
    global posx
    global posy
    if posicion_siguiente == "Right":
        if posx > 485:
            posx -= 510
        else:
            posx += 3
    elif posicion_siguiente == "Left":
        if posx < -25:
            posx += 510
        else:
            posx -= 3
    elif posicion_siguiente == "Up":
        if posy < -25:
            posy += 440
        else:
            posy -= 3
    elif posicion_siguiente == "Down":
        if posy > 415:
            posy -= 440
        else:
            posy += 3
    snake.place(x=posx, y=posy)
    ventana.after(10, mover_serpiente)

def direccion(event):
    global posicion_siguiente
    posicion_siguiente = event.keysym
     
ventana.bind("<Left>", direccion)
ventana.bind("<Right>", direccion)
ventana.bind("<Up>", direccion)
ventana.bind("<Down>", direccion)

menu = Frame(ventana, width=500, height=70, bg="#93c7ff", relief="solid", border=6)
menu.grid(row=0, column=0)
menu.grid_propagate(False)

border_color_mapa = Frame(ventana, width=500, height=430, bg="white")
border_color_mapa.grid(row=1, column=0, columnspan=1)

mapa = Frame(border_color_mapa, width=488, height=418, bg="#8dd55a")
mapa.place(x=6, y=6)

boton_iniciar = Button(menu, text="INICIAR", font=("Calibri", 12), bg="#9494c9", fg="white")
boton_iniciar.grid(row=0, column=0, padx=(50,20), pady=13)

boton_reiniciar = Button(menu, text="REINICIAR", font=("Calibri", 12), bg="#9494c9", fg="white")
boton_reiniciar.grid(row=0, column=1, pady=3)

puntos = Label(menu, text="CANTIDAD:", font=("Calibri", 13), fg="black", bg="#93c7ff")
puntos.grid(row=0, column=2, padx=(100,0))

snake = Frame(mapa, width=30, height=30, bg="green")
snake.place(x=0, y=0)

ventana.after(100, mover_serpiente)
ventana.mainloop()

