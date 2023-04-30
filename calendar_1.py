# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from make_draggable import make_draggable

# Add Calendar
class CALENDAR:
    def __init__(self,root):
        self.frame = Frame(root, highlightbackground='white', highlightcolor= "white",highlightthickness=1, bg='#222222')
        make_draggable(self.frame)
        self.frame.place(x=300, y=20)
        title = Label(self.frame, fg = '#66fbfb',bg = '#222222', text = 'Calendar', font = ("Segoe UI Variable Display",10)).pack(anchor = 'nw', pady = 4)
        close_btn = Button(self.frame, fg = '#66fbfb', bd=0, width = 3, text = 'x', command = self.frame.place_forget, bg = '#222222', font = ("Segoe UI Variable Display", 12))
        close_btn.place(x = 218, y= 0)
        self.today=date.today()
        self.todayy=str(self.today)
        self.todayyy = self.todayy.split("-")
        self.cal = Calendar(self.frame, selectmode = 'day', year = int(self.todayyy[0]), month = int(self.todayyy[1]), day = int(self.todayyy[2]))
        self.cal.pack()
    
    #def grad_date(self):
     #   self.date.config(text = "Selected Date is: " + self.cal.get_date())
 
# Execute Tkinter
#root = Tk()
#root.configure(bg='#222222')
#root.geometry('1280x720')
#timer = Stopwatch(root)
#call = CALENDAR(root)
#root.mainloop()