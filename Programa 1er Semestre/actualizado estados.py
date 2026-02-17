print("===================")
print("===== ESTADOS =====")
print("===================")

print("----------------------------------")
print("-Se presneta la lista de estados -")
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
estado = input("Elige el item ")

if not estado.isdigit():
    error = (" Error: solo se permiten números del 1 al 3")

estado = int(estado)

if estado < 1 or estado > 3:
        print("********************************")
        print(" Revisa y vuelve a elgir el item")
        print("********************************")
        

if estado == 1:
        print("==============================")
        print("Estado seleccionado: PENDIENTE")
        print("==============================")
    

elif estado == 2:
        print("===============================")
        print("Estado seleccionado: EN PROCESO")
        print("===============================")
elif estado == 3:
        print("==============================")
        print("Estado seleccionado: TERMINADO")
        print("==============================")