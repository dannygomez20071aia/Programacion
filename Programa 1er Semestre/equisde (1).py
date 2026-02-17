import os
import time

# ==============================================================================
#  MÓDULO: RESPONSABLE 1: SANTIAGO (GESTIÓN DE TAREAS - CORE) -> ¡COMPLETO!
# ==============================================================================
# ESQUEMA DE DATOS (LISTA DE LISTAS):
# [ID, NOMBRE, ESTADO, PRIORIDAD, FECHA, TIEMPO]
#  0     1        2        3        4       5

tasks = []  # Matriz principal de datos
ultimo_id = 0  # Generador de IDs
mensaje_sistema = "Sistema listo. Esperando código de Danny, Jandry y Donny..."
ancho = 80  # Ancho de pantalla

# ==============================================================================
#  MÓDULO: RESPONSABLE 2: DANNY (FLUJO Y PRIORIDADES) -> ¡PENDIENTE!
# ==============================================================================
# Definición de listas de referencia
# ESTADOS: 1=Pendiente, 2=En Proceso, 3=Terminada
ref_estados = {
    1: "PENDIENTE", 
    2: "EN PROCESO", 
    3: "TERMINADA"
}
# PRIORIDADES: 1=Baja, 2=Media, 3=Alta
ref_prioridades = {
    1: "BAJA", 
    2: "MEDIA", 
    3: "ALTA"
}

# Estilos visuales (ANSI)
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# Variable de control para filtros (Opción 4)
filtro_actual = None 

# ==============================================================================
#  BUCLE PRINCIPAL (INTERFAZ GRÁFICA)
# ==============================================================================
while True:
    # 1. LIMPIEZA DE PANTALLA
    os.system("cls" if os.name == "nt" else "clear")

    # Ajuste de ancho de consola
    if hasattr(os, "get_terminal_size"):
        try:
            ancho = os.get_terminal_size().columns
        except:
            ancho = 80

    # --------------------------------------------------------------------------
    #  LOGICA: RESPONSABLE 4: DONNY (MÉTRICAS) -> ¡PENDIENTE!
    # --------------------------------------------------------------------------
    # TODO DONNY: Recorrer 'tasks' para calcular estos valores reales.
    total_tareas = 0 # Reemplazar con len(tasks)
    total_done = 0   # Reemplazar con conteo real de estado 3
    tiempo_total = 0 # Reemplazar con suma de indice 5
    porcentaje = 0.0 # Calcular porcentaje (cuidar división por cero)

    # --------------------------------------------------------------------------
    #  INTERFAZ: HEADER (Encabezado)
    # --------------------------------------------------------------------------
    print(f"{GREEN}" + "=" * ancho + f"{RESET}")
    fecha_hoy = time.strftime("%Y-%m-%d")
    
    # Visualización de métricas
    color_perc = RESET # Donny puede cambiar esto luego
    stats_str = f"Tareas: {total_tareas} | Done: {total_done} ({color_perc}{porcentaje:.1f}%{RESET}) | T.Inv: {tiempo_total}m"
    
    long_visible = len(f"Tareas: {total_tareas} | Done: {total_done} ({porcentaje:.1f}%) | T.Inv: {tiempo_total}m")
    padding = (ancho - long_visible) // 2
    print(" " * padding + stats_str)
    
    print(f"=" * ancho)

    # --------------------------------------------------------------------------
    #  INTERFAZ: TABLERO (Tabla Principal)
    # --------------------------------------------------------------------------
    separador_cols = "|"
    print(f"{'ID':<4}", separador_cols, f"{'ESTADO':<11}", separador_cols, f" {'PRIO':<8}", separador_cols, f"{'FECHA':<12}", separador_cols, f"{'TAREA'}")
    print("=" * ancho)

    # --------------------------------------------------------------------------
    #  LOGICA: RESPONSABLE 1: SANTIAGO (ORDENAMIENTO) -> ¡COMPLETO!
    # --------------------------------------------------------------------------
    # BUBBLE SORT MANUAL: Prioridad Descendente (3,2,1) y luego ID Ascendente
    lista_ordenada = tasks[:] 
    n_items = len(lista_ordenada)
    
    for i in range(n_items):
        for j in range(0, n_items - i - 1):
            # [3] es Prioridad, [0] es ID
            t_act = lista_ordenada[j]
            t_sig = lista_ordenada[j+1]
            
            prio_act, prio_sig = t_act[3], t_sig[3]
            id_act, id_sig = t_act[0], t_sig[0]
            
            intercambiar = False
            # 1. Mayor prioridad primero
            if prio_act < prio_sig:
                intercambiar = True
            # 2. Desempate por ID (Menor ID primero)
            elif prio_act == prio_sig:
                if id_act > id_sig:
                    intercambiar = True
            
            if intercambiar:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    # Aplicar filtro (Parte de Danny/Santiago)
    if filtro_actual is not None:
        lista_a_mostrar = [t for t in lista_ordenada if t[3] == filtro_actual]
        aviso_filtro = f" [FILTRO ACTIVO: {filtro_actual}] "
    else:
        lista_a_mostrar = lista_ordenada
        aviso_filtro = ""

    # BUCLE DE RENDERIZADO (IMPRESIÓN FILA POR FILA)
    for _t in lista_a_mostrar:
        t_id = _t[0]
        t_nombre = _t[1]
        t_estado_num = _t[2]
        t_prio_num = _t[3]
        t_fecha = _t[4]

        # ----------------------------------------------------------------------
        #  LOGICA: RESPONSABLE 2: DANNY (VISUALIZACIÓN) -> ¡PENDIENTE!
        # ----------------------------------------------------------------------
        # TODO DANNY: Usar t_estado_num y t_prio_num para buscar texto y asignar color
        nombre_est = "???"
        color_est = RESET

        nombre_prio = "???"
        color_prio = RESET

        # ----------------------------------------------------------------------
        #  LOGICA: RESPONSABLE 3: JANDRY (TIEMPOS) -> ¡PENDIENTE!
        # ----------------------------------------------------------------------
        # TODO JANDRY: Comparar t_fecha con fecha_hoy.
        # Si t_fecha < fecha_hoy y no está terminada -> !VENCIDA! (Rojo)
        aviso_vencimiento = ""

        # IMPRESIÓN FINAL DE LA FILA
        est_fmt = f"{color_est}{str(nombre_est)[:11]:<11}{RESET}"
        prio_fmt = f"{color_prio}{str(nombre_prio):<8}{RESET}"
        
        print(
            f"{t_id:<4} | {est_fmt} | {prio_fmt} | {t_fecha:<12} | {t_nombre}{aviso_vencimiento}"
        )

    if len(tasks) == 0:
        print(f"\n{'[ La lista está vacía ]':^{ancho}}\n")
    elif len(lista_a_mostrar) == 0 and filtro_actual is not None:
         print(f"\n{'[ No hay tareas con este filtro ]':^{ancho}}\n")

    # --------------------------------------------------------------------------
    #  INTERFAZ: MENÚ
    # --------------------------------------------------------------------------
    print("-" * ancho)
    if aviso_filtro: print(f"{CYAN}{aviso_filtro}{RESET}")
        
    print(f"{YELLOW} [1] Nueva Tarea   [2] Modificar   [3] Borrar   [4] Filtrar   [5] Salir{RESET}")
    print(f"{CYAN}" + "-" * ancho + f"{RESET}")

    if mensaje_sistema:
        print(f" >> SISTEMA: {mensaje_sistema}")
        mensaje_sistema = ""
        print(f"{GREEN}" + "-" * ancho + f"{RESET}")

    opcion = input(" Acción > ")

    # ==========================================================================
    #  LÓGICA DE CONTROL
    # ==========================================================================

    # --- [OPCIÓN 1] NUEVA TAREA (SANTIAGO) -> HECHO ---
    if opcion == "1":
        print("\n [NUEVA TAREA]")
        in_nombre = input(" Nombre: ")

        if len(in_nombre) > 0:
            print(" Prioridad: 1=Baja, 2=Media, 3=Alta")
            in_prio = input(" Selección (Default 1): ")
            in_fecha = input(f" Fecha Límite (YYYY-MM-DD) [Hoy: {fecha_hoy}]: ")
            if not in_fecha: in_fecha = fecha_hoy 

            ultimo_id += 1
            prio_final = int(in_prio) if in_prio in ["1", "2", "3"] else 1
            
            # Estructura: [ID, Nombre, Estado(1), Prio, Fecha, Tiempo(0)]
            nueva_tarea = [ultimo_id, in_nombre, 1, prio_final, in_fecha, 0]
            tasks.append(nueva_tarea)
            mensaje_sistema = f"Tarea ID {ultimo_id} agregada."
        else:
            mensaje_sistema = "Error: Nombre vacío."

    # --- [OPCIÓN 2] MODIFICAR (DANNY) -> ¡PENDIENTE! ---
    elif opcion == "2":
        in_id = input(" ID a modificar: ")
        
        # TODO DANNY: Buscar la tarea por ID.
        # TODO DANNY: Pedir nuevo estado (1, 2, 3).
        # TODO DONNY: Si el nuevo estado es 3, pedir tiempo invertido y sumar.
        
        mensaje_sistema = "FUNCIONALIDAD NO IMPLEMENTADA (Tarea de Danny y Donny)"
        
        # --- CÓDIGO DE AYUDA (DESCOMENTAR Y COMPLETAR) ---
        # tarea_encontrada = None
        # for _t in tasks:
        #    if str(_t[0]) == in_id:
        #        tarea_encontrada = _t
        #        break
        #
        # if tarea_encontrada:
        #    print(f" Editando: {tarea_encontrada[1]}")
        #    nuevo_est = input(" Nuevo Estado (1-3): ")
        #    ... (Implementar lógica aquí) ...

    # --- [OPCIÓN 3] BORRAR TAREA (SANTIAGO) -> HECHO ---
    elif opcion == "3":
        in_id = input(" ID a borrar: ")
        idx_borrar = -1
        for i, _t in enumerate(tasks):
            if str(_t[0]) == in_id:
                idx_borrar = i
                break

        if idx_borrar != -1:
            borrada = tasks.pop(idx_borrar)
            mensaje_sistema = f"Tarea '{borrada[1]}' eliminada."
        else:
            mensaje_sistema = "Error: ID no existe."
    
    # --- [OPCIÓN 4] FILTRAR (DANNY/SANTIAGO) ---
    elif opcion == "4":
        # TODO DANNY: Puedes mejorar esto si quieres filtros combinados
        print("\n [FILTROS]")
        print(" 1. Ver Todas")
        print(" 2. Solo Alta Prioridad")
        print(" 3. Solo Media Prioridad")
        sub_op = input(" Selecciona: ")
        
        if sub_op == "1": filtro_actual = None
        elif sub_op == "2": filtro_actual = 3
        elif sub_op == "3": filtro_actual = 2
        else: mensaje_sistema = "Filtro inválido."
    
    # --- [OPCIÓN 5] SALIR ---
    elif opcion == "5":
        print("Cerrando Kanbancito...")
        # TODO DONNY: Imprimir reporte de estado final de la lista de tareas (Resumen sesión).
        break
    
    else:
        mensaje_sistema = "Opción inválida."