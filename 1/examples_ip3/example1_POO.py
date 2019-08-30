import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

class GrapGui(tkinter.Frame):
    def __init__ (self, master = None):
        # Construct the Frame object.
        tkinter.Frame.__init__(self, master) 
        self.pack()       
        # ---------------------------------------------------------------------------
        # Paso 1: Agregando los elementos en la ventana principal
        # ---------------------------------------------------------------------------

        # 1. Grafico (Dentro de la ventana raiz)
        fig = Figure(figsize=(5, 4), dpi=100)   # Figura asociada
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        self.canvas = FigureCanvasTkAgg(fig, master=self)  # tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
        # 2. Boton (Dentro de la ventana raiz)
        button = tkinter.Button(master=self, text="Quit", command=self._quit)
        button.pack(side=tkinter.BOTTOM)
        
        # ---------------------------------------------------------------------------
        # Paso 2: Conectar eventos
        # ---------------------------------------------------------------------------

        # Conectando eventos con funciones handler
        self.canvas.mpl_connect("key_press_event", self.on_key_press)

    # ---------------------------------------------------------------------------
    # Paso 3: Definir las funciones handler
    # ---------------------------------------------------------------------------

    # Funciones handler de los eventos

    def _quit(self):
        self.quit()     # stops mainloop
        self.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        
# ---------------------------------------------------------------------------
# Paso 5: Llamar el ciclo principal
# ---------------------------------------------------------------------------
# Allow the class to run stand-alone.
if __name__ == "__main__":
    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")
    app = GrapGui(master=root)    
    app.mainloop()
    