import tkinter
from tkinter import messagebox


def confirm(title, message, *args):
    # build and hide the main tkinter window
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()


def yesno(title, message):
    # build and hide the main tkinter window
    root = tkinter.Tk()
    root.withdraw()
    result = messagebox.askyesno(title, message)
    root.destroy()
    return result
