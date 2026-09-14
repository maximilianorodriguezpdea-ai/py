nombre = input("ingrese su nombre:")
nota1 = float(input("ingrese su nota 1:"))
nota2 = float(input("ingrese su nota 2:"))
nota3 = float(input("ingrese su nota 3:"))
nota4 = float(input("ingrese su nota 4:"))

promedio = (nota1 + nota2 + nota3 + nota4) / 4
if promedio >= 4.0:
    print("hola,{nombre}, usted aprobo con un promedio de:",{promedio})
else:
    print("hola,{nombre}, usted no aprobo con un promedio de:",{promedio})
