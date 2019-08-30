"""
https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
"""

import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

# ---------------------------------------------------------------------------
# Paso 3: Definir las funciones handler
# ---------------------------------------------------------------------------

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# ---------------------------------------------------------------------------
# Paso 1: Agregando los elementos en la ventana principal
# ---------------------------------------------------------------------------

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# 1. canvas
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# 2. toolbar
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# 3. button
button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)


# ---------------------------------------------------------------------------
# Paso 2: Conectar eventos
# ---------------------------------------------------------------------------
canvas.mpl_connect("key_press_event", on_key_press)


tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
