from tkinter import *
from tkinter import messagebox

inentos = 3

def accion():
    global intentos
    
    # Definimos el usuario y contraseña correctos
    user_correcto = "Danny"
    pass_correcto = "1234" # Puedes cambiar esto
    
    # Obtenemos lo que escribió el usuario
    u = entry2.get()
    p = entry3.get()
    
    if u == user_correcto and p == pass_correcto:
        messagebox.showinfo("ÉXITO", "Bienvenido Danny. Abriendo carta...")
        root.destroy() # Cerramos la ventana de login
        # Aquí llamarías a tu función de la animación del corazón
    else:
        intentos -= 1
        if intentos > 0:
            messagebox.showwarning("ERROR", f"Datos incorrectos.\nTe quedan {intentos} intentos")
            # Limpiamos las cajas para reintentar
            entry2.delete(0, END)
            entry3.delete(0, END)
        else:
            messagebox.showerror("BLOQUEADO", "Has agotado los intentos.")
            root.destroy() # Cerramos el programa por seguridad


root = Tk()
root.title("FIRST")
root.geometry("400x400")

Lbl = Label(root, text="HELLO WORLD")
Lbl.grid()

root.config(bd=15)

usuario = Label(root, text="USER")
usuario.grid(row=1, column=0)

entry2 = Entry(root)
entry2.grid(row=1, column=1)

pasword = Label(root, text="PASWORD")
pasword.grid(row=2, column=0)
    
entry3 = Entry(root)
entry3.grid(row=2, column=1)
entry3.config(show="/")

boton = Button(root, text="HERE", command=accion)
boton.grid(row=3, column=1)

root.mainloop()




