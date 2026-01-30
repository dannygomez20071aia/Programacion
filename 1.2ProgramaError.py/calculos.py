def determinarResultadosIMC(imc=float):
    if 0 <= imc < 16:
        return "Delgadez severa"
    elif 16 <= imc < 17:
        return "Delgadez moderada"
    elif 17 <= imc < 18.5:
        return "Delgadez leve"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado 1"
    elif 35 <= imc < 40:
        return "Obesidad Grado 2"
    elif imc >= 40:
        return "Obesidad Grado 3"
    else:
        return "IMC fuera de rango"
    
def encontrarMayor (val1=int,val2=int,val3=int):
    mayorActual = val1
    
    if val2 > mayorActual:
        mayorActual = val2

    if val3 > mayorActual:
        mayorActual = val3

    return mayorActual

def encontrarMenor(num1=int,num2=int,num3=int,num4=int):
    menorActual = num1
    
    if num2 < menorActual:
        menorActual = num2
    
    if num3 < menorActual:
        menorActual= num3
    
    if num4 < menorActual:
        menorActual = num4
    return menorActual