nombre = input ("ingrese su nombre:")
not1 = float(input("ingrese su primera nota:"))
not2 = float(input("ingrese su segunda nota:"))
not3 = float(input("ingrese su tercera nota"))
not4 = float(input("ingrese su cuarta nota:"))

if not1 >= 2.0 and not1 <= 7.0:
    if not2 >= 2.0 and not2 <= 7.0:
        if not3 >= 2.0 and not3 <= 7.0:
            if not4 >= 2.0 and not4 <= 7.0:
                promedio = (not1 + not2 + not3 + not4) / 4
                print(f"El promedio de {nombre} es: {promedio}")
                if promedio >= 4.0:
                    print("aprobado")
                else:
                    print("reprobado")
            else:
                print("la nota ingresada no es valida")
        else:
            print("la nota ingresada no es valida")
    else:
        print("la nota ingresada no es valida")
else:
    print("ingrese una nota valida entre el 2.0 y el 7.0")
