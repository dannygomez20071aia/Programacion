
def calcularPromedio (not1,not2,not3):
    promedio1=(not1+not2+not3)/3
    return promedio1

def calcularSubtotal(precioProducto:float, cantidad:int, porcentajeDescuento:float):
    subtotalSinDescuento = precioProducto * cantidad
    descuento = subtotalSinDescuento * porcentajeDescuento /100
    subtotal = subtotalSinDescuento -descuento
    return subtotal    


def consultarMulta (tipomulta:int):
    if tipomulta == 1:
        return 10
    elif tipomulta == 2:
        return 15
    elif tipomulta == 3:
        return 20
    elif tipomulta == 4:
        return 30
    else:
        return -1

def calcularValorHora (salario:float):
    valorhora = salario/160
    return valorhora

def calcularValorDescuento ( precio:float, porcentajeDescuento: float):
    descuento = precio *porcentajeDescuento / 100
    return descuento