import tkinter as tk
from tkinter import messagebox, simpledialog

class ControlProApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTROL PRO - Gestión Financiera")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        # Datos
        self.ingresos = []
        self.egresos = []
        self.contra = "CONTROLPRO1313"

        # --- Interfaz Gráfica ---
        tk.Label(root, text="CONTROL PRO", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)
        
        # Botones Principales
        self.btn_ingreso = tk.Button(root, text="Agregar Ingreso", width=25, command=self.agregar_ingreso, bg="#d4edda")
        self.btn_ingreso.pack(pady=10)

        self.btn_egreso = tk.Button(root, text="Agregar Egreso", width=25, command=self.agregar_egreso, bg="#f8d7da")
        self.btn_egreso.pack(pady=10)

        self.btn_resumen = tk.Button(root, text="Ver Resumen Mensual", width=25, command=self.ver_resumen, bg="#cce5ff")
        self.btn_resumen.pack(pady=10)

        self.btn_salir = tk.Button(root, text="Salir del Sistema", width=25, command=self.confirmar_salida, bg="#e2e3e5")
        self.btn_salir.pack(pady=10)

        # Área de historial rápido
        tk.Label(root, text="Movimientos recientes:", bg="#f0f0f0").pack(pady=(20, 0))
        self.historial = tk.Listbox(root, width=40, height=8)
        self.historial.pack(pady=5)

    def agregar_ingreso(self):
        valor = simpledialog.askstring("Ingreso", "Monto del ingreso:")
        if valor:
            try:
                monto = float(valor)
                if monto < 0:
                    messagebox.showerror("Error", "No se permiten valores negativos")
                else:
                    self.ingresos.append(monto)
                    self.historial.insert(0, f"Ingreso: +${monto:.2f}")
                    messagebox.showinfo("Éxito", "Ingreso registrado correctamente")
            except ValueError:
                messagebox.showerror("Error", "Ingrese solo números")

    def agregar_egreso(self):
        valor = simpledialog.askstring("Egreso", "Monto del egreso:")
        if valor:
            try:
                monto = float(valor)
                if monto < 0:
                    messagebox.showerror("Error", "No se permiten valores negativos")
                else:
                    self.egresos.append(monto)
                    self.historial.insert(0, f"Egreso: -${monto:.2f}")
                    messagebox.showinfo("Éxito", "Egreso registrado correctamente")
            except ValueError:
                messagebox.showerror("Error", "Ingrese solo números")

    def ver_resumen(self):
        totingresos = sum(self.ingresos)
        totegresos = sum(self.egresos)
        balance = totingresos - totegresos
        
        mensaje = f"Total Ingresos: ${totingresos:.2f}\n"
        mensaje += f"Total Egresos: ${totegresos:.2f}\n"
        mensaje += f"Balance Final: ${balance:.2f}\n"
        mensaje += "-"*30 + "\n"

        if totingresos > 0:
            porcentaje = (totegresos / totingresos) * 100
            mensaje += f"Los egresos representan el {porcentaje:.2f}%\n"
            
            if porcentaje < 50:
                mensaje += "Análisis: Excelente control"
            elif 50 <= porcentaje <= 80:
                mensaje += "Análisis: Buen control financiero"
            elif 80 < porcentaje <= 100:
                mensaje += "Análisis: Alerta: gastos muy altos"
            else:
                mensaje += "Análisis: Peligro: Gastas más de lo que ganas"
        else:
            mensaje += "No hay ingresos para análisis proporcional."

        messagebox.showinfo("Resumen Mensual", mensaje)

    def confirmar_salida(self):
        intentos = 3
        while intentos > 0:
            clave = simpledialog.askstring("Seguridad", f"Ingrese contraseña para salir (Intentos: {intentos}):", show='*')
            if clave == self.contra:
                messagebox.showinfo("Adiós", "Gracias por usar CONTROL PRO")
                self.root.destroy()
                return
            else:
                intentos -= 1
                if intentos > 0:
                    messagebox.showwarning("Error", "Contraseña incorrecta")
                else:
                    messagebox.showerror("Error", "Acceso denegado")

# Iniciar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlProApp(root)
    root.mainloop()