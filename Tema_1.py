from tkinter import *


root = Tk()
root.title("Mi primera interfaz gráfica")
# root.resizable(0,0)
# root.iconbitmap([NOMBRE ICO])

frame = Frame(root)
frame.pack(fill = "both", expand = 1)
frame.config(width = 420, height = 420, bg = "blue", bd =20, relief = "sunken")
my_label = Label(frame, text= "Hola, usuario.")
my_label.pack()










root.mainloop()