# contaqdor de letras 
#contador 
#desglose
#condicional
frase = input("Escribe tu frase aquì:")
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print("-- La cantidad e vocales que contiene tu palabra es:", contador)
