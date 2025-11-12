print("-------------------------")
print("-- CARNICERIA DANNY --")
print("-------------------------")
#parametros a revisar
#temperatura 
#valor de sueldos ( diario, mensual, anual )
#calculo de areas y perimetro de 4 figuaras básicas
print("---------------------------------------------")
print(" Se realiza el control de temperatura para : ")
print(" CARNES Y EMBUTIDOS ")
print("---------------------------------------------")

#control de temperatura 
print("---------------------------------------------------")
temp1= float(input("Cual es la temperatura de las carnes?:"))

if temp1>79:
    print("---------------------------------------")
    print("El producto se encuentra en buen estado")
    print("---------------------------------------")

else:
    print("-------------------------------")
    print("El producto debe ser desecahdo ")
    print("-------------------------------")
    
print("------------------------------------------------------")
temp2= float(input("Cual es la temperatura de los embutidos?:"))

if temp2>50:
    print("-------------------------------")
    print("El producto aun se puede vender")
    print("-------------------------------")

else:
    print("-------------------------")
    print("El producto esta caducado")
    print("-------------------------")

print("---------------------------------------")
print("Se culminó la revisión de los productos")
print("---------------------------------------")

print("---------------------------------------")
print("Gracias por revisar nuestros embutidos ")
print("-----------------------------------------------")
print("Participa en un juego y llevate embutido gratis")
print("-----------------------------------------------")
print("-----------------------------------------")
print("-- Escribe una palabra para participar --")
print("-Si tu palabra contiene 8 vocales ganas -")
print("-----------------------------------------")

frase = input("Escribe tu frase aquì:")
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print("-- La cantidad de vocales que contiene tu palabra es:", contador)

if contador==8:
    print("--------------------------------------")
    print("FELICIDADES GANASTE UN EMBUTIDO GRATIS")
    print("--------------------------------------")
else:
    print("GAME OVER")
    
#valor de sueldos( diario, mensual, anual)
#sueldom= mensual
#sueldos= semanal
#sueldod= diario 
print("----------------------------------")
print("----- Revision de los sueldos ----")
print("----------------------------------")

valor1 = 400
valor2 = 16
valor3 = 500
valor4 = 550
valor5 = 24.583
valor6 = 620
valor7 = 700
valor8 = 1200

print("------------------------------------------------------------")


print("---------------------")
print("---- SUELDO JEFE ----")
print("---------------------")
print("El jefe tiene un sueldo anual de:", valor8)
print("------------------------------------------------------------")

print("----------------")
print(" SUELDO CAJERO/A")
print("----------------")

sueldom= "mensual"
sueldos= "semanal"
sueldod= "diario"

if sueldom:
    print("----------------")
    print("Si su sueldo es:", sueldom,"gana", valor7)
    print("----------------")

if sueldos:
    print("----------------")
    print("Si su sueldo es:", sueldos,"gana", valor6)
    print("----------------")

if sueldod:
    print("----------------")
    print("Si su sueldo es:", sueldod,"gana", valor5)
    print("----------------")

print("------------------------------------------------------------")


print("-----------------")
print("SUELDO EMPELADOS ")
print("-----------------")

pagom= "mensual"
pagos= "semanal"
pagod= "diario"

if pagom:
    print("----------------")
    print("Si su sueldo es:", pagom,"gana", valor4)
    print("----------------")

if pagos:
    print("----------------")
    print("Si su sueldo es:", pagos,"gana", valor3)
    print("----------------")

if pagod:
    print("----------------")
    print("Si su sueldo es:", pagod,"gana", valor2)
    print("----------------")


print("-----------------")
print(" SUELDO CONSERJE ")
print("-----------------")

print("Sueldo fijo, tiene un valor mensual de:",valor1)

#calculo de areas y perimetro de 4 figuaras básicas


print("-------------------------------------------------------")
print("         Tienes dudas con areas y perìmetros           ")
print("Àrea Perìmetro Figura de elctrodomèsticos de la empresa")
print("-------------------------------------------------------")

print("---------------------------------------")
print("-- Vamos a realizar àrea y perìmetro --")
print("---------------------------------------")
print( "--------- FIGURAS A REALIZAR ---------")
print("fig1 = CUADRADO")
print("fig2 = CIRCULO")
print("fig3 = RECTANGULO")
print("fig4 = TRIANGULO")
print("---------------------------------------")

fig1= "CUADRADO"
fig2= "CIRCULO"
fig3= "RECTAGULO "
fig4= "TRIANGULO"

print("-----------------------------------------------")
print("-----------------------------------------------")

if fig1:
    print("----------")
    print(" CUADRADO ")
    print("----------")
        
    print(" Ingresa el valor del objeto cuadrado ")
    lado = float(input("TAMAÑO DEL LADO:"))
    area1 = lado * lado
    print(" El àrea del:",fig1 ,"es:", area1)

print("-----------------------------------------------")
print("-----------------------------------------------")

if fig2:
    print("---------")
    print(" CIRCULO ")
    print("---------")
    
    import math

print(" Ingresa la medida del objeto circular ")
radio= float(input("radio:"))

if radio >0:
    area2 = math.pi * radio **2
    perimetro = 2 * math.pi *radio 
    print("El àrea del:",fig2 ,"es", area2)
    print("El perìmetro del:",fig2,"es", perimetro)
    
    
else:
    print("-------------------------------------------")
    print("Revisa tu valor el radio debe ser positivo ")
    print("-------------------------------------------")
    
print("-----------------------------------------------")
print("-----------------------------------------------")

if fig3:
    print("------------")
    print(" RECTANGULO ")
    print("------------")


print(" Ingresa la medida del objeto rectangular ")    
base3 = int(input("Ingresa el valor de la base:"))
altura3 = int(input("Ingresa la altura:"))

area3 = base3 * altura3
perimetro3 = 2 * (base3 + altura3)

print("------------------------------")
print("El àrea del:",fig3 ,"es", area3)
print("El perìmetro del:", fig3, "es", perimetro3 )
print("------------------------------")

print("-----------------------------------------------")
print("-----------------------------------------------")

if fig4:
    print("-----------")
    print(" TRIANGULO ")
    print("-----------")

print(" Ingresa la mediada del objeto triangular ")
base4 = float (input("Ingresa el valor de la base:"))
altura4 = float (input("Ingresa el valor de la altura:"))

area4 = base4 * altura4 / 2

print("------------------------------")
print("El àrea del:",fig4 ,"es", area4)
print("------------------------------")

print("---------------------------")
print("-- GRACIAS POR SU VISITA --")
print("---------------------------")