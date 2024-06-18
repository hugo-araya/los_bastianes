import tkinter as tk
from tkinter import ttk

def funcion_click():
    accion.configure(text='** Has hecho Click! **', )
    etiqueta.configure(foreground = 'red')

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("Hola Mundo")

    etiqueta = ttk.Label(ventana, text = "Hola raton con cola")
    etiqueta.grid(column = 0, row = 0)

    accion = ttk.Button(ventana, text = 'Click', command = funcion_click)
    accion.grid(column = 1, row =0)

    ventana.mainloop()