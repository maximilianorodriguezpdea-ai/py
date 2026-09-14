nombre = input("Ingrese su nombre: ")
personas = int(input("Ingrese el número de personas: "))
precio = float(input("Ingrese el precio por persona: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

subtotal = personas * precio
valor_propina = subtotal * (porcentaje_propina / 100)
iva = subtotal * 0.19
total = subtotal + valor_propina + iva
valor_por_persona = total / personas

print(f"El total a pagar es: ${total} pesos,con un valor de la propina es: ${valor_propina:.2f}, el valor del IVA es: ${iva:.2f}, y el valor por persona es: ${valor_por_persona:.2f}")