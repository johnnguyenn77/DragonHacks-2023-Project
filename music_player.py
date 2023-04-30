from tkinter import *
import os
from pygame import *

root = Tk()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
height = 500
width = 600
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//4)-(height//4)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
# root.geometry("600x500")

# Navigating through windows
window = Frame(root)
window2 = Frame(root)


for frame in (window, window2):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(window)

# ===========================================================
# ============== HOME ===================================
# ===========================================================

window.config(background='#7852E6')


image_image_4 = PhotoImage(
    file="images/image_4.png")
image_4 = Label(
    window,
    bg='#7852E6',
    image=image_image_4
)
image_4.place(
    x=41,
    y=41
)


image_image_1 = PhotoImage(
    file="images/image_1.png")
image_1 = Label(
    window,
    bg='#7852E6',
    image=image_image_1
)
image_1.place(
    x=196,
    y=121
)


image_image_2 = PhotoImage(
    file="images/image_2.png")
image_2 = Label(
    window,
    bg='#7852E6',
    image=image_image_2
)
image_2.place(
    x=60,
    y=340
)


button_image_2 = PhotoImage(
    file="images/button_2.png")
button_2 = Button(
    window,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play(),
    relief="flat",
    activebackground='#7852E6'
)
button_2.place(
    x=243,
    y=386.0,
    width=80.0,
    height=81.0
)

button_image_3 = PhotoImage(
    file="images/button_3.png")
button_3 = Button(
    window,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: next_song(),
    relief="flat",
    activebackground='#7852E6'
)
button_3.place(
    x=355,
    y=397.0,
    width=74.0,
    height=56.0
)

button_image_4 = PhotoImage(
    file="images/button_4.png")
button_4 = Button(
    window,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: previous_song(),
    relief="flat",
    activebackground='#7852E6'
)
button_4.place(
    x=137,
    y=398.0,
    width=74.0,
    height=56.0
)

image_image_3 = PhotoImage(
    file="images/image_3.png")
image_3 = Label(
    window,
    bg='#000000',
    image=image_image_3
)
image_3.place(
    x=203,
    y=131
)


button_image_5 = PhotoImage(
    file="images/button_5.png")
button_5 = Button(
    window,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(window2),
    relief="flat",
    activebackground='#7852E6'
)
button_5.place(
    x=49,
    y=378.0,
    width=76.0,
    height=32.0
)

playing_song = Label(
    window,
    text="",
    bg='#7852E6',
    fg='#ffffff',
    font=('yu gothic ui', 8, 'bold')

)
playing_song.place(
    x=150,
    y=360,
    height=20,
    width=300
)

# ===========================================================
# ============== PLAYLIST ===================================
# ===========================================================
window2.config(background='#7852E6')

button_image_6 = PhotoImage(
    file="images/button_2.png")
button_6 = Button(
    window2,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: call_play(),
    relief="flat",
    activebackground='#7852E6'
)
button_6.place(
    x=100.0,
    y=2.0,
    width=80.0,
    height=80.0
)

def call_play():
    show_frame(window)
    play()

button_7 = Button(
    window2,
    text="""BACK""",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(window),
    relief="flat",
    activebackground='#000000',
    bg='#000000',
    fg='#ffffff',
)
button_7.place(
    x=26.0,
    y=25.0,
    width=54.0,
    height=33.0
)

listbox = Listbox(
    window2,
    selectmode=SINGLE,
    #bg='#000000',
    bg='#000000',
    fg='#ffffff',
    font=('yu gothic ui', 10, 'bold'),
    bd=25,
    relief='flat'
)
listbox.place(
    x=30,
    y=80,
    height=406,
    width=520
)

scroll = Scrollbar(
    window2
)
scroll.place(
    x=550,
    y=80,
    height=406
)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

os.chdir(r'C:\Users\User\Desktop\MusicPlayer\build\songs')
songs = os.listdir()


button_image_1 = PhotoImage(
    file="C:\\MusicPlayer\\build\\images\\button_1.png")


def play():
    current_song = listbox.get(ACTIVE)
    playing_song['text'] = current_song
    mixer.music.load(current_song)
    mixer.music.play()

    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: pause_song(),
        relief="flat",
        activebackground='#7852E6'
    )
    button_1.place(
        x=241,
        y=385.0,
        width=80.0,
        height=81.0
    )


resume_pic = PhotoImage(
    file="C:\\MusicPlayer\\build\\images\\button_2.png")


def pause_song():
    mixer.music.pause()

    resume_button = Button(
        window,
        image=resume_pic,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: resume_song(),
        relief="flat",
        activebackground='#7852E6'
    )
    resume_button.place(
        x=243,
        y=386.0,
        width=80.0,
        height=81.0
    )


def resume_song():
    mixer.music.unpause()
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: pause_song(),
        relief="flat",
        activebackground='#7852E6'
    )
    button_1.place(
        x=241,
        y=385.0,
        width=80.0,
        height=81.0
    )


def next_song():
    playing = playing_song['text']
    index = songs.index(playing)
    next_index = index + 1
    playing = songs[next_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)
    song_list()
    listbox.select_set(next_index)
    playing_song['text'] = playing


def previous_song():
    playing = playing_song['text']
    index = songs.index(playing)
    next_index = index - 1
    playing = songs[next_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)
    song_list()
    listbox.select_set(next_index)
    playing_song['text'] = playing


def song_list():
    for i in songs:
        listbox.insert(END, i)


song_list()

mixer.init()
songs_state = StringVar()
# songs_state.set("choosing")

root.resizable(False, False)
root.mainloop()