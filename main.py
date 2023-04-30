from tkinter import *
import json
from datetime import datetime
import pip._vendor.requests as requests
import time
from weather import weather_widget
from make_draggable import make_draggable
#from calculator import *
from stopwatch import *
from timer import *
from to_do_list import To_Do_List
from stickynote import Sticky_Note
from clock import DigitalClock
from Sidebar import *

#Initialize Window

root = Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
root.title("Your study space")

def addWeather():
    #parent = Sticky_Note.nametowidget(Sticky_Note.winfo_parent())
    weather2 = weather_widget(root)

def addStickyNotes():
    note = Sticky_Note(root)
    
def addTimer():
    timer2 = Timer(root)
#Frontend part of code - Interface

sb = Sidebar(root)
sb.add_spacer('Menu')
sb.add_button('Weather', command = addWeather)
sb.add_button('Sticky Notes', command = addStickyNotes)
sb.add_button('Timer', command=addTimer)

# stickyNoteWidget = Frame(root, bd = 4, bg = 'white')
# stickyNoteWidget.place(x=10, y=20)
# make_draggable(stickyNoteWidget)

# notes = Text(stickyNoteWidget)
# notes.pack()

weatherWidget = weather_widget(root)
stopwatchWidget = Stopwatch(root)
todolist = To_Do_List(root)
#calculatorWidget = Calculator(root)
timerWidget = Timer(root)
stickynote = Sticky_Note(root)

root.mainloop()
