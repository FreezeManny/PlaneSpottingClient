from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import glob
import webbrowser

import time


def BrowseAction():
    #get the working directorie (Output: Working directory as String)
    global CurrentDirectory
    CurrentDirectory = filedialog.askdirectory()
    #process for Name
    LocalVar = CurrentDirectory
    LocalVar = LocalVar.split("/")
    LocalVar = LocalVar[::-1]
    folderLocation_lbl.config(text=LocalVar[0])
    
    FolderInDirectory = glob.glob(CurrentDirectory + "/*")
    #get Aircraft types in List (Output: AircraftTypes as List with Types in List)
    AircraftTypes = []
    for item in FolderInDirectory:
        LocalDirectory = item
        LocalDirectory = LocalDirectory.split('\\')
        AircraftTypes.append(LocalDirectory[-1])
    #Clear listbox and add new to the List
    type_listbox.delete(0,'end')
    reg_listbox.delete(0,'end')
    for item in AircraftTypes:
        type_listbox.insert("end", item)
        
def SearchAction(Type):
    #get Selected Aircraft Type
    AircraftTypeSelected = type_listbox.selection_get()
    #get All Directorys from Aircraft Type (Output: Registration of Aircraft in List)
    RegistrationDirectory = glob.glob(CurrentDirectory + "/" + AircraftTypeSelected + "/*")
    #get Registration List (Output: Registrations as List with Types in List)
    global Registrations
    Registrations = []
    for item in RegistrationDirectory:
        LocalDirectory = item
        LocalDirectory = LocalDirectory.split('\\')
        Registrations.append(LocalDirectory[-1])
    #Clear Registration listbox and add new to the List
    reg_listbox.delete(0,'end')
    for item in Registrations:
        reg_listbox.insert("end", item)
    
def openOnFlightradar24():
    for items in Registrations:
        webbrowser.open("https://www.flightradar24.com/data/aircraft/" + items.lower())
        time.sleep(0.3)
        
def openSingleOnFlightradar24(item):
    RegistrationSelected = type_listbox.selection_get()
    webbrowser.open("https://www.flightradar24.com/data/aircraft/" + RegistrationSelected.lower())
        
        
root = Tk()
root.title("Opener")
root.geometry("1000x400")
root.minsize(120, 1)
root.maxsize(1924, 2141)
root.resizable(1,  1)
root.title("")
root.configure(bg="#4d4d4d")

Heading = Label(root)
Heading.place(relx=0.196, rely=0.022, height=25, width=304)
Heading.configure(activebackground="#f9f9f9")
Heading.configure(activeforeground="#004080")
Heading.configure(background="#d9d9d9")
Heading.configure(borderwidth="4")
Heading.configure(disabledforeground="#a3a3a3")
Heading.configure(foreground="#000000")
Heading.configure(highlightbackground="#d9d9d9")
Heading.configure(highlightcolor="black")
Heading.configure(text='''Planespotting Helper''')

browse_btn = Button(root, command=BrowseAction)
browse_btn.place(relx=0.685, rely=0.249, height=25, width=85)
browse_btn.configure(activebackground="#ececec")
browse_btn.configure(activeforeground="#000000")
browse_btn.configure(background="#d9d9d9")
browse_btn.configure(disabledforeground="#a3a3a3")
browse_btn.configure(foreground="#000000")
browse_btn.configure(highlightbackground="#d9d9d9")
browse_btn.configure(highlightcolor="black")
browse_btn.configure(justify='right')
browse_btn.configure(pady="0")
browse_btn.configure(text='''Browse''')

type_listbox = Listbox(root)
type_listbox.place(relx=0.02, rely=0.221, relheight=0.76, relwidth=0.245)
type_listbox.configure(background="white")
type_listbox.configure(disabledforeground="#a3a3a3")
type_listbox.configure(font="TkFixedFont")
type_listbox.configure(foreground="#000000")
type_listbox.configure(highlightbackground="#d9d9d9")
type_listbox.configure(highlightcolor="black")
type_listbox.configure(selectbackground="blue")
type_listbox.configure(selectforeground="white")
type_listbox.bind("<Double-1>", SearchAction)

folderLocation_lbl = Label(root)
folderLocation_lbl.place(relx=0.587, rely=0.331, height=20, width=180)
folderLocation_lbl.configure(activebackground="#f9f9f9")
folderLocation_lbl.configure(activeforeground="black")
folderLocation_lbl.configure(background="#d9d9d9")
folderLocation_lbl.configure(disabledforeground="#a3a3a3")
folderLocation_lbl.configure(foreground="#000000")
folderLocation_lbl.configure(highlightbackground="#d9d9d9")
folderLocation_lbl.configure(highlightcolor="black")
folderLocation_lbl.configure(relief="groove")
folderLocation_lbl.configure(text='''Label''')

reg_listbox = Listbox(root)
reg_listbox.place(relx=0.294, rely=0.221, relheight=0.76, relwidth=0.245)
reg_listbox.configure(background="white")
reg_listbox.configure(disabledforeground="#a3a3a3")
reg_listbox.configure(font="TkFixedFont")
reg_listbox.configure(foreground="#000000")
reg_listbox.configure(highlightbackground="#d9d9d9")
reg_listbox.configure(highlightcolor="black")
reg_listbox.configure(selectbackground="blue")
reg_listbox.configure(selectforeground="white")
reg_listbox.bind("<Double-1>", openSingleOnFlightradar24)

Label2 = Label(root)
Label2.place(relx=0.059, rely=0.138, height=27, width=74)
Label2.configure(activebackground="#f9f9f9")
Label2.configure(activeforeground="black")
Label2.configure(background="#d9d9d9")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(foreground="#000000")
Label2.configure(highlightbackground="#d9d9d9")
Label2.configure(highlightcolor="black")
Label2.configure(relief="ridge")
Label2.configure(text='''Aircraft Type''')

Label3 = Label(root)
Label3.place(relx=0.352, rely=0.138, height=27, width=74)
Label3.configure(activebackground="#f9f9f9")
Label3.configure(activeforeground="black")
Label3.configure(background="#d9d9d9")
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(foreground="#000000")
Label3.configure(highlightbackground="#d9d9d9")
Label3.configure(highlightcolor="black")
Label3.configure(relief="ridge")
Label3.configure(text='''Registration''')

search_btn = Button(root, command=openOnFlightradar24)
search_btn.place(relx=0.607, rely=0.47, height=24, width=167)
search_btn.configure(activebackground="#ececec")
search_btn.configure(activeforeground="#000000")
search_btn.configure(background="#d9d9d9")
search_btn.configure(disabledforeground="#a3a3a3")
search_btn.configure(foreground="#000000")
search_btn.configure(highlightbackground="#d9d9d9")
search_btn.configure(highlightcolor="black")
search_btn.configure(pady="0")
search_btn.configure(text='''Open on Flightradar 24''')

root.mainloop()
