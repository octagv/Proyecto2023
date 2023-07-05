import tkinter as tk
from gui.Lateralgui import Lateral
from gui.principalgui import Principal
from gui.tablegui import Table
from functools import partial

def open(widget, other_widget):
    widget.pack()
    for other in other_widget:
        other.unpack()
    
root = tk.Tk()
root.geometry("1080x720")

menu = Lateral(root)
principal = Principal(root)
principal.createImage()

menu.createImages()
menu.pack(0,0)
principal.pack(291,0)
root.mainloop()