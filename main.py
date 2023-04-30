from tkinter import *
from datetime import datetime
import pip._vendor.requests as requests
import time
from weather import weather_widget
from stopwatch import *
from timer import *
from to_do_list import To_Do_List
from stickynote import Sticky_Note
from clock import DigitalClock
from Sidebar import *
from calendar_1 import CALENDAR

#Initialize Window

root = Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
root.title("Your study space")

def addWeather():
    weather2 = weather_widget(root)

def addStickyNotes():
    note = Sticky_Note(root)
    
def addTimer():
    timer2 = Timer(root)
    
def addStopwatch():
    stopwatch = Stopwatch(root)
    
def addToDoList():
    todo = To_Do_List(root)
    
def addClock():
    clock = DigitalClock(root)

def addCalendar():
    calender = CALENDAR(root)
    
#Frontend part of code - Interface

sb = Sidebar(root, width = 150)
sb.add_spacer('Menu')
sb.add_button('Weather', command=addWeather)
sb.add_button('To-do List', command=addToDoList)
sb.add_button('Sticky Notes', command=addStickyNotes)
sb.add_button('Clock', command=addClock)
sb.add_button('Timer', command=addTimer)
sb.add_button('Stopwatch', command=addStopwatch)
sb.add_button('Calendar', command=addCalendar)

root.mainloop()
