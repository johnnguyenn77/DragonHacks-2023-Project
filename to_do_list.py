import tkinter
import tkinter.messagebox
import pickle
from make_draggable import make_draggable

class To_Do_List:

    def __init__(self,root):
        self.frame = tkinter.Frame(root, bd = 4, bg ='black')
        make_draggable(self.frame)
        
        #Where GUI starts
        frame_tasks = tkinter.Frame(self.frame)

        frame_tasks.pack()

        self.listbox_tasks = tkinter.Listbox(frame_tasks,height=10,width=50)
        self.listbox_tasks.pack(side=tkinter.LEFT)


        scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
        scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)

        self.listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.entry_task = tkinter.Entry(self.frame, width=50)
        self.entry_task.pack()

        button_add_task = tkinter.Button(self.frame, text="Add task", width=48, command=self.add_task)
        button_add_task.pack(side = tkinter.LEFT)

        button_delete_task = tkinter.Button(self.frame, text="Delete task", width=48, command=self.delete_task)
        button_delete_task.pack(side = tkinter.RIGHT)

        # button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
        # button_load_tasks.pack()

        # button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
        # button_save_tasks.pack()

        self.load_tasks()
        self.frame.pack()

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

# frame_tasks = tkinter.Frame(frame)
# frame_tasks.pack()

# listbox_tasks = tkinter.Listbox(frame_tasks,height=10,width=50)
# listbox_tasks.pack(side=tkinter.LEFT)


# scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
# scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)

# listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
# scrollbar_tasks.config(command=listbox_tasks.yview)

# entry_task = tkinter.Entry(root, width=50)
# entry_task.pack()

# button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
# button_add_task.pack(side = 'left')

# button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
# button_delete_task.pack(side = 'right')

# # button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
# # button_load_tasks.pack()

# # button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
# # button_save_tasks.pack()

# load_tasks()

#checkbutton = tkinter.Checkbutton(root,text ="Call friend").pack()

root = tkinter.Tk()
todolist = To_Do_List(root)
root.mainloop()