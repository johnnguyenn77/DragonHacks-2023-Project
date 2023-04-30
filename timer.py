import time
from tkinter import *
from tkinter import messagebox
from make_draggable import make_draggable
 
class Timer:
    def __init__(self, root):
        def submit():
            try:
                # the input provided by the user is
                # stored in here :temp
                temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
            except:
                print("Please input the right value")
            while temp >-1:
         
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                mins,secs = divmod(temp,60)
  
                # Converting the input entered in mins or secs to hours,
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
                hours=0
                if mins >60:
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                    hours, mins = divmod(mins, 60)
         
                # using format () method to store the value up to
                # two decimal places
                hour.set("{0:02d}".format(hours))
                minute.set("{0:02d}".format(mins))
                second.set("{0:02d}".format(secs))
  
                # updating the GUI window after decrementing the
                # temp value every time
                root.update()
                time.sleep(1)
  
                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0):
                    messagebox.showinfo("Time Countdown", "Time's up ")
         
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1
 
        # Declaration of variables
        self.frame = Frame(root, highlightbackground='white', highlightcolor= "white",highlightthickness=1, bg='#a7bfd5')
        self.frame.place(x=300, y=20)
        make_draggable(self.frame)
        
        top_frame = Frame(self.frame, bd = 0, bg = '#a7bfd5',width = 300)
        
        name = Label(self.frame, text = 'Timer', font = ("Segoe UI Variable Display", 18), bg = '#a7bfd5')

        
        close_btn = Button(self.frame, bd = 0, width = 3, text = 'X', command = self.frame.place_forget, bg = '#cedfef', font = ("Segoe UI Variable Display", 12))
        name.pack(anchor = 'nw')
        
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
  
        # setting the default value as 0
        hour.set("00")
        minute.set("00")
        second.set("00")
        button_frame = Frame(self.frame, bd = 4, bg='#cedfef')

        # Use of Entry class to take input from the user
        hourEntry= Entry(button_frame, width=3, bd = 0, justify='center', font = ("Segoe UI Variable Display", 23), textvariable=hour, bg = '#cedfef').pack(side = LEFT)
  
        minuteEntry= Entry(button_frame, width=3, bd = 0, justify='center', font = ("Segoe UI Variable Display", 23),textvariable=minute, bg = '#cedfef').pack(side = LEFT)
  
        secondEntry= Entry(button_frame, width=3, bd = 0, justify= CENTER, font = ("Segoe UI Variable Display", 23), textvariable=second, bg = '#cedfef').pack(side = LEFT)

        button_frame.pack()

        # button widget
        btn = Button(self.frame, bd = 0, text='Set Time Countdown', command= submit, font= ("Segoe UI Variable Display", 12), bg = '#cedfef').pack()
        close_btn.place(x= 133, y = 0)
        # infinite loop which is required to
        # run tkinter program infinitely
        # until an interrupt occurs


# creating Tk window
root = Tk()
root.geometry("1280x720")
root.title("Time Counter")
root.configure(bg='#222222')
timer = Timer(root)

root.mainloop()