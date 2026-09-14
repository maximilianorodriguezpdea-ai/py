nombre = input("Ingrese su nombre: ")
largo = float(input("Ingrese el largo de la habitacion en metros: "))
ancho = float(input("Ingrese el ancho de la habitacion en metros: "))
precio= float(input("Ingrese el precio por metro cuadrado: "))

area = largo * ancho
costo_instalacion = area * precio
iva = costo_instalacion * 0.19
total = costo_instalacion + iva

print(f"nombre: {nombre}, costo total de la instalacion: {costo_instalacion}")