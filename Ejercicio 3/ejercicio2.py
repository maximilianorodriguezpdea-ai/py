nombre = input("Ingrese su nombre: ")
consumodeelectricidad = float(input("Ingrese el consumo de electricidad en kWh: "))

valorkwh = 180
cargofijo = 3500

costototal = (consumodeelectricidad * valorkwh)
if consumodeelectricidad <= 200:
    costototal += cargofijo
    print(f"Hola {nombre}, su consumo de electricidad es de {consumodeelectricidad} kWh. El costo total a pagar es de {costototal} unidades de dinero.")                                                                                                                                       