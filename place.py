from tkinter import *
from tkinter import ttk
top = Tk()

L1 = ttk.Label(top, text="Physics")
L1.place(x=300,y=10)

E1 = ttk.Entry(top)
E1.place(x=60,y=10)

L2=ttk.Label(top,text="Maths")
L2.place(x=10,y=50)

E2=ttk.Entry(top)
E2.place(x=60,y=50)

L3=ttk.Label(top,text="Total")
L3.place(x=10,y=150)

E3=ttk.Entry(top)
E3.place(x=60,y=150)

B = ttk.Button(top, text ="Add")
B.place(x=100, y=100)

top.geometry("300x250+10+10")
top.mainloop()