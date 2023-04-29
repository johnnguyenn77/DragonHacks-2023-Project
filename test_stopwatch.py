import tkinter as tk
import time


class Timer:
    def __init__(self, root):
        self.root = root
        self.sv = tk.StringVar()
        self.start_time = None
        self.is_running = False

        self.frame = tk.Frame(self.root, bd = 4, bg = "white")
        self.frame.place(x=10, y=20)
        tk.Label(self.frame, textvariable=self.sv, font='ariel 15').pack()

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack()
        tk.Button(btn_frame, text='Start', command= self.start).pack(side=tk.LEFT)
        tk.Button(btn_frame, text='Stop', command= self.stop).pack(side=tk.RIGHT)
        tk.Button(btn_frame, text='Reset').pack(side=tk.RIGHT)
        self.frame.bind('<Return>', self.startstop)
        #self.root.mainloop()

    def make_widgets(self):
        self.frame = tk.Frame(self.root, bd = 4, bg = "white")
        self.frame.place(x=10, y=20)
        tk.Label(self.frame, textvariable=self.sv, font='ariel 15').pack()

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack()
        tk.Button(btn_frame, text='Start', command= self.start).pack(side=tk.LEFT)
        tk.Button(btn_frame, text='Stop', command= self.stop).pack(side=tk.RIGHT)
        tk.Button(btn_frame, text='Reset').pack(side=tk.RIGHT)

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.timer()
            self.is_running = True

    def timer(self):
        self.sv.set(self.format_time(time.time() - self.start_time))
        self.after_loop = self.root.after(50, self.timer())

    def stop(self):
        if self.is_running:
            self.root.after_cancel(self.after_loop)
            self.is_running = False

    def startstop(self, event=None):
        if self.is_running:
            self.stop()
        else:
            self.start()

    @staticmethod
    def format_time(elap = 0):
        hours = int(elap / 3600)
        minutes = int(elap / 60 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes * 60.0)
        hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds) * 1000)
        return '%02d:%02d:%02d:%03d' % (hours, minutes, seconds, hseconds)


root = tk.Tk()
timer = Timer(root)

root.mainloop()
