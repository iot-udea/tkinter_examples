import tkinter as tk
import tkinter.font
import picamera
from PIL import ImageTk, Image
import os


win=tk.Tk()
win.geometry('480x320')
win.title("PiCamerAPP")
myFont=tkinter.font.Font(family = 'Helvetica', size = 12, weight =  "bold")
win.attributes('-fullscreen', True)
win.bind('<Escape>',lambda e: win.destroy())

def takePicture():
    try:
        cam=picamera.PiCamera()
        cam.resolution = (320, 240)
        cam.capture('foto.jpg',use_video_port=True)
        img = ImageTk.PhotoImage(Image.open("foto.jpg"))
        panel.configure(image = img)
        panel.image=img
       
    finally:
        cam.close()
        
def exitProgram():
    win.destroy()
    
panel = tk.Label(win, text='Hola GUI tkinter')
panel.pack(fill=tk.BOTH, expand=True)   
camButton=tk.Button(win, text='Shot!', font=myFont, command=takePicture, bg='bisque2')
camButton.pack(fill=tk.X, expand=True)
exitButton=tk.Button(win, text='Exit', font=myFont, command=exitProgram, bg='cyan')
exitButton.pack(fill=tk.X, expand=True)

tk.mainloop()
