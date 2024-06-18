import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox

def funcion_boton():
    boton2.configure(text  = "--> Me apretastes <--" + " " + nombre.get(), state = tk.NORMAL)
    etiqueta.configure(foreground = 'red')

def funcion_boton3():
    if boton3['text'] == "Desactivar":
        boton3.configure(text = 'Activar')
    else:
        boton3.configure(text = 'Desactivar')
    if (str(boton2['state']) == "normal"):
        boton2.configure(state = tk.DISABLED)
    else:
        boton2.configure(state = tk.NORMAL)

def funcion_boton4(numero):
    print(numero)

def funcion_boton5(numero):
    # mBox.showinfo("Mensaje ","Este es el numero aleatorio: " + str(numero))
    # mBox.askokcancel("Mensaje ","Este es el numero aleatorio: " + str(numero))
    mBox.askyesnocancel("Mensaje ","Este es el numero aleatorio: " + str(numero))

if __name__ == '__main__':
    # Inicializar la ventana
    ventana = tk.Tk()
    ventana.title("Hola ventana al mundo")
    ventana.geometry('300x400+400+300')
    #ventana.config(width=400, height=300)
    ventana.resizable(0,0)

    # Agregar una etiqueta
    etiqueta = ttk.Label(ventana, text = 'Buenos dias mundo!!!')
    etiqueta.grid(column = 0, row = 0)

    # Agregar un boton
    boton1 = ttk.Button(ventana, text ="Presiona aqui!!!")
    boton1.grid(column = 0, row = 1)

    # Agregar un boton con accion
    boton2 = ttk.Button(ventana, text ="Apreta aqui!!!", state = tk.NORMAL, command = funcion_boton)
    boton2.grid(column = 0, row = 2)

    # Agregar caja de texto
    nombre = tk.StringVar()
    preguntar = ttk.Entry(ventana, width = 20, textvariable = nombre)
    preguntar.grid(column = 0, row = 3)

    # Agregar un boton con accion desactivar
    boton3 = ttk.Button(ventana, text ="Desactivar", command = funcion_boton3)
    boton3.grid(column = 0, row = 4)

    # Agregar un boton con accion y paso de parametros
    boton4 = ttk.Button(ventana, text ="Envia parametros", command = lambda: funcion_boton4(random.randint(0, 10)))
    boton4.grid(column = 0, row = 5)

    # Agregar un boton con accion, paso de parametros y muestra un messagebox
    boton5 = ttk.Button(ventana, text ="Parametro con mensaje", command = lambda: funcion_boton5(random.randint(0, 10)))
    boton5.grid(column = 0, row = 6)

    # Acrivar el foco del objeto principal
    preguntar.focus()

    # Activar la ventana
    ventana.mainloop()