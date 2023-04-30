import tkinter
from make_draggable import make_draggable

#Create an instance of tkinter frame
class Sticky_Note:
    def __init__(self,root):
        self.frame = tkinter.Frame(root, bg = '#cedfef', highlightbackground='white', highlightcolor= "white",highlightthickness=1)
        self.frame.place(x=300, y=20)
        make_draggable(self.frame)
        notes = tkinter.Text(self.frame,bg = "#222222",fg = "white")
    
        close_btn = tkinter.Button(self.frame, width = 3, bd =0, text = 'X', command = self.frame.place_forget, bg = '#cedfef', font = ("Segoe UI Variable Display", 10))
        close_btn.pack(anchor = "ne")
    #     add_btn = tkinter.Button(self.frame, width = 3, text = '+', command = self.add, bg = '#cedfef', font = ("Segoe UI Variable Display", 10))
    #     add_btn.place(x=1.0,y=0.3)
        notes.pack()
    # def add(self):
    #     #parent = Sticky_Note.nametowidget(Sticky_Note.winfo_parent())
    #     stickynotecopy = Sticky_Note(self.root)




root = tkinter.Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
todolist = Sticky_Note(root)
root.mainloop()