import serial #cargamos la libreria serial


import serial.tools.list_ports

i = 1
print("Listando los puertos disponibles: ")
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print(str(i) + '. ' + port.device)

indice_puerto = int(input("\nElija el numero del puerto de su preferencia: "))
indice_puerto -= 1
ser = serial.Serial(port[indice_puerto], 9600) #inicializamos el puerto de serie a 9600 baud

#variable para almacenar el mensaje
#le asignamos un valor introducido por el usuario
old_value = 'l'
while True:
    entrada = input("Introduzea un caracter 'h' para encender el LED o 'l' para apagarlo: ")
    # Se verifica si cambia el valor ingresado para ver si se justifica mandar el comando
    if entrada != old_value:
        if entrada == 'h' or entrada == 'l':
            ser.write(entrada.encode("ascii","ignore")) #envia la entrada por serial
        else:
            print("Opcion invalida")
        old_value = entrada
    otra_vez = input("Desea otra vez (S: Si - N: No): ")
    if otra_vez == 'N':
        print("Chao bambino")
        break
    elif otra_vez != 'S':
        print("ERROR!!! y Chao bambino")
        break
ser.close()

            






