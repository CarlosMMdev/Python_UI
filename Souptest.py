from bs4 import BeautifulSoup
from tkinter import messagebox

#Read HTML file and create the soup
with open(r"C:\Users\jmora\Escritorio\Python\Testing PCF files\submit.html") as submit_file:
    soup = BeautifulSoup(submit_file, "html.parser")
    # soup = soup.prettify()


# print(soup.label(attrs={"for": "title"}))


# tag = soup.find("trans", text="request.title")
# print(tag.find_parent("div"))

title_tag = soup.find("trans", string ="request.title")
# title_tag.find_parents("div")
# messagebox.showinfo(message=title_tag, title="Título")
print(title_tag)







