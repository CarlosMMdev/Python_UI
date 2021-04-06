from bs4 import BeautifulSoup

#Read HTML file and create the soup
with open(r"C:\Users\jmora\Escritorio\Python\Testing PCF files\submit.html") as submit_file:
    soup = BeautifulSoup(submit_file, "html.parser")
    # soup = soup.prettify()


# print(soup.label(attrs={"for": "title"}))


tag = soup.find("trans", text="request.title")
print(tag.find_parent("div"))