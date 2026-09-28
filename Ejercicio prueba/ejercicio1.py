cont = 0
acum = 0
ticket = 1
while ticket != 0:
    ticket = int(input("ingrese el numero de ticket: "))
    if ticket < 0:
        print("el numero de ticket debe ser mayor a 0")
    if ticket == 0:
        break
    pat = input("ingrese su patente: ")
    if pat == "":
        print("la patente no es valida, ingrese bien su patente por favor")
    cant_h = float(input("ingrese la cantidad de horas: "))
    if cant_h < 0:
        print("ERROR!!, ingrese bien la cantidad de horas mayor a 0")
    if cant_h <= 2:
        tarifa = 2000
        tarifa_h = cant_h * 2000
    if cant_h >= 3 and cant_h <=5:
        tarifa = 1500
        tarifa_h = cant_h * 1500
    if cant_h >= 6:
        tarifa = 1000
        tarifa_h = cant_h * 1000
    tpagar = cant_h * tarifa_h
    cont = cont + 1
    acum = acum + tpagar
    print("======COBRO ESTACIONAMIENTO======")
    print(f"Numero de ticket: {ticket}")
    print(f"Patente: {pat}")
    print(f"Horas estacionado: {cant_h}")

    print(f"Patente: {pat}")
    print(f"Tarifa por hora: ${tarifa_h}")
    print(f"Total a pagar: ${tpagar}")
    while ticket == 0:
        print(f"Numero de ticket: {ticket}")
        print("No existe mas ticket por procesar")
        print("Programa finalizado")

        print("======RESUMEN DE CIERRE DE CAJA======")
        print(f"Cantidad de cobros realizados: {cont}")
        print(f"Total recaudado: {acum}")
