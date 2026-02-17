print("==================")
print("====PRIORIDADES===")
print("==================")

print("-------------------------------------")
print("-Se presneta la lista de prioridades-")
print("-------------------------------------")

print("=============")
print("== 1. BAJA ==")
print("=============")

print("==============")
print("== 2. MEDIA ==")
print("==============")

print("=============")
print("== 3. ALTA ==")
print("=============")


print("-------------------------------------------")
print("--Lee y elige el item que deseas realizar:-")
print("-------------------------------------------")
prioridad = input("Elige el item ")

if not prioridad.isdigit():
        
        error = (" Error: solo se permiten números del 1 al 3")
        

prioridad = int(prioridad)

if prioridad < 1 or prioridad >3:
        print("********************************")
        print(" Revisa y vuelve a elgir el item")
        print("********************************")
      
if prioridad ==1:
        print("==============================")
        print(" Prioridad seleccionada : BAJA")
        print("==============================")

elif prioridad ==2:
    
        print("===============================")
        print("Prioridad seleccionada : MEDIA ")
        print("===============================")

elif prioridad ==3:
        print("==============================")
        print("Prioridad seleccionada : ALTA ")
        print("==============================")