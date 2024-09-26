import time
from tkinter import *
from tkiniter import messagebox

window = Tk()
window.geometry("300x300")

window.title("Timer Countdown")

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

#setting the default values
hours.set("00")
minutes.set("00")
seconds.set("00")


hrs = Entry(window)