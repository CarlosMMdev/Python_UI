#Campos de texto en Tkinter

from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup


# def show_tag():
#     print(soup.label['for'] = 'title')
#     return




root = Tk()
root.title("PCF Creator")

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
title_label.grid()

# Tab submit.html
introFrame = Frame(submitTab)
introFrame.grid()

#IntroFrame
Label(introFrame, text = "Choose the fields that you want to delete:").grid(sticky = W)

#Variables for the Checkbuttons
submit_title = StringVar(submitTab, "0")
submit_dateRequested = StringVar(submitTab, "0")
submit_targetAudience = StringVar(submitTab, "0")
submit_quoteRequired = StringVar(submitTab, "0")
submit_ReferenceProjectNumber = StringVar(submitTab, "0")
submit_ServicesList = StringVar(submitTab, "0")
submit_TranslateFrom = StringVar(submitTab, "0")
submit_TranslateInto = StringVar(submitTab, "0")
submit_TargetDate = StringVar(submitTab, "0")
submit_PurchaseOrder = StringVar(submitTab, "0")
submit_submittedBy = StringVar(submitTab, "0")
submit_SendBackOriginal = StringVar(submitTab, "0")

# submit.html checkbuttons 
FieldsFrame = Frame(submitTab)
FieldsFrame.grid()

Checkbutton(FieldsFrame, text = "Title", variable = submit_title, onvalue = 1, offvalue = 0, command = show_tag()).grid(column = 1, row = 1, sticky = W, pady = 10)
Checkbutton(FieldsFrame, text = "Date requested", variable = submit_dateRequested, onvalue = 1, offvalue = 0).grid(column = 2, row = 1, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Target audience", variable = submit_targetAudience, onvalue = 1, offvalue = 0).grid(column = 3, row = 1, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Quote required", variable = submit_quoteRequired, onvalue = 1, offvalue = 0).grid(column = 1, row = 2, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Reference project number", variable = submit_ReferenceProjectNumber, onvalue = 1, offvalue = 0).grid(column = 2, row = 2, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Services list", variable = submit_ServicesList, onvalue = 1, offvalue = 0).grid(column = 3, row = 2, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Translate from", variable = submit_TranslateFrom, onvalue = 1, offvalue = 0).grid(column = 1, row = 3, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Translate into", variable = submit_TranslateInto, onvalue = 1, offvalue = 0).grid(column = 2, row = 3, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Target date", variable = submit_TargetDate, onvalue = 1, offvalue = 0).grid(column = 3, row = 3, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Purchase order", variable = submit_PurchaseOrder, onvalue = 1, offvalue = 0).grid(column = 1, row = 4, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Submitted By", variable = submit_submittedBy, onvalue = 1, offvalue = 0).grid(column = 2, row = 4, sticky = W,pady = 10)
Checkbutton(FieldsFrame, text = "Send back original", variable = submit_SendBackOriginal, onvalue = 1, offvalue = 0).grid(column = 3, row = 4, sticky = W,pady = 10)

#Delete button
DeleteBtnFrame = Frame(submitTab)
DeleteBtnFrame.grid()

DeleteBtn = Button(DeleteBtnFrame, text = "Delete fields")
DeleteBtn.grid( pady = "12px")

#Read HTML file and create the soup
with open(r"C:\Users\jmora\Escritorio\Python\Testing PCF files\submit.html") as submit_file:
    soup = BeautifulSoup(submit_file, "html.parser")
    soup = soup.prettify()



#Text box for preview HTML
preview = Text(submitTab, width = "250")
submitTab.grid_columnconfigure(0, weight=1)
preview.insert(END, soup)
preview.grid(row = 6, sticky = "NE" )


root.mainloop()