import random
import webbrowser
from tkinter import *
from tkinter.messagebox import askyesno

import pyautogui

root = Tk()
websites = []
def getWebsites():
    webList =  open("websites.txt", "r")
    for i in webList.readlines():
        websites.append(i)

def doDesktop():

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


# confirm()
# start the app
# root.mainloop()
# auto-py-to-exe
getWebsites()
doDesktop()