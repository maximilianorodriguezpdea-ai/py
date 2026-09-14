nombre_proyecto = input("Ingrese el nombre del proyecto: ")
largo_invernadero = float(input("Ingrese el largo del invernadero en metros: "))
ancho_invernadero = float(input("Ingrese el ancho del invernadero en metros: "))
precio_m2 = float(input("Ingrese el precio por metro cuadrado: "))
cantidad_planta = int(input("Ingrese la cantidad de plantas: "))
precio_planta = float(input("Ingrese el precio por planta: "))

area_invernadero = largo_invernadero * ancho_invernadero
costo_material = area_invernadero * precio_m2
costo_plantas = cantidad_planta * precio_planta
subtotal = costo_material + costo_plantas
costo_promedio_Planta = subtotal / cantidad_planta

print(f"El costo total del proyecto {nombre_proyecto} es: ${subtotal}, con un costo promedio por planta de: ${costo_promedio_Planta}")