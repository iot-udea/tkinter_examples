"""
https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
"""

import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

# Creacion de la ventana principal (Raiz)
root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# ---------------------------------------------------------------------------
# Paso 3: Definir las funciones handler
# ---------------------------------------------------------------------------

# Funciones handler de los eventos

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def on_key_press(event):
    print("you pressed {}".format(event.key))
    #key_press_handler(event, canvas, toolbar)


# ---------------------------------------------------------------------------
# Paso 1: Agregando los elementos en la ventana principal
# ---------------------------------------------------------------------------

# 1. Grafico (Dentro de la ventana raiz)
fig = Figure(figsize=(5, 4), dpi=100)   # Figura asociada
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
canvas = FigureCanvasTkAgg(fig, master=root)  # tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) # Definiendo ubicacion y caracteristicas de la
                                                                           # tk.DrawingArea 
# 2. Boton (Dentro de la ventana raiz)
button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

# ---------------------------------------------------------------------------
# Paso 2: Conectar eventos
# ---------------------------------------------------------------------------

# Conectando eventos con funciones handler
canvas.mpl_connect("key_press_event", on_key_press)


# ---------------------------------------------------------------------------
# Paso 5: Llamar el ciclo principal
# ---------------------------------------------------------------------------
tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
