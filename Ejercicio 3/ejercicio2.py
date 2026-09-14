nombre = input("Ingrese su nombre: ")
consumodeelectricidad = float(input("Ingrese el consumo de electricidad en kWh: "))

valorkwh = 180
cargofijo = 3500

costototal = (consumodeelectricidad * valorkwh)
if consumodeelectricidad <= 200:
    