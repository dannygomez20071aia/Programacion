# Suma cualquie rtipo de objeto el uso de: len()

def prome (*suma):
    while True:
        entrada = input("Ingrese una nota o escriba 'ok' para terminar): ")

        if entrada.lower() == "ok":
            break
        
    resultado = sum(suma)
    promedio = resultado/len(suma)
    print(f"La suma de todas las notas es:",{resultado})
    print(f"El promedio de notas es:",{promedio})