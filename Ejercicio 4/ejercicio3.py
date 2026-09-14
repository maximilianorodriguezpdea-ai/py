nombre = input("ingrese su nombre:")
precioproducto = float(input("ingrese el precio del producto:"))
cantidadproducto = int(input("ingrese la cantidad del producto:"))

if precioproducto >= 1000 and cantidadproducto >=1 and cantidadproducto <=20:
    total = precioproducto * cantidadproducto
    print(f"los datos de la compra son validos")
    if cantidadproducto >=5 and total >= 50000:
        descuento = total * 0.10
        totalfinal = total - descuento
        print(f"tienes un 10% de descuento, el total a pagar es {totalfinal}")
    else:
        print(f"no tienes descuento, el total a pagar es {total}")
else:
    print("los datos no son validos")