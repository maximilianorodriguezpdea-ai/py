nombre = input("Por favor, ingresar tu nombre:")
cantidad = int (input("ingrese la cantidad" ))
precio = float (input("ingrese precio:"))
dinero = float (input("ingrese su dinero"))

subTotal = cantidad * precio
iva = (subTotal * 19)/100
totalApagar = subTotal * iva
vuelto = dinero - totalApagar

nombre = input("trabajador, ingrece su nombre" )
