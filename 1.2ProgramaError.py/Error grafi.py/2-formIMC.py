import tkinter as tk

#*********FUNCIONES********

#*********PARTE VISUAL*****
ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("imc")
lblIngresePeso=tk.Label(text="Ingrese su peso en kilos")
lblIngresePeso.pack()
txtPeso=tk.Entry()
txtPeso.pack()
lblErrorPeso=tk.Label(text="",fg="red")
lblErrorPeso.pack()
lblIngreseEstatura=tk.Label(text="Ingrese su estatura en centimetros")
lblIngreseEstatura.pack()
txtEstatura=tk.Entry()
txtEstatura.pack()
lblErrorEstatura=tk.Label(text="",fg="red")
lblErrorEstatura.pack()
btnIMC=tk.Button(text="CALCULAR IMC")
lblIMC=tk.Label(text="Su IMC es:",fg="blue")
lblIMC.pack()
lblInterpretacion=tk.Label(text="",fg="blue")
lblInterpretacion.pack()
ventana.mainloop()
