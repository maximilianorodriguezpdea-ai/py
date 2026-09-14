marca_automovil = input("Ingrese la marca del automóvil: ")
precio_automovil = float(input("Ingrese el precio del automóvil: "))
porcentaje_inicial = float(input("Ingrese el porcentaje de inicial: "))
cuotas = int(input("Ingrese el número de cuotas: "))

valor_pie_inicial = precio_automovil * (porcentaje_inicial / 100)
monto_por_pagar = precio_automovil - valor_pie_inicial
valor_cuota = monto_por_pagar / cuotas

print(f"el valor pie inicial es: ${valor_pie_inicial}")
print(f"el monto por pagar es: ${monto_por_pagar}")
print(f"el valor de cada cuota es: ${valor_cuota}")