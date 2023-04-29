from tkinter import *
import json
from datetime import datetime
import pip._vendor.requests as requests
import time
from weather import weather_widget
from make_draggable import make_draggable
from calculator import *
from stopwatch import *

#Initialize Window

root = Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
root.title("Your study spacce")
     
#Frontend part of code - Interface

weatherWidget = weather_widget(root)
stopwatchWidget = Stopwatch(root)
calculator_widget = Calculator(root)

stickyNoteWidget = Frame(root, bd = 4, bg = 'white')
stickyNoteWidget.place(x=10, y=20)
make_draggable(stickyNoteWidget)

notes = Text(stickyNoteWidget)
notes.pack()

root.mainloop()
