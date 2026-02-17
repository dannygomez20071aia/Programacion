import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

# Configuración del motor de gráficos
matplotlib.use("TkAgg")

class ControlProApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTROL PRO - Tech Edition")
        self.root.geometry("550x900")
        self.root.withdraw() 
        
        # PALETA DE COLORES (Psicología Tech-Enterprise)
        self.AZUL_FUERTE = "#3182CE"
        self.AZUL_CLARO = "#63B3ED"
        self.OSCURO_TECH = "#2D3748"
        self.AZUL_GELIDO = "#EBF8FF"
        self.BLANCO_PURO = "#FFFFFF"
        self.VERDE_EXITO = "#38A169"
        self.ROJO_ALERTA = "#E53E3E"

        self.ingresos, self.egresos = [], []
        self.usuario_actual = None
        self.contra_actual = None
        self.intentos_login = 0

        self.pantalla_registro()

    def pantalla_registro(self):
        self.reg_win = ctk.CTkToplevel(self.root)
        self.reg_win.title("Acceso Sistema")
        self.reg_win.geometry("480x620")
        self.reg_win.configure(fg_color=self.OSCURO_TECH)
        self.reg_win.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.reg_win.attributes("-topmost", True)

        ctk.CTkLabel(self.reg_win, text="⚡", font=("Arial", 40), text_color=self.AZUL_CLARO).pack(pady=(50, 0))
        ctk.CTkLabel(self.reg_win, text="CONTROL PRO", font=("Impact", 60), text_color=self.BLANCO_PURO).pack(pady=10)
        ctk.CTkLabel(self.reg_win, text="FINANZAS ORGANIZADAS, FUTURO ASEGURADO", font=("Segoe UI", 12, "bold"), text_color=self.AZUL_CLARO).pack(pady=(0, 40))

        self.user_entry = ctk.CTkEntry(self.reg_win, placeholder_text="Usuario", width=320, height=50, corner_radius=12, border_color=self.AZUL_FUERTE, fg_color=self.BLANCO_PURO, text_color=self.OSCURO_TECH)
        self.user_entry.pack(pady=10)
        self.pass_entry = ctk.CTkEntry(self.reg_win, placeholder_text="Contraseña", show="*", width=320, height=50, corner_radius=12, border_color=self.AZUL_FUERTE, fg_color=self.BLANCO_PURO, text_color=self.OSCURO_TECH)
        self.pass_entry.pack(pady=10)

        ctk.CTkButton(self.reg_win, text="ENTRAR AL SISTEMA", fg_color=self.AZUL_FUERTE, hover_color=self.AZUL_CLARO, font=("Segoe UI", 15, "bold"), height=55, width=320, corner_radius=15, command=self.validar_acceso).pack(pady=40)

    def validar_acceso(self):
        u = self.user_entry.get()
        p = self.pass_entry.get()
        
        if not u or not p:
            messagebox.showwarning("Aviso", "Ingrese sus datos.")
            return

        if self.usuario_actual is None:
            self.usuario_actual = u
            self.contra_actual = p
            self.reg_win.destroy()
            self.inicializar_interfaz_principal()
            self.root.deiconify()
        else:
            if u == self.usuario_actual and p == self.contra_actual:
                self.intentos_login = 0
                self.reg_win.destroy()
                self.root.deiconify()
            else:
                self.intentos_login += 1
                restantes = 3 - self.intentos_login
                if restantes > 0:
                    messagebox.showerror("Error", f"Contraseña incorrecta. Quedan {restantes} intentos.")
                else:
                    messagebox.showerror("Bloqueo", "Límite de intentos alcanzado.")
                    self.root.destroy()

    def inicializar_interfaz_principal(self):
        for widget in self.root.winfo_children(): widget.destroy()

        self.header = ctk.CTkFrame(self.root, fg_color=self.AZUL_FUERTE, corner_radius=0, height=150)
        self.header.pack(fill="x")
        ctk.CTkLabel(self.header, text="CONTROL PRO", font=("Impact", 45), text_color=self.BLANCO_PURO).pack(pady=(30, 0))
        ctk.CTkLabel(self.header, text=f"OPERADOR: {self.usuario_actual.upper()}", font=("Segoe UI", 11, "bold"), text_color=self.AZUL_GELIDO).pack()

        self.main_body = ctk.CTkFrame(self.root, fg_color=self.AZUL_GELIDO, corner_radius=0)
        self.main_body.pack(fill="both", expand=True)

        self.card_acciones = ctk.CTkFrame(self.main_body, fg_color=self.BLANCO_PURO, corner_radius=30, border_width=2, border_color=self.AZUL_CLARO)
        self.card_acciones.pack(fill="x", padx=30, pady=20)

        ctk.CTkButton(self.card_acciones, text="REGISTRAR INGRESO", fg_color=self.OSCURO_TECH, hover_color=self.AZUL_FUERTE, font=("Segoe UI", 15, "bold"), height=60, corner_radius=15, command=self.ventana_ingreso).pack(fill="x", padx=40, pady=(20, 10))
        ctk.CTkButton(self.card_acciones, text="REGISTRAR EGRESO", fg_color=self.AZUL_CLARO, text_color=self.OSCURO_TECH, hover_color=self.AZUL_FUERTE, font=("Segoe UI", 15, "bold"), height=60, corner_radius=15, command=self.ventana_egreso).pack(fill="x", padx=40, pady=(0, 20))

        ctk.CTkButton(self.main_body, text="📊 ANÁLISIS PROPORCIONAL", fg_color=self.AZUL_FUERTE, font=("Segoe UI", 14, "bold"), height=55, corner_radius=20, command=self.ver_resumen).pack(fill="x", padx=60, pady=5)
        
        ctk.CTkButton(self.main_body, text="CERRAR SESIÓN", fg_color=self.ROJO_ALERTA, font=("Segoe UI", 12, "bold"), height=40, corner_radius=15, command=self.cerrar_sesion).pack(fill="x", padx=100, pady=5)

        self.card_hist = ctk.CTkFrame(self.main_body, fg_color=self.BLANCO_PURO, corner_radius=30, border_width=1, border_color=self.AZUL_CLARO)
        self.card_hist.pack(fill="both", expand=True, padx=30, pady=15)

        self.historial = tk.Listbox(self.card_hist, font=("Consolas", 12), bd=0, bg=self.BLANCO_PURO, highlightthickness=0, selectbackground=self.AZUL_GELIDO, fg=self.OSCURO_TECH)
        self.historial.pack(fill="both", expand=True, padx=25, pady=15)
        ctk.CTkButton(self.card_hist, text="MODIFICAR VALOR SELECCIONADO", fg_color="transparent", text_color=self.AZUL_FUERTE, font=("Segoe UI", 11, "bold"), command=self.modificar_registro).pack(pady=(0, 15))

    def ver_resumen(self):
        totingresos, totegresos = sum(self.ingresos), sum(self.egresos)
        balance = totingresos - totegresos
        res_win = ctk.CTkToplevel(self.root)
        res_win.title("Balance Mensual")
        res_win.geometry("520x920")
        res_win.configure(fg_color=self.AZUL_GELIDO)
        res_win.attributes("-topmost", True)

        header = ctk.CTkFrame(res_win, fg_color=self.OSCURO_TECH, height=80, corner_radius=0)
        header.pack(fill="x")
        ctk.CTkLabel(header, text="ANÁLISIS PROPORCIONAL", font=("Impact", 25), text_color=self.BLANCO_PURO).place(relx=0.5, rely=0.5, anchor="center")

        body = ctk.CTkFrame(res_win, fg_color=self.BLANCO_PURO, corner_radius=40)
        body.pack(fill="both", expand=True, padx=20, pady=20)

        # LÓGICA DE GRÁFICA LIMITADA A 0-100%
        if totingresos > 0:
            porcentaje_calculado = (totegresos / totingresos) * 100
            # Sincronización estricta: Limitar visualmente al 100%
            porcentaje_visual = min(max(porcentaje_calculado, 0), 100)
            
            fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
            fig.patch.set_facecolor(self.BLANCO_PURO)
            
            labels = ['Disponible', 'Gastado']
            sizes = [100 - porcentaje_visual, porcentaje_visual]
            colors = [self.AZUL_FUERTE, self.AZUL_CLARO]
            
            ax.pie(sizes, labels=labels, startangle=140, colors=colors, 
                   wedgeprops={'width': 0.3, 'edgecolor': self.BLANCO_PURO},
                   textprops={'weight': 'bold'})
            
            ax.text(0, 0, f"{porcentaje_visual:.1f}%", ha='center', va='center', fontsize=22, fontweight='bold', color=self.OSCURO_TECH)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=body)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=15)

            if porcentaje_calculado < 50:
                analisis = "Excelente control"
            elif 50 <= porcentaje_calculado <= 80:
                analisis = "Buen control financiero"
            elif 80 < porcentaje_calculado <= 100:
                analisis = "Alerta: tus gastos son muy altos"
            else:
                analisis = "Peligro financiero: gastas más de lo que ganas"

            ctk.CTkLabel(body, text=f"Gasto: {porcentaje_visual:.2f}%", font=("Segoe UI", 18, "bold"), text_color=self.OSCURO_TECH).pack()
            ctk.CTkLabel(body, text=f"-> {analisis}", font=("Segoe UI", 15), text_color=self.AZUL_FUERTE).pack(pady=5)
            
        else:
            ctk.CTkLabel(body, text="No se puede realizar comparación\nproporcional sin ingresos", font=("Segoe UI", 16), text_color=self.ROJO_ALERTA).pack(pady=100)

        card_b = ctk.CTkFrame(body, fg_color=self.AZUL_GELIDO, corner_radius=20)
        card_b.pack(fill="x", padx=40, pady=20)
        ctk.CTkLabel(card_b, text=f"DISPONIBLE: $ {balance:,.2f}", font=("Consolas", 20, "bold"), text_color=self.AZUL_FUERTE).pack(pady=20)

        ctk.CTkButton(res_win, text="VOLVER AL MENÚ", fg_color=self.OSCURO_TECH, height=50, corner_radius=15, command=res_win.destroy).pack(pady=20, padx=60, fill="x")

    def _crear_modal(self, t, c, cb):
        modal = ctk.CTkToplevel(self.root); modal.geometry("400x320"); modal.configure(fg_color=self.BLANCO_PURO); modal.attributes("-topmost", True)
        ctk.CTkLabel(modal, text=t, font=("Segoe UI", 22, "bold"), text_color=self.OSCURO_TECH).pack(pady=30)
        entry = ctk.CTkEntry(modal, width=250, height=50, corner_radius=12, border_color=c); entry.pack(); entry.focus()
        ctk.CTkButton(modal, text="CONFIRMAR", fg_color=c, height=45, corner_radius=12, command=lambda: cb(entry.get(), modal)).pack(pady=30)

    def ventana_ingreso(self): self._crear_modal("Nuevo Ingreso", self.AZUL_FUERTE, self.guardar_ingreso)
    def ventana_egreso(self): self._crear_modal("Nuevo Egreso", self.AZUL_CLARO, self.guardar_egreso)

    def guardar_ingreso(self, v, w):
        try:
            m = float(v)
            self.ingresos.append(m)
            self.historial.insert(0, f"  Ingreso: ${m:,.2f}")
            self.historial.itemconfig(0, fg=self.AZUL_FUERTE)
            w.destroy()
        except: pass

    def guardar_egreso(self, v, w):
        try:
            m = float(v)
            self.egresos.append(m)
            self.historial.insert(0, f"  Egreso:  ${m:,.2f}")
            self.historial.itemconfig(0, fg=self.ROJO_ALERTA)
            w.destroy()
        except: pass

    def modificar_registro(self):
        try:
            sel = self.historial.curselection()
            if not sel: return
            idx = sel[0]; txt = self.historial.get(idx)
            monto_v = float(txt.split("$")[-1].replace(",", ""))
            tipo = "Ingreso" if "Ingreso" in txt else "Egreso"
            
            modal = ctk.CTkToplevel(self.root); modal.geometry("350x250"); modal.attributes("-topmost", True)
            entry = ctk.CTkEntry(modal); entry.insert(0, str(monto_v)); entry.pack(pady=20)
            
            def aplicar():
                try:
                    m_n = float(entry.get())
                    if tipo == "Ingreso":
                        self.ingresos.remove(monto_v)
                        self.ingresos.append(m_n)
                        self.historial.delete(idx)
                        self.historial.insert(idx, f"  Ingreso: ${m_n:,.2f}")
                        self.historial.itemconfig(idx, fg=self.AZUL_FUERTE)
                    else:
                        self.egresos.remove(monto_v)
                        self.egresos.append(m_n)
                        self.historial.delete(idx)
                        self.historial.insert(idx, f"  Egreso:  ${m_n:,.2f}")
                        self.historial.itemconfig(idx, fg=self.ROJO_ALERTA)
                    modal.destroy()
                except: pass
                
            ctk.CTkButton(modal, text="ACEPTAR", command=aplicar).pack()
        except: pass

    def cerrar_sesion(self):
        if messagebox.askyesno("Salir", "¿Desea cerrar la sesión actual?"):
            self.root.withdraw()
            self.pantalla_registro()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ControlProApp(root)
    root.mainloop()