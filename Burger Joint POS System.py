import time

combo_simple = 5
combo_doble = 6
combo_triple = 7
postre = 2
pedidos = []
encargados_permitidos = ["juan", "maria", "pedro"]
encargado_actual = ""

while True:
    if not encargado_actual:
        print("Bienvenidos a Hamburguesas IT")
        encargado_actual = str(input("Ingrese su nombre de encargado: "))
        if encargado_actual not in encargados_permitidos:
            print("Lo siento, no tiene permiso para acceder al sistema.")
            encargado_actual = ""
            continue
        print(f"Hamburguesas IT\nEncargado -> {encargado_actual}\nRecuerda, siempre hay que recibir al cliente con una sonrisa")
        print("1 - Ingreso nuevo pedido")
        print("2 - Cambio de turno")
        print("3 - Cerrar programa")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cant_combo_simple = int(input("Ingrese cantidad de combo S: "))
        cant_combo_doble = int(input("Ingrese cantidad de combo D: "))
        cant_combo_triple = int(input("Ingrese cantidad de combo T: "))
        cant_postre = int(input("Ingrese cantidad de combo Flurby: "))
        total = cant_combo_simple * combo_simple + cant_combo_doble * \
            combo_doble + cant_combo_triple * combo_triple + cant_postre * postre
        print(f"Total {total} ")
        abono = float(input("Abona con $: "))
        vuelto = abono - total
        print(f"Vuelto {vuelto} ")
        confirmacion = input("¿Confirma pedido? Y/N: ")
        if confirmacion.lower() == "y":
            now = time.localtime()
            current_time = time.strftime("%a %b %d %H:%M:%S %Y", now)
            pedido = {
                "cliente": nombre_cliente,
                "fecha": current_time,
                "combo_simple": cant_combo_simple,
                "combo_doble": cant_combo_doble,
                "combo_triple": cant_combo_triple,
                "postre": cant_postre,
                "total": total,
                "abono": abono,
                "vuelto": vuelto
            }
            pedidos.append(pedido)
            with open("ventas.txt", "a") as archivo:
                archivo.write(f"{nombre_cliente};{current_time};{cant_combo_simple};{cant_combo_doble};{cant_combo_triple};{cant_postre};{total}\n")
            print("Pedido confirmado. ¡Buen provecho!")
        else:
            print("Pedido cancelado.")
    elif opcion == "2":
        encargado_actual = ""
        print("Cambio de turno exitoso")
    elif opcion == "3":
        print("Hasta pronto")
        break
    else:
        print("Ingrese una opcion valida")
