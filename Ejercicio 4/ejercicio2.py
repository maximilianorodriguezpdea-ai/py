nombre = input("ingrese su nombre:")
temperaturaactual = float(input("ingrese la temperatura actual:"))
humedad = float(input("ingrese la humedad actual:"))
velocidadviento = float(input("ingrese la velocidad del viento:"))

if temperaturaactual >= 30 and humedad <= 30 and velocidadviento >= 30:
    print("Riesgo de incendio en la zona alerta!!!")
else:
    print("No hay riesgo de incendio en la zona")
    