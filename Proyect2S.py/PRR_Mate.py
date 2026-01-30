ingresos = []
egresos = []

contra = "CONTROLPRO1313"
while True:
    print("================================")
    print("========= BEIENVENIDO ==========")
    print("================================")
    print("========= CONTROL PRO ==========")
    print("================================")
    print("-------------------")
    print("1. Agregar ingresos")
    print("-------------------")
    print("------------------")
    print("2. Agregar egresos")
    print("------------------")
    print("----------------------")
    print("3. Ver resumen mensual")
    print("----------------------")
    print("--------")
    print("4. Salir")
    print("--------")
    
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        while True:
            try:
                ingreso = input("->""Realice su ingreso (`fin` para volver al menú): ")
                
                if ingreso.lower() == "fin":
                    break
                
                ingreso = float(ingreso)
                if ingreso < 0:
                    print("No se permiten valores negativos")
                else:
                    ingresos.append(ingreso)
                    print("******************")
                    print("Ingreso registrado")
                    print("******************")
            except ValueError:
                print("Ingrese solo números")

    elif opcion == "2":
        while True:
            try:
                egreso = input("->""Realice un egreso (`fin` para volver al menú): ")
                
                if egreso.lower() == "fin":
                    break
                
                egreso = float(egreso)
                if egreso < 0:
                    print("No se permiten valores negativos")
                else:
                    egresos.append(egreso)
                    print("*****************")
                    print("Egreso registrado")
                    print("*****************")

            except ValueError:
                print("Ingrese solo números")

    elif opcion == "3":
        totingresos = sum(ingresos)
        totegresos = sum(egresos)
        balance = totingresos - totegresos

        print("\n========= RESUMEN MENSUAL =========")
        print("=======================================")
        print(f"Total ingresos: $ {totingresos:.2f}")
        print("=======================================")
        print("======================================")
        print(f"Total egresos:  $ {totegresos:.2f}")
        print("======================================")
        print("=====================================")
        print(f"Gasto mensual: $ {totegresos:.2f}")
        print("================================= ===")
        print("===============================")
        print(f"Balance final: $ {balance:.2f}")
        print("===============================")

        if totingresos > 0:
            proporcion = totegresos / totingresos
            porcentaje = proporcion * 100

            print("\n----- ANÁLISIS PROPORCIONAL -----")
            print(f"Los egresos representan el {porcentaje:.3f}% de los ingresos")

            if porcentaje < 50:
                print("->""Excelente control")
            elif 50 <= porcentaje <= 80:
                print("->""Buen control financiero")
            elif 80 < porcentaje <= 100:
                print("->""Alerta: tus gastos son muy altos")
            else:
                print("->""Peligro financiero: gastas más de lo que ganas")
        else:
            print("\nNo se puede realizar comparación proporcional sin ingresos")

        if balance > 0:
            print("Ahorro positivo")
        elif balance < 0:
            print("Déficit financiero")
        else:
            print("Sin ganancia ni pérdida")
            
    elif opcion == "4":
        intentos = 3
        while intentos > 0:
            print("-------------------------------------------------")
            clave = input("Ingrese la contraseña para asegurar y salir : ")
            print("-------------------------------------------------")
            if clave == contra:
                print("====================================")
                print("=== Gracias por usar CONTROL PRO ===")
                print("====================================")
                exit()
            else:
                intentos -= 1
                print("******************************************************")
                print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
                print("******************************************************")

        print("Acceso denegado. Regresando al menú...")

    else:
        print("Opción inválida, intente nuevamente")