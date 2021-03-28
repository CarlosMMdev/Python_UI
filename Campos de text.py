#Campos de texto en Tkinter

from tkinter import *
from tkinter import ttk


root = Tk()
root.title("PCF Creator")
# root.config()

#Creating TabControl object and declaring tabs
tabControl = ttk.Notebook(root, width = 480, height = 320)

HowToUseTab = ttk.Frame(tabControl)
submitTab = ttk.Frame(tabControl)
projectdataTab = ttk.Frame(tabControl)
fielddefTab = ttk.Frame(tabControl)
labelxmlTab = ttk.Frame(tabControl)

tabControl.add(HowToUseTab, text = "How to use")
tabControl.add(submitTab, text = "submit.html")
tabControl.add(projectdataTab, text = "projectdata.html")
tabControl.add(fielddefTab, text = "fieldDef.xml")
tabControl.add(labelxmlTab, text = "labelXML.js")

tabControl.pack(expand = 1, fill = "both")


# Tab How to use

title_label = Label(HowToUseTab, text = "Welcome to PCF Creator", font=("Consolas", 24))
title_label.pack()

# Tab submit.html

Label(submitTab, text = "Choose the fields that you want to delete:").pack(anchor=NW)

#Variables for the Checkbuttons

submit_title = StringVar(submitTab, "0")
submit_dateRequested = StringVar(submitTab, "0")
submit_targetAudience = StringVar(submitTab, "0")
submit_quoteRequired = StringVar(submitTab, "0")
submit_submittedBy = StringVar(submitTab, "0")

# submit.html checkbuttons 

Checkbutton(submitTab, text = "Title", variable = submit_title, onvalue = 1, offvalue = 0).pack(anchor=NW)
Checkbutton(submitTab, text = "Date requested", variable = submit_dateRequested, onvalue = 1, offvalue = 0).pack(anchor=NW)
Checkbutton(submitTab, text = "Target audience", variable = submit_targetAudience, onvalue = 1, offvalue = 0).pack(anchor=NW)
Checkbutton(submitTab, text = "Quote Required", variable = submit_quoteRequired, onvalue = 1, offvalue = 0).pack(anchor=NW)
Checkbutton(submitTab, text = "Submitted By", variable = submit_submittedBy, onvalue = 1, offvalue = 0).pack(anchor=NW)



root.mainloop()