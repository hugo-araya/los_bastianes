import tkinter as tk
from tkinter import ttk

def funcion_click():
    etiqueta.configure(text='Hola ' + nombre.get())

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("Hola Mundo")

    etiqueta = ttk.Label(ventana, text = "Hola raton con cola")
    etiqueta.grid(column = 0, row = 0)

    nombre = tk.StringVar()
    preguntar_nombre = ttk.Entry(ventana, width = 20, textvariable = nombre)
    preguntar_nombre.grid(column = 0, row = 1)

    accion = ttk.Button(ventana, text = 'Click', command = funcion_click)
    accion.grid(column = 1, row =1)

    ventana.mainloop()