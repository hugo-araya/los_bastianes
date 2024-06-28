import tkinter as tk
from tkinter import ttk 
from PIL import Image as itk

ventana = tk.Tk()
imagen = tk.PhotoImage(file = 'cafe.png')
fondo = ttk.Label(ventana, image = imagen)
fondo.pack()

ventana.mainloop()