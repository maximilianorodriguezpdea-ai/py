nombre = input("Ingrese su nombre: ")
consumo = float(input("Ingrese el consumo de energia en kwh: "))
precio = float(input("Ingrese el precio por kwh: "))
cargo_fijo = float(input("Ingrese el cargo fijo: "))

costo_consumo = consumo * precio
subtotal = costo_consumo + cargo_fijo
iva = subtotal * 0.19
descuento =subtotal + iva

print(f"nombre: {nombre}, costo total de la factura: {descuento}")