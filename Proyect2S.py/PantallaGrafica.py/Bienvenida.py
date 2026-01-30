import tkinter as tk
from tkinter import messagebox

class ControlProApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTROL PRO - Gestión Financiera")
        self.root.geometry("400x450")

        # Datos
        self.ingresos = []
        self.egresos = []
        self.contra = "CONTROLPRO1313"

        # --- Interfaz Principal ---
        tk.Label(root, text="CONTROL PRO", font=("Arial", 18, "bold")).pack(pady=15)

        tk.Button(root, text="Agregar Ingreso", width=25, command=self.ventana_ingreso).pack(pady=10)
        tk.Button(root, text="Agregar Egreso", width=25, command=self.ventana_egreso).pack(pady=10)
        tk.Button(root, text="Ver Resumen Mensual", width=25, command=self.ventana_resumen).pack(pady=10)
        tk.Button(root, text="Salir del Sistema", width=25, command=self.confirmar_salida).pack(pady=10)

        tk.Label(root, text="Movimientos recientes:").pack(pady=(20, 0))
        self.historial = tk.Listbox(root, width=40, height=8)
        self.historial.pack(pady=5)

    # ---------------- Ventanas ---------------- #

    def ventana_ingreso(self):
        win = tk.Toplevel(self.root)
        win.title("Agregar Ingreso")
        win.geometry("300x150")

        tk.Label(win, text="Monto del ingreso:").pack(pady=10)
        entrada = tk.Entry(win)
        entrada.pack()

        def guardar():
            try:
                monto = float(entrada.get())
                if monto < 0:
                    messagebox.showerror("Error", "No se permiten valores negativos")
                else:
                    self.ingresos.append(monto)
                    self.historial.insert(0, f"Ingreso: +${monto:.2f}")
                    messagebox.showinfo("Éxito", "Ingreso registrado")
                    win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Ingrese solo números")

        tk.Button(win, text="Guardar", command=guardar).pack(pady=15)

    def ventana_egreso(self):
        win = tk.Toplevel(self.root)
        win.title("Agregar Egreso")
        win.geometry("300x150")

        tk.Label(win, text="Monto del egreso:").pack(pady=10)
        entrada = tk.Entry(win)
        entrada.pack()

        def guardar():
            try:
                monto = float(entrada.get())
                if monto < 0:
                    messagebox.showerror("Error", "No se permiten valores negativos")
                else:
                    self.egresos.append(monto)
                    self.historial.insert(0, f"Egreso: -${monto:.2f}")
                    messagebox.showinfo("Éxito", "Egreso registrado")
                    win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Ingrese solo números")

        tk.Button(win, text="Guardar", command=guardar).pack(pady=15)

    def ventana_resumen(self):
        win = tk.Toplevel(self.root)
        win.title("Resumen Mensual")
        win.geometry("350x250")

        totingresos = sum(self.ingresos)
        totegresos = sum(self.egresos)
        balance = totingresos - totegresos

        mensaje = f"Total Ingresos: ${totingresos:.2f}\n"
        mensaje += f"Total Egresos: ${totegresos:.2f}\n"
        mensaje += f"Balance Final: ${balance:.2f}\n"
        mensaje += "-" * 30 + "\n"

        if totingresos > 0:
            porcentaje = (totegresos / totingresos) * 100
            mensaje += f"Egresos: {porcentaje:.2f}%\n"

            if porcentaje < 50:
                mensaje += "Análisis: Excelente control"
            elif porcentaje <= 80:
                mensaje += "Análisis: Buen control financiero"
            elif porcentaje <= 100:
                mensaje += "Análisis: Alerta: gastos altos"
            else:
                mensaje += "Análisis: Gastas más de lo que ganas"
        else:
            mensaje += "No hay ingresos registrados."

        tk.Label(win, text=mensaje, justify="left").pack(padx=15, pady=15)

    # ---------------- Seguridad ---------------- #

    def confirmar_salida(self):
        intentos = 3
        while intentos > 0:
            clave = tk.simpledialog.askstring(
                "Seguridad",
                f"Ingrese contraseña (Intentos: {intentos})",
                show="*"
            )
            if clave == self.contra:
                messagebox.showinfo("Adiós", "Gracias por usar CONTROL PRO")
                self.root.destroy()
                return
            intentos -= 1

        messagebox.showerror("Error", "Acceso denegado")

# Iniciar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlProApp(root)
    root.mainloop()