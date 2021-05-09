from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(True,True)
root.title("DataFlair-youtube video downloader")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

savePath = "D:/"


##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
    try: 
        yt =YouTube(str(link))
    except VideoUnavailable:
        Label(root, text = 'Connection error', font = 'arial 15').place(x= 180 , y = 210)
    mp4files = yt.streams.filter(adaptive=True,file_extension='mp4').order_by('resolution').desc()  
    mp4files.first().download(savePath)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)



root.mainloop()
