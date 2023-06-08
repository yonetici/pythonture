from tkinter import *
from tkinter import messagebox
import base64
from cryptography.fernet import Fernet
def encrpytText(message, secretKey):
    key = base64.b64encode(f"{secretKey:<32}".encode("utf-8"))
    encryptor = Fernet(key=key)
    encrypted = encryptor.encrypt(
        message.encode("utf-8")
    )
    return encrypted

def dcryptText(decryptedMessage, secretKey):
    key = base64.b64encode(f"{secretKey:<32}".encode("utf-8"))
    encryptor = Fernet(key=key)
    result = encryptor.decrypt(decryptedMessage).decode("utf-8")
    return result

#Save Secret Note
def saveNotes():
    title = myEntry.get()
    message = my_text.get("1.0",END)
    secretKey = myEntry1.get()

    if title == '' or message =='' or secretKey == '':
        messagebox.showinfo(title="Attention", message="An error occured, fill the required fields.")
    else:
        encryptedText = encrpytText(message, secretKey)
        try:
            with open("secret.txt", "a") as myFile:
                myFile.write(f"\n{title}\n{encryptedText}")
        except FileNotFoundError:
            with open("secret.txt", "w") as myFile:
                myFile.write(f"\n{title}\n{encryptedText}")
        finally:
            myEntry.delete(0,END)
            myEntry1.delete(0,END)
            my_text.delete("1.0",END)

def decryptMessage():
    message = my_text.get("1.0",END)
    message = bytes(message[2: -1], 'utf-8')
    secretKey = myEntry1.get()

    if message=='' or secretKey == '':
        messagebox.showinfo("Error", "Please fill all required fields")
    else:
        try:
            decryptText = dcryptText(message,secretKey)
            my_text.delete("1.0", END)
            my_text.insert("1.0", decryptText)
        except:
            messagebox.showinfo(title="Error", message=f"{message} ve {secretKey}")



window = Tk()
window.title("Python TkInter")
window.minsize(width=250,height=500)
canvas = Canvas(height=128, width=128)
logo = PhotoImage(file="secretlogopy.png")
canvas.create_image(50,50,image=logo)
canvas.pack()

#Label
myLabel = Label(
    text="Enter Your Title",
    font=('Arial', 12, "normal"),
    fg="black"
)
myLabel.focus()
myLabel.place(x=50, y=100)

myEntry = Entry(width=20)
myEntry.focus()
myEntry.place(x=50, y= 130)

myLabel2 = Label(
    text="Enter Your Secret",
    font=('Arial', 12, "normal"),
    fg="black"
)

myLabel2.place(x=50, y=160)
my_text = Text(window, width=20, height=6)
my_text.place(x=50, y=190)


myLabel3 = Label(
    text="Enter Your Master Key",
    font=('Arial', 12, "normal"),
    fg="black"
)

myLabel3.place(x=50, y=300)

myEntry1 = Entry(width=20)
myEntry1.focus()
myEntry1.place(x=50, y= 330)

saveButton = Button(text="Save & Encrypt",command=saveNotes)
saveButton.place(x=60, y= 360)
decryptButton = Button(text="Decrypt",command=decryptMessage)
decryptButton.place(x=70, y= 390)
# #Label
# my_text = Text(width=20, height=10)
# my_text.place(x=50, y=230)
# #Entry
# myEntry = Entry(width=20)
# myEntry.focus()
# myEntry.place(x=50, y= 130)
#
# myEntry2 = Entry(width=20)
# myEntry2.place(x=50, y= 190)
# def buttonClicked():
#     userBMI = round(int(myEntry.get()) / pow(int(myEntry2.get())/100,2),1)
#     messagebox.showinfo("Your BMI Index", userBMI)
# #Button
# myButton = Button(window, text="Calculate", command=buttonClicked)
# myButton.config(padx=5, pady=5)
# myButton.place(x = 80, y = 210)

window.mainloop()
