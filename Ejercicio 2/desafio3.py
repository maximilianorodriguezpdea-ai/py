nombre = input("ingrese su nombre:")
precio = float(input("ingrese el precio del producto:"))
cantidad = int(input("ingrese la cantidad de productos:"))

subtotal = precio * cantidad
if subtotal >= 50000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    print(f"hola,{nombre}, usted tiene un descuento de ${descuento} y el total a pagar es ${total}")
else:
    print(f"hola,{nombre}, usted no tiene descuento y el total a pagar es ${subtotal}")      