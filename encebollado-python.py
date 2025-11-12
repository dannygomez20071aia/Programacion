print("-------------------------------------------")
print("-------------------------------------------")
print(" -----  BIENVENIDO CABEZA DE POLLO  ------ ")
print("-------------------------------------------")
print("-------------------------------------------")
print(" ---- Ayer te pasaste de copas? s / n ---- ")
s = input("Respuesta: ")

if s == "s":
    print("---------------------------------------")
    print(" -- Calma aquí curamos tu chuchaqui -- ")
    print("---------------------------------------")
    print("------------------------------")
    print("--- Ven y prueba tu suerte ---")
    print("------------------------------")
    print("------------------------------")
    print("Si escribes una palabra que contenga 8 vocales ganas un encebollado gratis")
    print("------------------------------")
    palabra = input("---- Ingrese una palabra ----: ")
    print("-----------------------------------------")

    vocales = "aeiouáéíóúü"
    contador = 0

    for letra in palabra:
        if letra in vocales:
            contador += 1

    print("La palabra contiene", contador, vocales)

    if contador == 8:
        print("-----------------------------------------------------")
        print("-- Felicidades te ganaste un encebollado gratis ---")
        print("-----------------------------------------------------")
    else:
        print("--------------------------------------------------------")
        print("--------- Lo lamentamos, sigue participando ------------")
        print("NO TE DESANIMES VEN Y SUBE TU ANIMO CON UN ENCEBOLLADO")
        print("--------------------------------------------------------")

    print("-------------------------------------------")
    print("-- Te presentamos el menú del día de hoy --")
    print("------- Deseas ver el menú ? s / n --------")
    print("-------------------------------------------")
    menu = input("Respuesta: ")

    final = 0
    detalle = ""

    if menu == "s":
        print("-----------------------------------------------------------")
        print("------------ Este es el menú del día de hoy ---------------")
        print("1. Encebollado mixto ............................... $9.50")
        print("2. Encebollado concha .............................. $8.00")
        print("3. Encebollado camarón ............................. $7.50")
        print("4. Encebollado corvina ............................. $5.50")
        print("5. Encebollado simple .............................. $2.50")
        print("6. Pescado Frito  .................................. $3.50")
        print("7. Pescado Ahumado  ................................ $2.50")
        print("8. Corviche   ...................................... $1.50")
        print("-----------------------------------------------------------")

        itm = int(input("Selecciona el item que deseas adquirir: "))

        precios = {
            1: ("Encebollado mixto ............................... $9.50", 9.50),
            2: ("Encebollado concha .............................. $8.00", 8.00),
            3: ("Encebollado camarón ............................. $7.50", 7.50),
            4: ("Encebollado corvina ............................. $5.50", 5.50),
            5: ("Encebollado simple .............................. $2.50", 2.50),
            6: ("Pescado Frito  .................................. $3.50", 3.50),
            7: ("Pescado Ahumado  ................................ $2.50", 2.50),
            8: ("Corviche   ...................................... $1.50", 1.50),
        }

        if itm in precios:
            detalle, final = precios[itm]
        else:
            print(" --- Revise nuevamente su orden ---")

    else:
        print("------------------------------------------------------------")
        print("-------------- También ofrecemos bebidas -------------------")
        print("------------ Por si aún no se le abre el apetito -----------")
        print("------------------------------------------------------------")
        print("--- El menú de bebidas es : ---")
        print("1. Jaba de cerveza ................................... $22.50")
        print("2. Cerveza Pilsener .................................. $2.50")
        print("3. Cerveza Club  ..................................... $3.50")
        print("4. Jarra de jugo ..................................... $12.50")
        print("5. Vaso de jugo  ..................................... $2.50")
        print("6. Soda Personal ..................................... $1.00")
        print("7. Soda de Litro ..................................... $2.00")
        print("8. Botella de Agua ................................... $0.75")
        print("------------------------------------------------------------")
        opn = int(input("Selecciona alguna opción: "))

        precios_bebidas = {
            1: 22.50, 2: 2.50, 3: 3.50, 4: 12.50,
            5: 2.50, 6: 1.00, 7: 2.00, 8: 0.75
        }

        if opn in precios_bebidas:
            final = precios_bebidas[opn]
        else:
            print(" --- Revise su pedido --- ")

    # FACTURA
    print("-----------------------------------")
    print("------- FACTURA ENCEBOLLADO -------")
    print("-----------------------------------")
    nombre = input("NOMBRE DEL CLIENTE: ")
    ci = input("CÉDULA DE IDENTIDAD: ")
    nomofirma = input("FIRMA O NOMBRE DEL CLIENTE (confirmación): ")

    print("Valor a pagar:", final)
    print("Su pago será con tarjeta o efectivo? 1 / 2")
    pago = int(input("Opción: "))

    if pago == 1:
        tarjeta = input("Con qué tarjeta deseas pagar: ")
        print("- EXCELENTE ya te damos el número de cuenta para tu depósito -")
        cliente = int(input("¿Eres cliente VIP? 1 / 2: "))

        if cliente == 1:
            oculto = "VIP1313"
            intentos = 1
            while intentos <= 3:
                clave = input("Ingresa tu contraseña VIP: ")
                if clave == oculto:
                    print("PERFECTO ERES CLIENTE VIP")
                    break
                else:
                    print("CLAVE INCORRECTA")
                    intentos += 1
                    
        else:
            print("Debes cancelar en caja con efectivo")
    else:
        print("-- Por favor cancelar en la caja --")

    # PREMIO POR VOCALES
    if contador==8:
        print("------------------------------")
        print(" No olvides retirar tu premio ")
        print("------- FELICIDADES ----------")
        print("------------------------------")
    else:
        print("PAGA TU VALOR FINAL: $", final)

    print("-----------------------------------------------")
    print("-- Espera, deseas ganarte una cerveza? 1 / 2 --")
    print("-----------------------------------------------")
    deseo = int(input("Opción: "))

    if deseo == 2:
        print("----------------------------------------------")
        print("- NO PASA NADA MUCHAS GRACIAS POR VISITARNOS -")
        print("----------------------------------------------")
    else:
        print("----------------------------------------------")
        print("------ VEN PARTICIPA EN ESTE ÚLTIMO JUEGO ----")
        print("----------------------------------------------")
        numero = int(input("Ingresa un número entre 1 y 100: "))

        if numero == 0:
            print("No existe ningún símbolo para representar el 0")
        elif numero > 1000:
            print("Muy alto")
        elif numero < 0:
            print("Debe ser positivo")
        else:
            if numero == 1000:
                print("M")
            else:
                nu = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
                nd = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
                nc = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

                centenas = numero // 100 % 10
                decenas = numero // 10 % 10
                unidades = numero % 10

                print("Número romano:", nc[centenas], nd[decenas], nu[unidades])
            print("----------------------------------")
            print("-  FELICIDADES GANASTE UNA BIELA -")
            print(" -------- VUELVE PRONTO ----------")
            print("----------------------------------")

else:  
    print(" PASA Y DISFRUTA DE NUESTRA SAZÓN ")