'''
Author : Nafees Ur Rehman
'''
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from PIL    import Image,ImageTk

def clickDownload():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR", "ENTER url ")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR", "ENTER LOCATION ")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Downloading Finish", yt.title+" has been downloaded Sucessfully!!!")

def setURL():
    #Get URL of the Video
    url = getURL.get()
    print(url)

    #Create Object to hold the URL
    global yt
    yt = YouTube(url)
    print(yt.title)

    # Get the Quality of the Videos and store in the 'videos' variable
    global videos
    videos = yt.streams.filter(mime_type='video/mp4')
    
    #Get Quality and display as list in the Listbox
    count = 1
    for v in videos:
        listbox.insert(END, str(count)+". "+str(v)+"\n\n")
        count += 1


def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def clickReset():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0,END)

#defining new function for about_us Windows
def open_win():
   new= Toplevel(root)#inheriting properties from "root object"
   new.geometry("550x280")
   new.resizable(True, True)
   new.title("About Us")
   photo = PhotoImage(file = 'favicon.png')
   new.iconphoto(False, photo)
   #end of function open_win
   #creating new statements in aboutus windows
   Aboutus = Label(new,   text="Video Downloader:", font=("Century Gothic",21)).grid(row=0, column=0, padx=10,  pady=10)    
   #video DOwnloader Photo 
   # Read the Image
   image = Image.open("favicon.png")
 
    # Resize the image using resize() method
   resize_image = image.resize((400, 400), Image.ANTIALIAS)
 
   img = ImageTk.PhotoImage(resize_image)
 
    # create label and add resize image
   label1 = Label(new,image=img)
   label1.image = img
   label1.grid(row=1, column=0, padx=10, pady=10)
   #photo ends here
   
   #info of about us
   info = Label(new, text="A simple application to download YouTube videos using Python. \nTkinter API is used for GUI And with love from Google to use the Youtube API.\nPytube is a new API used for downloading Youtube videos for free of cost.", font=("Century Gothic",11)).grid(row=2, column=0, padx=10,  pady=10)
   Developed= Label(new, text="Developed By:", font=("Century Gothic",15)).grid(row=3, column=0, padx=0,  pady=0)
   Developers= Label(new, text="Nafees Ur Rehman\nLead Programmer\n", font=("Century Gothic",11)).grid(row=4, column=0, padx=0,  pady=0)
   #info

#Create Root Object
root = Tk()

#Set Title
root.title("SSIT Video Downloader")

#Set size of window
root.geometry("1080x840")

#Make the Window not Resizeable
root.resizable(True, True)

#Set Title photo
photo = PhotoImage(file = 'favicon.png')

#Make the windows not Resizeable
root.iconphoto(False, photo)
image = Image.open("ssit.png")
 
    # Resize the image using resize() method
resize_image = image.resize((100, 100), Image.ANTIALIAS)
 
img = ImageTk.PhotoImage(resize_image)
 
    # create label and add resize image
label1 = Label(root,image=img)
label1.image = img
label1.grid(row=0, column=0, padx=10, pady=10)
#Set Labels
headLabel       = Label(root,   text="SSIT VIDEO DOWNLOADER",  font=("Century Gothic",25)).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(root,   text="SELECT QUALITY",      font=("Century Gothic",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)
developer1      = Label(root,   text="Developed by Nafees Ur Rehman @SSIT college project.", font=("Century Gothic",10)).grid(row=5, column=1, padx=10,  pady=10)
License         = Label(root,   text="MIT License(c) 2018.", font=("Century Gothic",10)).grid(row=6, column=1, padx=10,  pady=10)


#Get Input
getURL = StringVar()
getLoc = StringVar()

#Set Entry
urlEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

#List box for video Quality
listbox     = Listbox(root, font=("Century Gothic",11), width = 60, height = 11, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2,column=1, padx=10, pady=10)

#Set Buttons
urlButton       = Button(root, text = "SET URL",    font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(root, text = "BROWSE",     font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(root, text = "DOWNLOAD",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickDownload).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(root, text = "CLEAR ALL",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=4, column=2, padx=10, pady=10)
aboutUs         = Button(root, text = "About Us",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=open_win).grid(row=7, column=1, padx=10, pady=10)

#Set an infinite loop so window stays in view
root.mainloop()
