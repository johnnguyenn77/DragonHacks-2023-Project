# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from make_draggable import make_draggable
 
# Create Object

# Set geometry

class CALENDAR:
    def __init__(self, root): 
        self.frame = Frame(root, bd = 4, bg = 'sky blue')
        self.frame.place(x=10, y=20)
        make_draggable(self.frame)

        self.today1 = str(date.today())
        self.todayy = self.today1.split("-")
    # Add Calendar
        self.cal = Calendar(self.frame, year = int(self.todayy[0]), month = int(self.todayy[1]),day = int(self.todayy[2]))
        self.cal.pack(pady = 20)
    
    def grad_date(self):
        self.date.config(text = "Selected Date is: " + self.cal.get_date())
    
#Execute Tkinter
root =Tk()
you = CALENDAR(root)
root.mainloop()