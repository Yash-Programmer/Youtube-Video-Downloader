from tkinter import *
from tkinter import filedialog, ttk, messagebox
from pytube import *
from PIL import ImageTk
from PIL import Image
import pafy
import wget
import sys
import os
import playsound

sys.argv

def Info():
    Window = Toplevel()
    url = URL_Entry.get()
    if url.strip() == '':
        Label(Window, text='None', font=['Arial', 20]).pack()
    elif 'you' not in url.strip():
        Label(Window, text='None', font=['Arial', 20]).pack()
    else:
        thumbnail = pafy.new(url)
        thumbnail = thumbnail.thumb
        wget.download(thumbnail)

        img = ImageTk.PhotoImage(Image.open('default.jpg'))
        Label(Window, image=img).grid()
        os.remove('default.jpg')

        Label(Window, text=f'Title:     {pafy.new(url).title}', font=15).grid(row=1, column=0)
        Label(Window, text=f'Views:     {pafy.new(url).viewcount}', font=15).grid(row=2, column=0)
        Label(Window, text=f'Likes:     {pafy.new(url).likes}', font=15).grid(row=3, column=0)
        Label(Window, text=f'Dislikes:  {pafy.new(url).dislikes}', font=15).grid(row=4, column=0)
        Label(Window, text=f'Duration:  {pafy.new(url).duration}', font=15).grid(row=5, column=0)
        Label(Window, text=f'Category:  {pafy.new(url).category}', font=15).grid(row=6, column=0)

    Window.mainloop()

def EmptyLabel(a, loc):
    b = Label(loc, text=' ', font=a)
    b.pack()
    pass

def choosePath():
    global Folder_Path
    Folder_Path = filedialog.askdirectory()
    return Folder_Path


def check():
    global Folder_Path
    url = URL_Entry.get()
    if url.strip() == '':
        print('No Url is selected')
        messagebox.showerror('YouTube Video Downloader', 'No Url Found.\nPlease Fill The Space')
    elif Folder_Path == '':
        print('No Path Selected')
        messagebox.showerror('YouTube Video Downloader', 'No Path Selected')


def DownloadVideo():
    Downloading_Label_Text['text'] = ''
    #check()
    #playsound.playsound(r'C:\Users\Lenovo\PycharmProjects\YouTube Video Downloader\Files\Downloading.mp3')
    url = URL_Entry.get()
    choice = quality_choices.get()
    if choice == choices[0]:
        pafy.new(url).getbest().download(Folder_Path)
        #Downloading_Label_Text['text'] = 'Downloaded Successfully'
        #playsound.playsound(r'YouTube Video Downloader\Files\Downloaded Successfully.mp3')
    elif choice == choices[1]:
        YouTube(url).streams.first().download(Folder_Path)
        Downloading_Label_Text['text'] = 'Downloaded Successfully'
        #playsound.playsound(r'C:\Users\Lenovo\PycharmProjects\YouTube Video Downloader\Files\Downloaded Successfully.mp3')
    elif choice == choices[2]:
        YouTube(url).streams.filter(only_audio=True).first().download(Folder_Path)
        Downloading_Label_Text['text'] = 'Downloaded Successfully'
        #playsound.playsound(r'C:\Users\Lenovo\PycharmProjects\YouTube Video Downloader\Files\Downloaded Successfully.mp3')
    elif choice == choices[3]:
        YouTube(url).streams.filter(only_video=True).first().download(Folder_Path)
        Downloading_Label_Text['text'] = 'Downloaded Successfully'
        #playsound.playsound(r'C:\Users\Lenovo\PycharmProjects\YouTube Video Downloader\Files\Downloaded Successfully.mp3')

def Show_Path(a):
    if Folder_Path == '':
        print('\n\nNone Path is Selected!')
    else:
        PathLabel.config(text=a)

root = Tk()
root.resizable(width=False, height=False)
root.title("Youtube Video Downloader__By Yash")
root.geometry('477x700')
#root.iconbitmap(r'C:\Users\Lenovo\PycharmProjects\YouTube Video Downloader\Files\Logo.ico')  # Files/Logo.ico

Frame1 = LabelFrame(root, text='URL')
Frame1.pack()

URL_Label = Label(Frame1, text="Enter the URL of the Video", font=('Times New Roman', 30))
URL_Label.pack()

URL_Entry = Entry(Frame1, width=45, borderwidth=5, font=['Calibri', 13])
URL_Entry.pack(ipady=3)

Video_Details_Button = Button(Frame1, text='Video Details', bg="light green", height=1, width=10, command=Info)
Video_Details_Button.pack()

EmptyLabel(1, Frame1)

Frame2 = LabelFrame(root, text='Path', padx=120)
Frame2.pack()

Choose_Path_Label = Label(Frame2, text="Choose Path", font=('Times New Roman', 30))
Choose_Path_Label.pack()

Choose_Path_Button = Button(Frame2, text='Enter Path', bg="light green", height=1, width=10,
                            command=lambda: [choosePath(), Show_Path(Folder_Path)])
Choose_Path_Button.pack()

PathLabel = Label(Frame2, text='')
PathLabel.pack()

EmptyLabel(1, Frame2)

Frame3 = LabelFrame(root, text='File Type', padx=61)
Frame3.pack()

Video_File_Type = Label(Frame3, text="Select File Type", font=('Times New Roman', 30))
Video_File_Type.pack()

choices = ["Video + Audio (High Quality)", "Video + Audio (Low Quality)", "Only Audio", "Only Video"]
quality_choices = ttk.Combobox(Frame3, values=choices, width=50)
quality_choices.pack()

EmptyLabel(1, Frame3)

Download_Button = Button(root, text="Download", width=10, height=2, bg="light green", command=DownloadVideo)
Download_Button.pack()

Downloading_Label_Text = Label(root, text='', font=['Roboto', 15])
Downloading_Label_Text.pack()

By_Label = Label(root, text='By Yash Varshney', font=['Times New Roman', 20])
By_Label.pack()

#My_Image = ImageTk.PhotoImage(Image.open(r'C:\Users\Lenovo\PycharmProjects\YouTube Video Downloader\Files\Pic.png'))  # Files/Pic.png
#My_Image_Label = Label(image=My_Image)
#My_Image_Label.pack()

root.mainloop()