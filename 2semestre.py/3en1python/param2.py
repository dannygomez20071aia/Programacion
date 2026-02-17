#suma de muchos numeros 
#arg se usa con :*
#kwargs se usa con : **

# USO DE *
def suma (*numeros):
    total = sum(numeros)
    print(f"La suma es: {total}")

suma(1,2,3,4,5,6,7)


# USO DE **
def info_personal (**datos):
    for nombre,dato in datos.items():
        print(f"{nombre}:{dato}")

info_personal(nombre="Julio", edad=20, ciudad="Quito", ocupacion = "Abogado")


