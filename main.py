from tkinter import *
import json
from datetime import datetime
import pip._vendor.requests as requests
import time
from weather import weather_widget
from make_draggable import make_draggable
from calculator import *
from stopwatch import *
from timer import *
from to_do_list import To_Do_List
from stickynote import Sticky_Note
from calendar_1 import CALENDAR

#Initialize Window

root = Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
root.title("Your study spacce")
     
#Frontend part of code - Interface

# stickyNoteWidget = Frame(root, bd = 4, bg = 'white')
# stickyNoteWidget.place(x=10, y=20)
# make_draggable(stickyNoteWidget)

# notes = Text(stickyNoteWidget)
# notes.pack()

weatherWidget = weather_widget(root)
stopwatchWidget = Stopwatch(root)
todolist = To_Do_List(root)
calculatorWidget = Calculator(root)
timerWidget = Timer(root)
stickynote = Sticky_Note(root)
calendar = CALENDAR(root)

root.mainloop()
