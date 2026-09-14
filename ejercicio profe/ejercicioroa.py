cantidad_notas =int(input("ingrese la cantidad de notas:"))
cantidad_notas = cantidad_notas + 1

for i in range(1, cantidad_notas):
    nota = float(input("ingrese la nota:"))
    #-- valide nota
    while nota < 2.0 or nota > 7.0:
        print("nota invalida")
        nota = float(input("ingrese su nota"))
    suma = suma + nota
    promedio = round(suma / (cantidad_notas - 1), 1)

if promedio >= 4.0:
    print("aprobado")
else:
    print("reprobaste, debes hacer un examen")
    