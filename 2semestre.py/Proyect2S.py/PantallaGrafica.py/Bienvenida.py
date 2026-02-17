import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from PIL import Image, ImageTk

# Configuración de apariencia
ctk.set_appearance_mode("light")
matplotlib.use("TkAgg")

class ControlProApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTROL PRO - Finanzas Elite")
        self.root.geometry("600x920")
        self.root.configure(fg_color="#F1F5F9") # Fondo gris azulado muy suave

        # --- Paleta de Colores Premium ---
        self.COL_PRIMARIO = "#0F172A"    # Azul Oxford (Header)
        self.COL_ACCENTO = "#0D9488"     # Turquesa oscuro
        self.COL_EXITO = "#10B981"       # Verde Esmeralda Vibrante
        self.COL_PELIGRO = "#EF4444"     # Rojo Intenso
        self.COL_TEXTO = "#1E293B"       # Gris Pizarra
        self.COL_CARD = "#FFFFFF"

        # Datos
        self.ingresos, self.egresos = [], []
        self.contra = "CONTROLPRO1313"

        self.setup_ui()

    def setup_ui(self):
        # --- Header con degradado visual (Simulado con Frame) ---
        self.header = ctk.CTkFrame(self.root, fg_color=self.COL_PRIMARIO, corner_radius=0, height=160)
        self.header.pack(fill="x")
        
        ctk.CTkLabel(self.header, text="CONTROL PRO", font=("Inter", 48, "bold"), 
                     text_color="#F8FAFC").pack(pady=(30, 2))
        
        self.status_bar = ctk.CTkFrame(self.header, fg_color=self.COL_ACCENTO, height=4, width=200)
        self.status_bar.pack()
        
        ctk.CTkLabel(self.header, text="GESTIÓN FINANCIERA DE ALTO NIVEL", 
                     font=("Inter", 12, "bold"), text_color="#94A3B8").pack(pady=(10, 20))

        # --- Contenedor Principal (Scrollable para evitar cortes en pantallas chicas) ---
        self.main_container = ctk.CTkScrollableFrame(self.root, fg_color="transparent", scrollbar_button_color="#CBD5E1")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Tarjeta de Operaciones ---
        self.card_ops = ctk.CTkFrame(self.main_container, fg_color=self.COL_CARD, corner_radius=25, 
                                     border_width=1, border_color="#E2E8F0")
        self.card_ops.pack(fill="x", pady=10)

        ctk.CTkLabel(self.card_ops, text="OPERACIONES RÁPIDAS", font=("Inter", 14, "bold"), 
                     text_color=self.COL_TEXTO).pack(pady=(20, 10))

        self.btn_ing = ctk.CTkButton(self.card_ops, text="✚  REGISTRAR INGRESO", 
                                     fg_color=self.COL_EXITO, hover_color="#059669",
                                     font=("Inter", 15, "bold"), height=55, corner_radius=15,
                                     command=self.ventana_ingreso)
        self.btn_ing.pack(fill="x", padx=40, pady=10)

        self.btn_egr = ctk.CTkButton(self.card_ops, text="▬  REGISTRAR EGRESO", 
                                     fg_color="#F43F5E", hover_color="#E11D48",
                                     font=("Inter", 15, "bold"), height=55, corner_radius=15,
                                     command=self.ventana_egreso)
        self.btn_egr.pack(fill="x", padx=40, pady=(10, 30))

        # --- Botón Resumen (Efecto Elevado) ---
        self.btn_res = ctk.CTkButton(self.main_container, text="📊 VER DASHBOARD ANALÍTICO", 
                                     fg_color=self.COL_PRIMARIO, text_color="white",
                                     hover_color=self.COL_ACCENTO, font=("Inter", 16, "bold"),
                                     height=65, corner_radius=18, command=self.ver_resumen)
        self.btn_res.pack(fill="x", pady=15)

        # --- Sección de Historial ---
        ctk.CTkLabel(self.main_container, text="ACTIVIDAD RECIENTE", font=("Inter", 13, "bold"), 
                     text_color="#64748B").pack(anchor="w", padx=10, pady=(10, 5))

        self.card_hist = ctk.CTkFrame(self.main_container, fg_color=self.COL_CARD, corner_radius=20, 
                                      border_width=1, border_color="#E2E8F0")
        self.card_hist.pack(fill="both", expand=True, pady=5)

        self.historial = tk.Listbox(self.card_hist, font=("Consolas", 12), bd=0, 
                                    bg=self.COL_CARD, highlightthickness=0, 
                                    selectbackground="#F1F5F9", fg=self.COL_TEXTO,
                                    relief="flat", height=10)
        self.historial.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Footer ---
        ctk.CTkButton(self.root, text="Cerrar Sesión de Forma Segura", fg_color="transparent", 
                      text_color="#64748B", font=("Inter", 12, "bold"),
                      hover_color="#E2E8F0", command=self.confirmar_salida).pack(pady=15)

    def _crear_modal(self, titulo, color_tema, callback):
        modal = ctk.CTkToplevel(self.root)
        modal.title(titulo)
        modal.geometry("420x350")
        modal.configure(fg_color="#F8FAFC")
        modal.attributes("-topmost", True)
        modal.grab_set() # Bloquea la ventana principal hasta cerrar el modal
        
        # Barra de acento superior
        ctk.CTkFrame(modal, fg_color=color_tema, height=8, corner_radius=0).pack(fill="x")
        
        ctk.CTkLabel(modal, text=titulo, font=("Inter", 24, "bold"), text_color=self.COL_TEXTO).pack(pady=(30, 10))
        
        entry = ctk.CTkEntry(modal, placeholder_text="0.00", width=280, height=55, 
                             corner_radius=12, font=("Inter", 20), border_color="#CBD5E1",
                             fg_color="white", justify="center")
        entry.pack(pady=20)
        entry.focus()
        
        ctk.CTkButton(modal, text="CONFIRMAR", fg_color=color_tema, corner_radius=12, 
                      height=50, width=280, font=("Inter", 14, "bold"), 
                      command=lambda: callback(entry.get(), modal)).pack(pady=20)

    def guardar_ingreso(self, val, win):
        try:
            m = float(val)
            self.ingresos.append(m)
            self.historial.insert(0, f" 🟢 INGRESO    +${m:,.2f}")
            self.historial.itemconfig(0, fg="#059669")
            win.destroy()
        except: messagebox.showerror("Error", "Por favor ingresa un monto numérico válido.")

    def guardar_egreso(self, val, win):
        try:
            m = float(val)
            self.egresos.append(m)
            self.historial.insert(0, f" 🔴 EGRESO     -${m:,.2f}")
            self.historial.itemconfig(0, fg="#DC2626")
            win.destroy()
        except: messagebox.showerror("Error", "Por favor ingresa un monto numérico válido.")

    def ventana_ingreso(self): self._crear_modal("Nuevo Ingreso", self.COL_EXITO, self.guardar_ingreso)
    def ventana_egreso(self): self._crear_modal("Nuevo Egreso", self.COL_PELIGRO, self.guardar_egreso)

    def ver_resumen(self):
        ti, te = sum(self.ingresos), sum(self.egresos)
        balance = ti - te
        raw_porc = (te / ti * 100) if ti > 0 else (100 if te > 0 else 0)
        porc_str = f"{min(raw_porc, 100):.2f}"
        
        res_win = ctk.CTkToplevel(self.root)
        res_win.title("Dashboard")
        res_win.geometry("550x850")
        res_win.configure(fg_color="white")
        res_win.attributes("-topmost", True)

        ctk.CTkLabel(res_win, text="RESUMEN FINANCIERO", font=("Inter", 22, "bold"), 
                     text_color=self.COL_PRIMARIO).pack(pady=(30, 5))

        # --- Gráfico Ultra-Limpio ---
        if ti > 0 or te > 0:
            fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
            fig.patch.set_facecolor('none') # Transparencia de fondo
            
            colores = [self.COL_EXITO, "#F1F5F9"] # Verde y un gris neutro para el fondo
            if te > ti: colores = ["#E2E8F0", self.COL_PELIGRO]
            
            # Gráfico de progreso circular
            ax.pie([max(0, ti-te), te], startangle=90, colors=colores,
                   wedgeprops={'width': 0.2, 'edgecolor': 'white', 'linewidth': 4},
                   counterclock=False)

            ax.text(0, 0, f"{porc_str}%\nGASTADO", ha='center', va='center', 
                    fontdict={'fontsize': 22, 'fontweight': 'bold', 'color': self.COL_PRIMARIO})
            
            ax.axis('equal') 
            canvas = FigureCanvasTkAgg(fig, master=res_win)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=10)

        # --- Tarjetas de Datos Estilo iOS ---
        info_frame = ctk.CTkFrame(res_win, fg_color="#F8FAFC", corner_radius=20, border_width=1, border_color="#E2E8F0")
        info_frame.pack(fill="both", expand=True, padx=40, pady=20)

        def crear_linea(label, valor, color):
            f = ctk.CTkFrame(info_frame, fg_color="transparent")
            f.pack(fill="x", padx=25, pady=10)
            ctk.CTkLabel(f, text=label, font=("Inter", 13), text_color="#64748B").pack(side="left")
            ctk.CTkLabel(f, text=valor, font=("Inter", 15, "bold"), text_color=color).pack(side="right")

        crear_linea("Total Ingresos", f"$ {ti:,.2f}", self.COL_EXITO)
        crear_linea("Total Egresos", f"$ {te:,.2f}", self.COL_PELIGRO)
        ctk.CTkFrame(info_frame, fg_color="#E2E8F0", height=2).pack(fill="x", padx=20, pady=5)
        crear_linea("Balance Neto", f"$ {balance:,.2f}", self.COL_PRIMARIO if balance >= 0 else self.COL_PELIGRO)

        # Botón de cierre
        ctk.CTkButton(res_win, text="ENTENDIDO", fg_color=self.COL_PRIMARIO, 
                      hover_color=self.COL_ACCENTO, corner_radius=15, 
                      height=50, width=200, font=("Inter", 14, "bold"), 
                      command=res_win.destroy).pack(pady=30)

    def confirmar_salida(self):
        pass_win = ctk.CTkToplevel(self.root)
        pass_win.title("Seguridad")
        pass_win.geometry("400x350")
        pass_win.configure(fg_color=self.COL_PRIMARIO)
        pass_win.attributes("-topmost", True)
        
        ctk.CTkLabel(pass_win, text="SISTEMA BLOQUEADO", font=("Inter", 20, "bold"), 
                     text_color="white").pack(pady=(40, 10))
        
        entry = ctk.CTkEntry(pass_win, placeholder_text="PIN de seguridad", show="*", 
                             width=250, height=45, corner_radius=10, border_color=self.COL_ACCENTO)
        entry.pack(pady=20)
        entry.focus()
        
        def validar():
            if entry.get() == self.contra: self.root.destroy()
            else: messagebox.showerror("Denegado", "Contraseña incorrecta", parent=pass_win)
            
        ctk.CTkButton(pass_win, text="DESBLOQUEAR Y SALIR", fg_color=self.COL_PELIGRO, 
                      corner_radius=10, font=("Inter", 13, "bold"), 
                      height=45, command=validar).pack(pady=20)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ControlProApp(root)
    root.mainloop()