# Texto estático
etiqueta = tk.Label(root, text="Introduce algo:")
etiqueta.pack()

# Cuadro para escribir
entrada = tk.Entry(root)
entrada.pack()

# Para insertar texto por código en el cuadro:
entrada.insert(0, "Texto por defecto")