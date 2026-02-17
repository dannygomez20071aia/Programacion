from tkinter import *

root = Tk()
#nombre de la ventana 
root.title("FIRST")
#tamaño de la ventana 
root.geometry("400x400")
#texto dentro de la ventana 
Label = Label(root, text="HELLO WORLD")
Label.pack()

root.mainloop()
# con .pack y . mainloop permitevisualizar el texto 
