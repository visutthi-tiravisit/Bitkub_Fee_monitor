from importlib.resources import path
from logging import root
from tkinter import *
import tkinter
from numpy import append


root = tkinter.Tk()
root.title('Bitkub Fee monitor')
root.geometry("500x500")

e = Entry(root, width=60)
e.pack()

def Bitkub():
    from Bitkub_scrape import make_df
    make_df(e.get())
    Bitkub_label = Label(root,text="Done, Check file name: Bitkub_fee.csv")
    Bitkub_label.pack()
    #print(file_path)


Bitkub_button = Button(root,text="Get Bitkub Fee", command=Bitkub, height = 5, width = 60, bg="green") 
Bitkub_button.pack()

root.mainloop()


    
    