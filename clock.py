from tkinter import *
import datetime
from datetime import datetime
import geocoder
from make_draggable import make_draggable

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root, highlightbackground='white', highlightcolor= "white",highlightthickness=1, bg = '#222222', width = 100)
        make_draggable(self.frame)
        self.frame.place(x = 300, y =  30)
        
        g = geocoder.ip('me')
        result = g.address
        result = result.split(', ')
        title = Label(self.frame, fg = '#66fbfb',bg = '#222222', text = 'Clock', font = ("Segoe UI Variable Display",10)).pack(anchor = 'nw', pady =4)
        close_btn = Button(self.frame, fg = '#66fbfb', bd=0, width = 3, text = 'X', command = self.frame.place_forget, bg = '#222222', font = ("Segoe UI Variable Display", 10))
        close_btn.place(x = 208, y= 0)
        location = Label(self.frame, bg = '#222222', fg ='white',text = result[0]+', '+result[1], font = ("Segoe UI Variable Display",15))
        #display the time
        self.digital_time_lb = Label(self.frame,font=("Segoe UI Variable Display",30), fg = 'white', bg = '#222222')

        #display the day/month/Year
        self.digital_DAY_lb = Label(self.frame,font=("Segoe UI Variable Display",15), fg = 'white', bg = '#222222')
        self.digital_DAY_lb.pack()
        self.digital_time_lb.pack()
        location.pack()
        self.timezone_list=StringVar()
        self.my_digital_clock()
        
#current_time = datetime.now(pytz.timezone('Africa/Djibouti')) # get the current time
    def my_digital_clock(self):
        #current_time = datetime.now(pytz.timezone(self.timezone_list.get())) # get the current time from the drop_down list
        current_time = datetime.now()
        time_display=current_time.strftime('%H:%M:%S')
        self.digital_time_lb.config(text=time_display)#updates the label to the current time
        day_display=datetime.now()
        day_display=current_time.strftime('%B %d, %Y')
        self.digital_DAY_lb.config(text = day_display)
    #print(timezone_list.set(str(pytz.common_timezones[0])))
    #used strftime() to format the display of the current time
    #%H->hours
    #%M->minutes
    #%s->seconds
    #%B->month name
    #%Y->year
    #%d->day
    #change the time after a specific millisecond
        self.root.after(80, self.my_digital_clock)
    


#root = Tk()
#root.title("Digital Clock")
#root.geometry("310x200")

#clock_widget = DigitalClock(root)#function call
#root.mainloop()