nombre = input("ingrese su nombre:")
sueldobase = float(input("ingrese su sueldo base:"))
horasextras = float(input("ingrese las horas extras trabajadas:"))
valorhoraextra = float(input("ingrese el valor de la hora extra:"))

pagohorasextras = horasextras * valorhoraextra
sueldobruto = sueldobase + pagohorasextras
descuento = (sueldobruto * 10) / 100
sueldoliquido = sueldobruto - descuento

print(f"nombre: {nombre}, sueldo líquido: {sueldoliquido}")