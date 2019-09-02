import serial #cargamos la libreria serial


import serial.tools.list_ports

i = 1
print("Listando los puertos disponibles: ")
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print(str(i) + '. ' + port.device)

indice_puerto = int(input("\nElija el puerto de su preferencia: "))
indice_puerto -= 1
ser = serial.Serial(port[indice_puerto], 9600) #inicializamos el puerto de serie a 9600 baud

#variable para almacenar el mensaje
#le asignamos un valor introducido por el usuario
entrada = input("Introduce un caracter ('s' para salir): ")
while entrada != 's': #introduciendo 's' salimos del bucle
    ser.write(entrada.encode("ascii","ignore")) #envia la entrada por serial
    print("He enviado: ", entrada)
    entrada = input("Introduce un caracter ('s' para salir): ")
ser.close()
