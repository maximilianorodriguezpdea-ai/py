combustible = float(input("Ingrese el tipo del combustible: "))
cantidad = float(input("Ingrese la cantidad de combustible en litros: "))
precio = float(input("Ingrese el precio por litro del combustible: "))
dinero_entregado = float(input("Ingrese el dinero entregado: "))

costo_total = cantidad * precio
iva_incluido = costo_total * 1.19
vuelto = dinero_entregado - iva_incluido

print(f"el costo total del combustible {combustible} es ${iva_incluido} y el vuelto es ${vuelto}")
