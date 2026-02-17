import tkinter as tk 
ventna = tk.Tk()
ventna.title("FIRST WINDOW")
ventna.geometry("400x400")

input_usu = tk.Entry(ventna)
input_usu.pack()

def INSERT():
    tot= input_usu.get()
    print(tot)
boton = tk.Button(ventna, text="INSERT", command=INSERT)
boton.pack()



ventna.mainloop()