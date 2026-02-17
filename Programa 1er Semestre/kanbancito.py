import os
import time
from datetime import datetime

# ==============================================================================
#   KANBAN INTEGRADO: SANTIAGO (CORE) + DONNY (METRICAS) + DANNY (MENUS) + JANDRY (FECHAS)
# ==============================================================================

tasks = [] 
ultimo_id = 0 
mensaje_sistema = "Bienvenido a KANBANCITO"
ancho = 80 
filtro_actual = None 

# Referencias
ref_estados = {1: "PENDIENTE", 2: "EN PROCESO", 3: "TERMINADO"}
ref_prioridades = {1: "BAJA", 2: "MEDIA", 3: "ALTA"}

# Colores
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# ==============================================================================
#   BUCLE PRINCIPAL
# ==============================================================================
while True:
    os.system("cls" if os.name == "nt" else "clear")

    try:
        ancho = os.get_terminal_size().columns
    except:
        ancho = 80

    # --------------------------------------------------------------------------
    #   LOGICA DONNY: MÉTRICAS
    # --------------------------------------------------------------------------
    total_tareas = len(tasks)
    total_done = 0
    tiempo_total = 0

    for _t in tasks:
        if _t[2] == 3: # Estado 3 = TERMINADO
            total_done += 1
        tiempo_total += _t[5]

    porcentaje = 0.0
    if total_tareas > 0:
        porcentaje = (total_done / total_tareas) * 100

    # --------------------------------------------------------------------------
    #   HEADER
    # --------------------------------------------------------------------------
    print("=" * ancho)
    ahora = datetime.now()
    fecha_hoy_str = ahora.strftime("%Y-%m-%d")
    
    stats_str = f"Tareas: {total_tareas} | Done: {total_done} ({porcentaje:.1f}%) | T.Inv: {tiempo_total}m"
    padding = (ancho - len(stats_str)) // 2
    print(" " * padding + stats_str)
    print("=" * ancho)

    # --------------------------------------------------------------------------
    #   TABLA
    # --------------------------------------------------------------------------
    print(f"{'ID':<4} | {'ESTADO':<11} | {'PRIO':<8} | {'FECHA LIMITE':<12} | {'AVISO / TAREA'}")
    print("=" * ancho)

    # ORDENAMIENTO (Santiago)
    lista_ordenada = tasks[:]
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(n - i - 1):
            a = lista_ordenada[j]
            b = lista_ordenada[j + 1]
            if a[3] < b[3] or (a[3] == b[3] and a[0] > b[0]): 
                lista_ordenada[j], lista_ordenada[j + 1] = b, a

    # FILTRO
    if filtro_actual is not None:
        lista_a_mostrar = [t for t in lista_ordenada if t[3] == filtro_actual]
        aviso_filtro = f"[FILTRO ACTIVO: {ref_prioridades.get(filtro_actual)}]"
    else:
        lista_a_mostrar = lista_ordenada
        aviso_filtro = ""

    # RENDERIZADO (Lógica visual Jandry + Datos Danny)
    for _t in lista_a_mostrar:
        t_id, t_nombre, t_est, t_prio, t_fecha_str, t_tiempo = _t
        
        nombre_est = ref_estados.get(t_est, "???")
        nombre_prio = ref_prioridades.get(t_prio, "???")
        
        # Semáforo de fechas (Jandry)
        color_fila = RESET
        aviso_jandry = ""
        
        try:
            fecha_tarea = datetime.strptime(t_fecha_str, "%Y-%m-%d")
            if t_est != 3:
                if fecha_tarea.date() < ahora.date():
                    color_fila = RED
                    aviso_jandry = f"{RED}[YA VENCIÓ X]{RESET} "
                elif fecha_tarea.date() == ahora.date():
                    color_fila = YELLOW
                    aviso_jandry = f"{YELLOW}[VENCE HOY !]{RESET} "
                else:
                    color_fila = GREEN
            else:
                color_fila = CYAN 
        except ValueError:
            aviso_jandry = "[Error Fecha] "

        # Impresión
        fmt_id = f"{t_id:<4}"
        fmt_est = f"{color_fila}{nombre_est:<11}{RESET}"
        fmt_prio = f"{nombre_prio:<8}"
        fmt_fecha = f"{t_fecha_str:<12}"
        
        print(f"{fmt_id} | {fmt_est} | {fmt_prio} | {fmt_fecha} | {aviso_jandry}{t_nombre}")

    if len(tasks) == 0:
        print(f"\n{'[ La lista está vacía ]':^{ancho}}\n")
        
    #   MENÚ
    print("-" * ancho)
    if aviso_filtro: print(aviso_filtro)
    print(" [1] Nueva Tarea   [2] Modificar   [3] Borrar   [4] Filtrar   [5] Salir")
    print("-" * ancho)

    if mensaje_sistema:
        print(f" >> SISTEMA: {mensaje_sistema}")
        mensaje_sistema = ""
        print("-" * ancho)

    opcion = input(" Acción > ")
    
    #   OPCIÓN 1: NUEVA TAREA
    if opcion == "1":
        print("\n [NUEVA TAREA]")
        in_nombre = input(" Nombre: ")

        if in_nombre:
            # --- MENU PRIORIDAD (DANNY) ---
            print("==================")
            print("====PRIORIDADES===")
            print("==================")
            print("== 1. BAJA ==")
            print("== 2. MEDIA ==")
            print("== 3. ALTA ==")
            print("-------------------------------------------")
            
            prio_input = input("Elige el item > ")
            
            prio_final = 1
            if prio_input in ["1", "2", "3"]:
                prio_final = int(prio_input)
            else:
                print(" Entrada inválida. Se asigna BAJA.")

            # --- VALIDACIÓN FECHA (JANDRY) ---
            fecha_final = ""
            print(f" Fecha Límite (Ej: {fecha_hoy_str})")
            while True:
                entrada_f = input(" > ").strip()
                if entrada_f == "":
                    fecha_final = fecha_hoy_str
                    break
                try:
                    datetime.strptime(entrada_f, "%Y-%m-%d")
                    fecha_final = entrada_f
                    break 
                except ValueError:
                    print(f"{RED} Error: Formato incorrecto.{RESET}")

            ultimo_id += 1
            tasks.append([ultimo_id, in_nombre, 1, prio_final, fecha_final, 0])
            mensaje_sistema = f"Tarea ID {ultimo_id} agregada."
        else:
            mensaje_sistema = "Error: Nombre vacío."

    #   OPCIÓN 2: MODIFICAR (AQUÍ ESTÁ LA INTEGRACIÓN EXACTA)
    elif opcion == "2":
        in_id = input(" ID a modificar: ")
        
        tarea = None
        for _t in tasks:
            if str(_t[0]) == in_id:
                tarea = _t
                break

        if not tarea:
            mensaje_sistema = "Error: ID no existe."
        else:
            print(f" Editando: {tarea[1]}")
            
            # --- 1. MENÚ VISUAL DE DANNY (COPIADO DE SU ARCHIVO) ---
            print("===================")
            print("===== ESTADOS =====")
            print("===================")
            print("----------------------------------")
            print("-Se presenta la lista de estados -")
            print("----------------------------------")
            print("==================")
            print("== 1. PENDIENTE ==")
            print("==================")
            print("===================")
            print("== 2. EN PROCESO ==")
            print("===================")
            print("==================")
            print("== 3. TERMINADO ==")
            print("==================")
            print("-------------------------------------------")
            print("--Lee y elige el item que deseas realizar:-")
            print("-------------------------------------------")
            
            estado_input = input("Elige el item > ")
            
            # --- 2. VALIDACIÓN DE DANNY ---
            es_valido = False
            if not estado_input.isdigit():
                 mensaje_sistema = " Error: solo se permiten números del 1 al 3"
            else:
                nuevo_estado = int(estado_input)
                if nuevo_estado < 1 or nuevo_estado > 3:
                     mensaje_sistema = " Revisa y vuelve a elegir el item"
                else:
                    es_valido = True

            # --- 3. LÓGICA DE TIEMPO DE DONNY ---
            # Si Danny valida el número, pasamos a Donny
            if es_valido:
                tiempo_a_sumar = 0
                error_donny = False
                
                # Si el estado elegido es 3 (TERMINADO)
                if nuevo_estado == 3:
                    tiempo_str = input(" Minutos invertidos: ")
                    
                    # Validación estricta de Donny
                    if not tiempo_str.isdigit():
                        mensaje_sistema = "Error: Solo números enteros."
                        error_donny = True # Marcamos error para no guardar
                    else:
                        tiempo_a_sumar = int(tiempo_str)
                
                # Si NO hubo error en la parte de Donny, guardamos todo
                if not error_donny:
                    tarea[2] = nuevo_estado      # Guardar Estado (Danny)
                    if tiempo_a_sumar > 0:
                        tarea[5] += tiempo_a_sumar   # Guardar Tiempo (Donny)
                    
                    # Mensaje de éxito de Danny
                    if nuevo_estado == 1:
                         mensaje_sistema = "Estado seleccionado: PENDIENTE"
                    elif nuevo_estado == 2:
                         mensaje_sistema = "Estado seleccionado: EN PROCESO"
                    elif nuevo_estado == 3:
                         mensaje_sistema = "Estado seleccionado: TERMINADO"

   #   OTRAS OPCIONES

    elif opcion == "3":
        in_id = input("ID a borrar: ")
        idx = -1
        for i, _t in enumerate(tasks):
            if str(_t[0]) == in_id:
                idx = i
                break
        if idx != -1:
            borrada = tasks.pop(idx)
            mensaje_sistema = f"Tarea '{borrada[1]}' eliminada."
        else:
            mensaje_sistema = "ID no encontrado."

    elif opcion == "4":
        print("\n [FILTROS]")
        print(" 1. Ver Todas | 2. Alta | 3. Media | 4. Baja")
        sub = input(" > ")
        if sub == "1": filtro_actual = None
        elif sub == "2": filtro_actual = 3
        elif sub == "3": filtro_actual = 2
        elif sub == "4": filtro_actual = 1

    elif opcion == "5":
        print("-------------------------")
        print("-- PROGRAMA FINALIZADO --")
        print("-------------------------")
        break
    else:
        mensaje_sistema = "Opción inválida."