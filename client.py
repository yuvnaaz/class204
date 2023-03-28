import socket 
from threading import Thread
from PIL import ImageTk, Image
from tkinter import *
screenwidth = None
screenheight = None
server = None
ip = None 
port = None
canvas1 = None 
playername = None
nameEntry = None
namewindow = None
def savename():
    global server
    global playername
    global nameEntry
    global namewindow
    playername = nameEntry.get()
    nameEntry.delete(0,END)
    namewindow.destroy()
    server.send(playername.encode())
def askPlayerName():
    global canvas1
    global screenwidth
    global screenheight
    global playername
    global nameEntry
    global namewindow
    namewindow = Tk()
    namewindow.title("Lan Game")
    screenwidth = namewindow.winfo_screenwidth()
    screenheight = namewindow.winfo_screenheight()
    namewindow.configure(width = screenwidth, height = screenheight)
    bg = ImageTk.PhotoImage(file = "./assts/background.png")
    canvas1 = Canvas(namewindow, width = 500, height = 500, )
    canvas1.create_image(0,0, image = bg, anchor = "nw")
    canvas1.create_text(screenwidth/2, screenheight/5, text = "Enter Name", font = ("Chalkboard SE", 50), fill = "white")
    nameEntry = Entry(namewindow, width = 15, justify = "center", font = ("Chalkboard SE", 50), bd = 5, bg = "white")
    nameEntry.place(x = screenwidth/2 -220, y = screenheight/4 + 100)
    button = Button(namewindow, text = "save", font =  ("Chalkboard SE", 50), height = 2, bd = 3, bg = "blue", command = savename)
    button.place(x = screenwidth/2-130, y = screenheight/2 -30)
    namewindow.mainloop()

def setup():
    global server
    global ip 
    global port

    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    askPlayerName()






setup()