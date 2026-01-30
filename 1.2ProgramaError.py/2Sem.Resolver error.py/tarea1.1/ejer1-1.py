import mod2 
palabra = input("---- Ingrese una palabra ----: ")

vocales = "AEIOUaeiouáéíóúü"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print("La palabra contiene", contador, "letras")
print(palabra.upper())
print(palabra.lower())