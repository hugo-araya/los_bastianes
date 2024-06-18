from tkinter import *
from tkinter import ttk

def mensaje():
    print("Desde el boton....")

ventana = Tk()
etiqueta = ttk.Label(ventana, text="Hola Mundo!")
etiqueta.grid(column=0, row=0)

boton = ttk.Button(ventana, text="Salir", command=ventana.destroy)
boton.grid(column=1, row=0)

etiqueta1 = ttk.Label(ventana, text="Chao Mundo!")
etiqueta1.grid(column=0, row=1)

boton1 = ttk.Button(ventana, text="Chao", command = mensaje)
boton1.grid(column=1, row=1)

ventana.mainloop()