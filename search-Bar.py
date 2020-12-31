import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import time
from PIL import ImageTk, Image
import shutil
from shutil import SameFileError


###### backend ###################
filecount = 1
def savefile():
    global file_check, prog
    try:
            file = asksaveasfilename(initialfile="{}".format(saving), defaultextension="{}".format(ext), filetypes=[("All files", "*.*"),\
                ("Picture", "{}".format(ext))])
            p = os.path.split(file)
            shutil.copy(p[1], p[0])
            file_check.set("")
            aal.set("")
    except SameFileError:
        t1.insert(1.0, "File replaced by existing file!")

    except FileNotFoundError:
        t1.delete(1.0, 'end')
        t1.insert(1.0, "File not Saved")
    except NameError:
        t1.delete(1.0, 'end')
        t1.insert(1.0, "No file found!")

s = ('Desktop', 'Complete')
files1 = []
f = ''
val=0
image_path = ''
count = 0


# paths
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
profile = os.path.join(os.environ['USERPROFILE'])

def selection():
    global text,filecount ,canvas,a1, root, val, aal, files1,_list1,complete_path, count, path_search,aal, prog
    aal = StringVar()
    count = 0
    ### Backends ####
    try:
        if path_search.get() == 'Complete':
            complete_path = desktop
        elif path_search.get() == 'Desktop':
            complete_path = profile

        Label(canvas, text='Loading files...', font="calibri 12").place(x=268, y = 740)
        l = Label(canvas, font="calibri 12")
        l.place(x = 380, y = 740)
        prog = ttk.Progressbar(canvas, orient=HORIZONTAL, length=400, mode='determinate')
        prog.place(x=268, y=765)
        text.delete(1.0, 'end')
        t1.delete(1.0, 'end')
        
        files1 = []
        load.set("Loading Data...")

        
        for path, folder, files in os.walk(complete_path):
            for filename in files:
                ext = len(filename) - 4
                if filename[ext:] == '.png' or filename[ext:] == '.jpg':
                    count += 1
                    files1.append(filename)
                    l['text'] = f"({filecount})"
                    prog['value'] = val
                    root.update_idletasks()
                    text.insert(1.0, "{}\n".format(filename))
                    time.sleep(0.0000001)
                    filecount += 1
                    val += 1
                    if val > 100:
                        val = 0

        val = 100
        prog['value'] = val
        time.sleep(0.0000001)
        # showing message after the search is done
        messagebox.showinfo("Search", "Search is completed - ({}) - files found".format(filecount-1))
        time.sleep(0.0000001)
        #Label(canvas, text="Save the file", font="consolas 10 bold").place(x=738, y=257)
        a1 = Entry(canvas, font='consolas 18',width=21,  textvariable=aal)
        a1.place(x=738, y=281)

        # Button(canvas,bg='red',text='Browser', fg='white', relief='solid',height=0 ,font="Agencyfb 11 bold", command=savefile).place(x=1025, y=281)
        # placing filenames in the list box
        _list1['values'] = files1
    except NameError:
        t1.insert(1.0, 'Insert the Path')


def openpic():
    global complete_path, image_path,a1 ,t1, file_check, f, saving, ext
    image_path = ''
    f = ''
    saving = ''
    ext = ''
    try:
        # new root for images
        r = tk.Toplevel()

        pic = file_check.get()
        for i, j, k in os.walk(complete_path):
            for fi in k:
                if pic == fi:
                    image_path = i
                    f = fi

        # getting to the images directory
        os.chdir(image_path)

        # openning the images .jog and .png
        photo = ImageTk.PhotoImage(Image.open(f))
        Label(r, image=photo).pack()

        # inserting and deleting from the entries
        a1.delete(0, 'end')
        a1.insert('end',f)

        # filename to save
        name_file = len(f) - 4
        saving = f[:name_file]
        # extension of file to save
        file_end = len(f) - 4
        ext = f[file_end:]
        r.mainloop()

    except OSError:
        t1.delete(1.0, END)
        t1.insert(1.0, "Insert Image!")
        r.destroy()

    except NameError:
        t1.delete(1.0, END)
        t1.insert(1.0, "Path is not defined")
        r.destroy()
#################### Backend ends ###################

############### bindings ############################
def Main():
    root.destroy()
    main()

def e(E):
    global ass
    ass['font'] = 'Agencyfb 20 underline'

def l(ee):
    global ass
    ass['font']= 'Agencyfb 20 '

def e1(E):
    global ass1
    ass1['font'] = 'Agencyfb 20 underline'

def l1(ee):
    global ass
    ass1['font']= 'Agencyfb 20 '
############## ends ################################

def images():

    global canvas
    global ass, ass1
    global b
    global files
    global text
    global path_search
    global file_check, _list1, t1, load, aal

    path_search = tk.StringVar()
    file_check = tk.StringVar()
    load = StringVar()
    load.set("Not Loading")

    picframe.destroy()
    root.update()

    b['relief'] = 'solid'

    Label(canvas, text="Path to search", font="consolas 10 bold").place(x=266, y=93)
    Label(canvas, text="Select the image", font="consolas 10 bold").place(x=740, y=193)

    _list = ttk.Combobox(canvas, textvariable=path_search, width=20, font='consolas 18')
    _list['values'] = s
    _list.place(x= 266, y = 114)

    ass = tk.Button(canvas, text='Home', font='Agencyfb 20', bg='red', fg='white', relief='solid', command=Main)
    ass.place(x=62, y=214)
    ass1 = tk.Button(canvas, text='Exit', font='Agencyfb 20', bg='red', fg='white', relief='flat', command=exit)
    ass1.place(x=74, y=278)

    # hoverings
    ass.bind('<Enter>', e)
    ass.bind('<Leave>', l)
    ass1.bind('<Enter>', e1)
    ass1.bind('<Leave>', l1)

    button = tk.Button(canvas, text='Select',bg='red', fg='white', relief='flat',height=0 ,font="Agencyfb 11 bold", command=selection)
    button.place(x=618, y=115)

    scrollbar = Scrollbar(canvas)
    text = tk.Text(canvas, wrap=WORD ,width=50, height=30,highlightbackground='#7baedc' ,font='calibri 12',highlightcolor='#7baedc',yscrollcommand=scrollbar.set)
    text.place(x=268, y=161)
    text.focus_set()
    scrollbar.place(x=674, y=161, relheight=0.73)
    scrollbar.config(command=text.yview)

    msg = tk.Label(canvas, text='Choose the place where you want to search',fg='red' ,font="calibri 13 bold")
    msg.place(x=729, y=121)

    _list1 = ttk.Combobox(canvas, textvariable=file_check, width=17, font='consolas 18')
    _list1.place(x= 738, y = 215)

    button1 = tk.Button(canvas, text='Open',bg='red', fg='white', relief='solid', height=1, font="Agencyfb 11 bold", command=openpic)
    button1.place(x=1042, y=216)

    label3 = tk.Label(canvas, text='Error Encounters:', font='calibri 14 bold', relief='flat')
    label3.place(x=738, y=315)

    t1 = tk.Text(canvas, width=50,relief='groove',  height=10)
    t1.place(x=738, y=352)
    aal = Label(canvas, textvar=load, font="calibri 12")
    aal.place(x=268, y = 740)
    prog = ttk.Progressbar(canvas, orient=HORIZONTAL, length=400, mode='determinate')
    prog.place(x=268, y=765)

    Label(canvas, text="Save the file", font="consolas 11").place(x=738, y=257)
    a1 = Entry(canvas, font='consolas 18', width=19 ,textvariable=aal)
    a1.place(x=738, y=281)

    Button(canvas,bg='red',text='Browser', fg='white', relief='solid',height=0 ,font="Agencyfb 11 bold", command=savefile).place(x=1042, y=281)


def coords(event):
    pass
    #print("{} {}".format(event.x, event.y))

def enter(event):
    global b
    b['font'] = 'Agencyfb 15 underline bold'
    b['fg'] = 'lightgrey'

def leave(event):
    global b
    b['font'] = 'Agencyfb 15 bold'
    b['fg'] = 'white'

def en(e):
    global p1l
    p1l['background'] = "lightgrey"
def le(e):
    global p1l
    p1l['background'] = "Systembackground"
def ent(e):
    global p12
    p12['background'] = "lightgrey"
def lea(e):
    global p12
    p12['background'] = "Systembackground"


def main():
    global root, canvas, b, b1, b2, p1l, p12, picframe
    root = tk.Tk()
    root.geometry("1200x800+100+0")
    root.maxsize(1200, 800)
    root.minsize(1200, 800)
    root.title("Search")
    root.wm_attributes("-topmost", 0)

    canvas = tk.Canvas(root, width=1200, height=800)
    canvas.pack()
    pass
    #canvas.bind_all("<Button-1>", coords)

    canvas.create_rectangle(0,0,255, 799, fill='red', width=4)
    canvas.create_rectangle(255,0,1199, 87, fill='orange', width=4)
    canvas.create_line(15,90,222, 90, fill='grey', width=4)

    picframe = tk.Frame(canvas, width=800, height=500)
    picframe.place(x = 272, y = 217)

    tk.Label(picframe, text='Images', font='calibri 10').place(x=395, y=280)


    label = tk.Label(canvas, text='Search Bar Personal Project',  fg="white", font='elephant 27' ,bg='orange')
    label.place(x = 450, y = 20)

    label1 = tk.Label(canvas, text='@ Search Bar', fg="ghost white", font='Algerian 18', bg='red')
    label1.place(x = 8, y = 13)

    ico2 = tk.PhotoImage(file="2.png")
    p12 = tk.Button(picframe, image=ico2, relief='flat',height=140, bg='Systembackground', command=images)
    p12.place(x=353, y=124)
    p12.bind('<Enter>', ent)
    p12.bind('<Leave>', lea)

    b = tk.Button(canvas, text='Image Search', anchor='n', font='Agencyfb 15 bold', bg='red', fg='white', relief='flat', width=16, command=images)
    b.place(x = 3, y = 124)
    b.bind('<Enter>', enter)
    b.bind('<Leave>', leave)
    root.mainloop()

if __name__ == '__main__':
    main()
