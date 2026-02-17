from tkinter import Tk, Label, Button
def mensaje():
    print("SMS THE BUTTON")

ventana = Tk()
ventana.geometry("400x400")
ventana.title("HELLO WORLD")

lbl = Label(ventana, text="THIS IS A LABEL")
lbl.pack()

btn = Button(ventana, text= "PRESS HERE", command=mensaje)
#fg = para letras
#bg = para el boton 
btn.config( bg="black", fg="white")
btn.pack()


ventana.mainloop()




