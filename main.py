import random
import webbrowser
from tkinter import *
from tkinter.messagebox import askyesno

import pyautogui

root = Tk()


def doDesktop():
    websites = ["dcps.instructure.com", "https://dcps.instructure.com/courses/237226", "https://dcps.instructure.com/courses/237724", "https://dcps.instructure.com/courses/236450",
            "https://dcps.instructure.com/courses/237343", "https://dcps.instructure.com/courses/235737", "https://dcps.instructure.com/courses/237343/modules", "https://dcps.instructure.com/courses/237226/modules"]
    pyautogui.hotkey('winleft', 'd')
    brave_file = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
    webbrowser.get(brave_file).open(random.choice(websites))


def confirm():
    answer = askyesno(title='confirmation',
                      message='ya sure bud?')
    if answer:
        root.destroy()
        doDesktop()
    else:
        root.destroy()

confirm()
# start the app
root.mainloop()