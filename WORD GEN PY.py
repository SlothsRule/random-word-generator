from tkinter import *

import random

root=Tk()
root.geometry("300x300")
root.title("Random word maker")

letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(letters)

resultlbl=Label(root)
resultlbl.place(relx=0.5, rely=0.5, anchor=CENTER)

def find():
    r=random.random(0,26)
    lucky=letters[r]
    print(lucky)
    resultlbl["text"]=lucky

btn=Button(root,text="Make a random word today!", command=find)
btn.place(relx=0.5, rely=0.65, anchor=CENTER)


root.mainloop()