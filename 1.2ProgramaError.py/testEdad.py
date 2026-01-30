import calculos

resultado1=calculos.calcularEdad(2050)
if resultado1==-1:
    print("Año nacimiento: 2050 => Usted aun no nace, o nació antes de cristo")

resultado2=calculos.calcularEdad(-10)
if resultado2==-1:
    print("Año nacimiento: -10 =>Usted aun no nace, o nació antes de cristo")

resultado3=calculos.calcularEdad(2024)
print(f"Año nacimiento: 2024 =>Este año cumple {resultado3} años")

resultado4=calculos.calcularEdad(2013)
print(f"Año nacimiento: 2013 =>Este año cumple {resultado4} años")
