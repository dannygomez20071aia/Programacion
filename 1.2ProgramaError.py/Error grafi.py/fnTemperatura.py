import tkinter as tk
def btnConvertir(ventana,resultado, r1):
    tk.Button(
ventana,
text="Transformar",

command=lambda: resultado.delete(0,tk.END)or (resultado.insert(
0,
str(
f"Son {(float(r1.get() if r1.get() else 0)
* 1.8)+32} grados Fahrenheit"
)
))
).pack()