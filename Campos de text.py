#Campos de texto en Tkinter

from tkinter import *


root = Tk()
root.title("PCF Creator")
# root.config()

#Title frame and label
title_frame = Frame(root, width = 480, height = 320, bg="lightblue", bd="10")
title_frame.pack()

title_label = Label(title_frame, text = "Welcome to PCF Creator", font=("Consolas", 24))
title_label.pack()

#File to modify selection

intro_label = Label(root, text = "Choose the file that you want to modify:", font=("Consolas", 12))
intro_label.pack(anchor=W)

submit_file = StringVar()
submit_file.set(False)
projectdata_file = StringVar()
projectdata_file.set(False)

Checkbutton(root, text = "submit.html", variable = submit_file, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = "projectdata.html", variable = projectdata_file, onvalue = 1, offvalue = 0).pack()










root.mainloop()