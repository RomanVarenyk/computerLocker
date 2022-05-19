from tkinter import *
import ctypes
from tkinter import ttk
from tkinter.messagebox import askyesno

root = Tk()


# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                      message='ya sure bud?')
    if answer:
        root.destroy()
        ctypes.windll.user32.LockWorkStation()
    else:
        root.destroy()


confirm()
# start the app
root.mainloop()
