nombre = input("ingrese su nombre:")
distancia = float(input("ingrese la distancia del viaje en km:"))
rendimiento = float(input("ingrese el rendimiento del vehículo en km/l:"))
precio = float(input("ingrese el precio del combustible por litro:"))

litros_consumidos = distancia / rendimiento
costo_total_combustible = litros_consumidos * precio
costo_aproximado_km = costo_total_combustible / distancia

print(f"nombre: {nombre}, costo aproximado por km: {costo_aproximado_km}")