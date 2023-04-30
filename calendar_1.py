# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from make_draggable import make_draggable

# Add Calendar
class CALENDAR:
    def __init__(self,root):
        self.frame = Frame(root, bd = 4, bg='black')
        make_draggable(self.frame)
        self.frame.place(x=300, y=20)
        self.today=date.today()
        self.todayy=str(self.today)
        self.todayyy = self.todayy.split("-")
        self.cal = Calendar(self.frame, selectmode = 'day', year = int(self.todayyy[0]), month = int(self.todayyy[1]), day = int(self.todayyy[2]))
        self.cal.pack(pady = 20)
    
    #def grad_date(self):
     #   self.date.config(text = "Selected Date is: " + self.cal.get_date())
 
# Execute Tkinter
root = Tk()
call = CALENDAR(root)
root.mainloop()