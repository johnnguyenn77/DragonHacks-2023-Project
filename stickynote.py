import tkinter
from make_draggable import make_draggable

# Create an instance of tkinter frame
class Sticky_Note:
    def __init__(self,root):
        self.frame = tkinter.Frame(root, bd = 4, bg = 'white')
        self.frame.place(x=10, y=20)
        make_draggable(self.frame)
        notes = tkinter.Text(self.frame)
        notes.pack()

root = tkinter.Tk()
todolist = Sticky_Note(root)
root.mainloop()