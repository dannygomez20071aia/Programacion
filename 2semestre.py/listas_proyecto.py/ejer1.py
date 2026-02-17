#crear n progra,a para una tienda 
#que genere una lista de compras
#solicite el ingreso de 3 productos en un listado 
#muestre la lista completa al usuario
#que elimine un elemento de la lista y muestre el resultado 

compras = []

print("==========================")
print("====== MARKET_DANNY ======")
print("==========================")

print("--------------")
print("= Bienvenido =")
print("--------------")

print("===================================")
print("== INGRESAR al menos 3 productos ==")
print("===================================")


for i in range(3):
    producto = (input(f"Ingrese el producto {i + 1}: "))
    compras.append(producto)
    
print("---------------------")
print("--Lista de compras:--")
print("---------------------")
print(compras)

elim = input("--Ingrese el producto que desea eliminar: --")

if elim in compras:
    compras.remove(elim)
    print("Producto eliminado correctamente")
else:
    print("=======================================")
    print("El producto no se encuentra en la lista")
    print("=======================================")

print("-----------------------------")
print("Lista de compras actualizada:")
print("-----------------------------")

print(compras)