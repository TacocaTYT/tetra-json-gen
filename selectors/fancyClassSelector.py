from generators.socket import user_input_array as socket
from tkinter import *


def mm():
    OPTIONS = [
        "Socket"
    ]

    master = Tk()

    mOS = StringVar(master)
    mOS.set(OPTIONS[0]) # default value

    w = OptionMenu(master, mOS, *OPTIONS)
    w.pack()

    def ok():
        master.destroy()

    button = Button(master, text="OK", command=ok)
    button.pack()

    mainloop()
    return mOS.get()

modGen = mm()

if modGen == 'Socket':
    socket()
else:
    mm()