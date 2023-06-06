import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox


targetUrl = "https://news.ycombinator.com/"
urls = []

def makeRequest(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def value_exists(value, list_of_dicts):
    for dictionary in list_of_dicts:
        if value in dictionary.values():
            return True
    return False
def crawler(url):
    links = makeRequest(url)
    for link in links.find_all('a', href=True):
        foundedLink=link.get('href')
        if link.get('href') !="https://news.ycombinator.com/" and "https" in link.get('href'):
            if not value_exists(foundedLink,urls):
                urls.append({"url":foundedLink, "title":link.text})
                if len(urls)>=30:
                    break
                print(link.text)
    return urls

def saveNotes():
    url = myEntry.get()
    if url=='':
        messagebox.showinfo("Error", "Please fill all required fields")
    else:
        try:
            links = makeRequest(url)
            for link in links.find_all('a', href=True):
                foundedLink = link.get('href')
                if link.get('href') != "https://news.ycombinator.com/" and "https" in link.get('href'):
                    if not value_exists(foundedLink, urls):
                        urls.append({"url": foundedLink, "title": link.text})
                        if len(urls) >= 30:
                            break
            for url in urls:
                my_text.insert("1.0", url["url"] +"\n")
        except:
            messagebox.showinfo(title="Error", message=f"{url} ")
#result = crawler(targetUrl)
# print(result)
# print(len(result))

window = Tk()
window.title("Python TkInter")
window.minsize(width=700,height=720)
canvas = Canvas(height=128, width=128)
logo = PhotoImage(file="logopy.png")
canvas.create_image(50,50,image=logo)
canvas.pack()

#Label
myLabel = Label(
    text="Enter WebSite URL",
    font=('Arial', 12, "normal"),
    fg="black"
)
myLabel.focus()
myLabel.place(x=250, y=100)
myEntry = Entry(width=40)
myEntry.focus()
myEntry.place(x=230, y= 130)
myLabel3 = Label(
    text="Collected Links",
    font=('Arial', 12, "normal"),
    fg="black"
)
myLabel3.place(x=250, y=160)
my_text = Text(window, width=75, height=30)
my_text.place(x=50, y=190)

saveButton = Button(text="Collect Links",command=saveNotes)
saveButton.place(x=300, y= 680)
window.mainloop()
