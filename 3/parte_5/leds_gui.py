from tkinter import *
from gpiozero import LED, PWMLED
from signal import pause

class LedsGui(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.ban = BooleanVar(value=False) # Bandera que indica si la luz esta prendida o apagada.

        """ Configurando elementos fisicos de la rPi """
        self.led = LED(17)
        self.led.off()
        self.ledPWM = PWMLED(18)
        self.ledPWM.value = 0

        """ Agregando los elementos de la interfaz grafica """
        self.pack()
        # Boton ON/OFF
        self.buttonLed = Button(self , text='ON', command=self.ledChange) 
        self.buttonLed.pack(pady=5)
        # Slider para el pwm
        self.ledPWMScale = Scale(self,label='Dutty',
                            command=self.changePWM,
                            from_=0 , to=100 ,length=200,
                            tickinterval=20,
                            orient='horizontal')
        self.ledPWMScale.pack(expand=YES, fill=Y)

    
    def ledChange(self):
        # Funcion para prender y apagar el led 
        if self.ban.get() == False:
            self.ban.set(True)
            print("led on")
            self.buttonLed.config(text = "OFF") 
            self.led.on()
        else:
            self.ban.set(False)
            print("led off")
            self.buttonLed.config(text = "ON") 
            self.led.off()
    
    def changePWM(self,value):
        # Funcion para cambiar el dutty del led
        dutty = float(value)/100
        print(dutty)
        self.ledPWM.value = dutty
    
if __name__ == '__main__':
    LedsGui().mainloop()
    

