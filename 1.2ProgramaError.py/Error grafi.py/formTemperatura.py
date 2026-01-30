import tkinter as tk 

#########funciones
#def btnConvertirF():
import tkinter as tk
import fnTemperatura
ventana = tk.Tk()
ventana.title("Grados Centigrados a Fahrenheit")
ventana.geometry("400x400")
tk.Label(ventana,text="Ingrese en Grados Centigrados ").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana,text="Resultado en Fahrenheit" ).pack()
resultado = tk.Entry(ventana)
resultado.pack()
fnTemperatura.btnConvertir(ventana,resultado, entrada1)
ventana.mainloop()
#########parte visual
ventana=tk.Tk()
ventana.geometry("300x300")
ventana.title("CONVERTIDOR TEMPERATURA")

lblIngreseCentigrados=tk.Label(text="Ingrese la temperatura en Grados Centigrados")
lblIngreseCentigrados.pack()

txtCentigrados=tk.Entry()
txtCentigrados.pack()

btnConvertir=tk.Button(text="CONVERTIR A FARENHEIT")
btnConvertir.pack()

lblResultado=tk.Label(text="...")
lblResultado.pack()

ventana.mainloop()