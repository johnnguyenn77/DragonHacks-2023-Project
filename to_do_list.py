import tkinter
import tkinter.messagebox
import pickle
from make_draggable import make_draggable
class To_Do_List:

    def __init__(self,root):
        self.frame = tkinter.Frame(root, highlightbackground='white', highlightcolor= "white",highlightthickness=1, bg ='#222222')
        make_draggable(self.frame)
        
        #Where GUI starts
        name = tkinter.Label(self.frame, text = 'To-do List', fg = '#66fbfb', font = ("Segoe UI Variable Display", 12), bg = '#222222')
        close_btn = tkinter.Button(self.frame, fg = '#66fbfb', bd = 0, width = 3, text = 'x', command = self.frame.place_forget, bg = '#222222', font = ("Segoe UI Variable Display", 12))
        name.pack(anchor = 'nw', pady=4)
        close_btn.place(x= 325, y = 0)
        frame_tasks = tkinter.Frame(self.frame, bg = '#222222')

        frame_tasks.pack()

        self.listbox_tasks = tkinter.Listbox(frame_tasks,height=10,width=47, bg = '#222222', bd = 0, fg = 'white', font = ("Segoe UI Variable Display", 10))
        self.listbox_tasks.pack(side=tkinter.LEFT, padx = 5)


        scrollbar_tasks = tkinter.Scrollbar(frame_tasks, bg = '#222222', bd = 0)
        scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)

        self.listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.entry_task = tkinter.Entry(self.frame, width=55, bg = '#222222', fg = 'white',highlightbackground='white', highlightcolor= "white",highlightthickness=1, bd = 0, insertbackground='white')
        self.entry_task.pack(pady = 3)

        button_add_task = tkinter.Button(self.frame,fg = 'white',bd = 0, text="Add task", width=10, command=self.add_task, bg = '#222222', font = ("Segoe UI Variable Display", 10))
        button_add_task.pack(side = tkinter.LEFT)

        button_delete_task = tkinter.Button(self.frame, fg = 'white', bd = 0,text="Delete task", width=10, command=self.delete_task, bg = '#222222', font = ("Segoe UI Variable Display", 10))
        button_delete_task.pack(side = tkinter.RIGHT)
        
        self.load_tasks()
        self.frame.place(x=300,y=20)

    def add_task(self):
        task= self.entry_task.get()
        if task != "":
            #checkbutton = tkinter.Checkbutton(listbox_tasks,task)

            self.listbox_tasks.insert(0,task)
            self.entry_task.delete(0,tkinter.END)
            tasks = self.listbox_tasks.get(0, self.listbox_tasks.size())
            #print(tasks)

            pickle.dump(tasks,open("tasks.dat","wb"))
        else:
            tkinter.messagebox.showwarning(title="Warning",message="You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(task_index)
            tasks = self.listbox_tasks.get(0, self.listbox_tasks.size())
            #print(tasks)

            pickle.dump(tasks,open("tasks.dat","wb"))
        except:
            tkinter.messagebox.showwarning(title="Warning",message="You must select a task.")

    def load_tasks(self):
        try:
            tasks = pickle.load(open("tasks.dat","rb"))
            self.listbox_tasks.delete(0,tkinter.END)
            for task in tasks:
                self.listbox_tasks.insert(tkinter.END,task)
        except:
            tkinter.messagebox.showwarning(title="Warning",message="Cannot find task.")

    # def save_tasks():
    #     tasks = listbox_tasks.get(0, listbox_tasks.size())
    #     #print(tasks)

    #     pickle.dump(tasks,open("tasks.dat","wb"))





#Create GUI

#root = tkinter.Tk()
#root.title("Time Counter")
#root.geometry("1280x720")
#root.configure(bg='#222222')
#todolist = To_Do_List(root)
#root.mainloop()