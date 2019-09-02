from PIL import ImageTk, Image

import RPi.GPIO as GPIO
import tkinter as tk
import tkinter.font
import picamera
import time
import os

lightPin=13

win = tk.Tk()
my_font = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

win.geometry('480x320')
win.title("PiCamerAPP")
win.attributes('-fullscreen', True)
win.bind('<Escape>', lambda e: win.destroy())

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightPin, GPIO.OUT)

led = GPIO.PWM(13, 100)


def led_on():
    if scale.get() > 0:
        scale.set(0)
        led_button["text"] = "Led on"
    else:
        scale.set(100)
        led_button["text"] = "Led off"


def exit_program():
    GPIO.cleanup()
    win.destroy()

        
def take_picture():
    current_intensity = scale.get()
    
    change_light(100)
    time.sleep(5)
    
    try:
        cam = picamera.PiCamera()
        cam.resolution = (120, 100)
        cam.capture('foto.jpg', use_video_port=True)
        img = ImageTk.PhotoImage(Image.open("foto.jpg"))
        panel.configure(image=img)
        panel.image = img
    except Exception as e:
        print(e)
    else:
        change_light(current_intensity)
    finally:
        cam.close()
        
    
def change_light(value):
    led.start(0)
    led.ChangeDutyCycle(int(value))
    

    
panel = tk.Label(win, text='The picture goes here!!')
panel.pack(fill=tk.BOTH, expand=True)

led_button = tk.Button(
    win, text='Led on',
    font=my_font,
    width=10,
    command=led_on
)
led_button.pack()

cam_button = tk.Button(
    win,
    text='Shot!',
    font=my_font,
    width=10,
    command=take_picture
)
cam_button.pack()

exit_button = tk.Button(
    win,
    text='Exit',
    font=my_font,
    command=exit_program,
    fg='red',
    width=10
)
exit_button.pack()

config_button = tk.Button(
    win,
    text='Configuration',
    font=my_font,
    fg='blue',
    width=10
)
config_button.pack(side=tk.LEFT)

scale = tk.Scale(
    win,
    font=my_font,
    orient='horizontal',
    from_=0,
    to=100,
    command=change_light
)
scale.pack(side=tk.RIGHT)

tk.mainloop()
