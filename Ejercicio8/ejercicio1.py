codigo = 1
while codigo != 0:
    codigo = int(input("ingrese su codigo: "))
    if codigo == 0:
        break
    nombre = input("ingrese su nombre: ")
    precio = float(input("ingrese el precio del producto: "))
    cventas = int(input("ingrese la cantidad de ventas: "))
    if precio > 0 and cventas >0:
        subtotal = precio * cventas
        if subtotal >= 100000:
            porcentaje = "5%"
            descuento = subtotal * 0.05
        if subtotal > 100000 and subtotal <=300000:
            porcentaje = "10%"
            descuento = subtotal * 0.10
        if subtotal > 300000:
            porcentaje = "15%"
            descuento = subtotal * 0.15

            mdescuento = subtotal - descuento

        print(f"Codigo: {codigo}")
        print(F"Nombre: {nombre}")
        print(f"Precio: {precio}")
        print(f"Cabtidad de ventas: {cventas}")
        print(f"Subtotal: ${subtotal}")
        print(f"Descuento: {descuento}")
        print(f"Monto descuento: {mdescuento}")
    else:
        print("ingreso algo mal, revisa los datos")


