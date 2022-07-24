from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import webbrowser

win = Tk()
win.geometry('600x400')
win.title('YouTube Downloader')
win.config(bg = '#072434')


link = StringVar()
og_path = StringVar()
title_var = StringVar()
thumb_var = StringVar()
lengh_var = StringVar()
views_var = StringVar()
qu_var = StringVar()



#Functions
def Clear():
    link.set('')
    og_path.set('')
    title_var.set('')
    thumb_var.set('')
    lengh_var.set('')
    views_var.set('')



def Save_As():
    path = filedialog.askdirectory()
    og_path.set(path)


def Download():
    temp_link = link.get()
    yt = YouTube(temp_link)


    temp_q  = qu_var.get()


    if temp_q == '360p mp4':
        stream = yt.streams.get_by_itag(18)
        stream.download(og_path.get())

    if temp_q == '720p mp4':
        stream = yt.streams.get_by_itag(22)
        stream.download(og_path.get())

    if temp_q == '1080p mp4':
        stream = yt.streams.get_by_itag(137)
        stream.download(og_path.get())

    if temp_q == '128kbps mp4':
        stream = yt.streams.get_by_itag(140)
        stream.download(og_path.get())

    if temp_q == '50kbps webm':
        stream = yt.streams.get_by_itag(249)
        stream.download()



def Search():
    temp_link = link.get()
    yt = YouTube(temp_link)
    
    title_var.set(yt.title)
    thumb_var.set(yt.thumbnail_url)
    lengh_var.set(yt.length)
    views_var.set(yt.views)



def callback():
   webbrowser.open_new_tab(thumb_var.get())


in_link = ttk.Entry(textvariable = link, width = 50)
in_link.place(x = 140, y = 50)

com_qu = ttk.Combobox(textvariable = qu_var, values =  ['360p mp4', '720p mp4', '1080p mp4', '128kbps mp4', '50kbps webm'])
com_qu.set('720p mp4')
com_qu.pack()




#Lables
lb_link = Label(text = 'YouTube Link:', fg ='white', bg ='#072434')
lb_link.place(x = 50, y = 50)


lb_title = Label(text = 'Video Title:', fg = 'white', bg = '#072434', font = ('', 10))
lb_title.place(x = 60, y = 120)

lb_title_main = Label(textvariable = title_var, fg = 'white', bg = '#072434', font = ('', 10))
lb_title_main.place(x = 220, y = 120)


lb_thumbnail = Label(text = 'Video Thumbnail link:', fg = 'white', bg = '#072434', font = ('', 10))
lb_thumbnail.place(x = 60, y = 160)

lb_thumbnail_main = Label(textvariable = thumb_var, fg = 'blue', bg = '#072434', font = ('', 10), cursor="hand2")
lb_thumbnail_main.place(x = 220, y = 160)
lb_thumbnail_main.bind("<Button-1>", lambda e:callback())


lb_length = Label(text = 'Video Length:', fg = 'white', bg = '#072434', font = ('', 10))
lb_length.place(x = 60, y = 200)

lb_length_main = Label(textvariable = lengh_var, fg = 'white', bg = '#072434', font = ('', 10))
lb_length_main.place(x = 220, y = 200)


lb_views = Label(text = 'Video Views:', fg = 'white', bg = '#072434', font = ('', 10))
lb_views.place(x = 60, y = 240)

lb_views_main = Label(textvariable = views_var, fg = 'white', bg = '#072434', font = ('', 10))
lb_views_main.place(x = 220, y = 240)



#Buttons
bt_seacrh = ttk.Button(text = 'Search', command = Search)
bt_seacrh.place(x = 450, y = 49)

bt_save_as = ttk.Button(text = 'Save as...', command = Save_As)
bt_save_as.place(x = 190, y = 300)

bt_setdir = ttk.Button(text = 'Start!', command = Download)
bt_setdir.place(x = 280, y = 300)

bt_clear= ttk.Button(text = 'Clear All', command = Clear)
bt_clear.place(x = 370, y = 300)

win.mainloop()