from tkinter import *
from os import *
from PIL import Image, ImageTk

root = Tk()

# hier wird das Bild über Image.open geladen und mit ImageTk aus
#  der Bibliothek PIL konvertiert. 
# Dazu muss Pillow installiert sein
# commands:  
#       -m pip install --upgrade pip --user
#       -m pip install --upgrade PIL

bild1 = ImageTk.PhotoImage(Image.open("test.jpg"))
panel1 = Label(root, image=bild1)
panel1.grid(row=0, column=0)

root.mainloop()