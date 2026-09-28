ficha = 1
while ficha != 0:
    ficha = int(input("ingrese numero de ficha:"))
nombre = input("ingrese nombre del trabajador:")
sBruto = float(input("ingrese sueldo bruto:"))

if ficha > 0 and nombre != "" and sBruto >0:
    if sBruto <= 500000:
        descuento = sBruto * 0.10
    if sBruto >= 500001 and sBruto <= 1000000:
        descuento = sBruto * 0.12
    if sBruto > 1000001:
        descuento = sBruto * 0.15

    sliquido = sBruto - descuento

    print("Ficha:", ficha)
    print("Nombre:", nombre)
    print("Sueldo Bruto:", sBruto)
    print("Descuento:", descuento)
    print("Sueldo Neto:", sliquido)
    ficha = 