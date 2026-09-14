nombre = input("ingrese su nombre:")
cantidad = int(input("ingrese su nota:"))
suma = 0
inicio = 1
while inicio <= cantidad:
    nota = float(input(f"ingrese la nota:"))
    if nota < 2.0 or nota > 7.0:
        print("nota invalida")
    else:
        suma = suma + nota
        inicio = inicio + 1
promedio = suma / cantidad
if promedio >= 4.0:
    print(f"{nombre} su promedio es: {promedio} y esta aprobado")
else:
    print(f"{nombre} su promedio es: {promedio} y no esta aprobado, debe realizar un examen")
    examen = float(input("ingrese la nota del examen:"))
    while examen < 2.0 or examen > 7.0:
        print("nota invalida")
        examen = float(input("ingrese la nota del examen:"))
    if examen >= 4.0:
        print(f"{nombre} su promedio es: {promedio} y esta aprobado con examen")
    else:
        print(f"{nombre} su promedio es: {promedio} y no esta aprobado, debe repetir el curso")
