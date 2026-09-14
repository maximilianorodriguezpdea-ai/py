nombre = input("Ingrese su nombre: ")
saldodisponible = float(input("Ingrese su saldo disponible: "))
cantidadviaje = int(input("Ingrese la cantidad de viajes: "))
valorviaje = float(input("Ingrese el valor de cada viaje: "))

costo_total = cantidadviaje * valorviaje
dinero_restante = saldodisponible - costo_total

if saldo_disponible >= costo_total:
    print(f"Hola {nombre}, su saldo disponible es suficiente para realizar {cantidadviaje} viajes.")
else:
    print(f"Hola {nombre}, su saldo disponible no es suficiente para realizar {cantidadviaje} viajes. Le faltan {abs(dinero_restante)} unidades de dinero.")
