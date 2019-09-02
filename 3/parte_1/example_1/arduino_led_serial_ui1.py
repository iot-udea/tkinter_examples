from tkinter import *
import serial #cargamos la libreria serial
import serial.tools.list_ports



class UILedSerial(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()
        # Variables de la aplicacion
        self.port_sel = StringVar(self)
        self.banConectar = False
        self.ledState = False


        ports = serial.tools.list_ports.comports(include_links=False)
        self.dic_ports = {}
        for port in ports:
            self.dic_ports[port.name] = port.device
        
        list_ports = list(self.dic_ports.keys())
        

        self.port_sel.set(list_ports[0]) # default value



        # Agregando frames principales       
        self.mainFrame = Frame(self)         
        self.fConectar = LabelFrame(self,text="Conectar")
        self.optionSer = OptionMenu(self.fConectar, self.port_sel, *list_ports)
        self.bConnectar = Button(self.fConectar,text = "Conectar", command = self.conectar)
        self.lConectar = Label(self.fConectar,text = "Desconectado")
        self.optionSer.pack()
        self.bConnectar.pack()
        self.lConectar.pack()

        self.fControl = Frame(self)
        self.bOnOff = Button(self.fControl,text = "ON", command = self.on_off_light)
        self.bOnOff.pack()

        self.fConectar.pack(side = 'left',fill = Y,expand= YES)
        self.fControl.pack(side = 'right',fill = Y,expand= YES)

    def on_off_light(self):
        if self.ledState == False:
            self.ser.write('h'.encode("ascii","ignore")) #envia la entrada por serial
            self.bOnOff.config(text = "OFF")
            self.ledState = True
        else:
            self.ser.write('l'.encode("ascii","ignore"))
            self.bOnOff.config(text = "ON")
            self.ledState = False

    def conectar(self):
        if self.banConectar == False:
            print("Conectando a: " + self.port_sel.get())  
            self.ser = serial.Serial(self.dic_ports[self.port_sel.get()], 9600)  
            self.bConnectar.config(text = "Desconectar")
            self.lConectar.config(text = 'Conectado')
            self.banConectar = True
        else:
            print("Desconectanto de: " + self.port_sel.get())  
            self.ser.close()
            self.bConnectar.config(text = "Conectar")
            self.lConectar.config(text = 'Desconectado')
            self.banConectar = False


# Allow the class to run stand-alone.
if __name__ == "__main__":
    app = UILedSerial()
    app.mainloop()


