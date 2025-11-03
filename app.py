from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=500)
frm.grid()
ttk.Button(frm, command=root.destroy).grid(column=1, row=0)
root.mainloop()