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
    r1=random.randint(0,25)
    r2=random.randint(0,25)
    r3=random.randint(0,25)
    r4=random.randint(0,25)
    r5=random.randint(0,25)
    
    
    
    lucky=letters[r1]+letters[r2]+letters[r3]+letters[r4]+letters[r5]
    print(lucky)
    resultlbl["text"]=lucky

btn=Button(root,text="Make a random word today!", command=find)
btn.place(relx=0.5, rely=0.65, anchor=CENTER)


root.mainloop()