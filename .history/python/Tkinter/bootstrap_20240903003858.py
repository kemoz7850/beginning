import tkinter as tk
from tkinter import messagebox
from tkinter import BooleanVar, Toplevel, Frame, BOTH, LEFT, RIGHT, VERTICAL, Y
import ttkbootstrap as tb
from ttkbootstrap.constants import PRIMARY
import sqlite3
conn = sqlite3.connect('accounts.db')
cun = conn.cursor()
root = tb.Window(themename="vapor")
text_var = tk.StringVar()
name_var = tk.StringVar()
email_var = tk.StringVar()
color_var = tk.StringVar()
password_var = tk.StringVar()
catagory_var = tk.IntVar()
buttons= tb.Style()
buttons.configure('Custom.TButton', font=('Helvetica', 12),foreground='#C0C0C0')
def on_text_change(*args): #search
    index = 0
    curt = text_var.get()
    nlst = [word[:-(len(word)-len(curt))] if len(word) > len(curt) else word for word in lst]
    for i,cur in enumerate(nlst):
        if cur.lower() == curt.lower() and len(curt)!=0:
            pass
def on_mousewheel(event): #scrolling
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
def update_scrollregion(): #update 4 scrolling
    my_canvas.update_idletasks()
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

def ADD():
    def clear(cond):
        if cond == 0:
            if len(color_var.get())<=6 and name_var.get() != "" and ((email_var.get() != "" and password_var.get() !="") and catagory_var.get() != 1 )and color_var.get() != "":
                messagebox.showinfo(title="Successful", message="Added account successfully")
            else:
                messagebox.showerror("Unsuccessful", "Invaild Format") 
            name_var.set("")
            color_var.set("")
            email_var.set("")
            password_var.set("")
        elif cond==1 and catagory_var.get() == 1:
            Email_Label.grid_remove()
            Email_Entry.grid_remove()
            Password_Label.grid_remove()
            Password_Entry.grid_remove()
        elif cond == 1 and catagory_var.get() == 0:
            Email_Label.grid()
            Email_Entry.grid()
            Password_Label.grid()
            Password_Entry.grid()

    global addwindow,editwindow
    if not addwindow.get() and not editwindow.get():
        addwindow.set(True)
        addacc = Toplevel(root)
        addacc.title("Add Account")
        deffont = ('Helvetica', 18)
        windowWidth = 425
        windowHeight = 295
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
        addacc.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        root.resizable(False, False)
        addacc.protocol("WM_DELETE_WINDOW", lambda: (addwindow.set(False) , addacc.destroy()))
        Name_Label = tb.Label(addacc, text='Name:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Name_Label.grid(column=0,row=0)
        Email_Label = tb.Label(addacc, text='Email:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Email_Label.grid(column=0,row=1)
        Password_Label = tb.Label(addacc, text='Password:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Password_Label.grid(column=0,row=2)
        Color_Label = tb.Label(addacc, text='Color:',style=PRIMARY,font=deffont,foreground="#C0C0C0")
        Color_Label.grid(column=0,row=3)
        Name_Entry = tb.Entry(addacc,width=15,textvariable=name_var,font=deffont)
        Name_Entry.grid(column=1,row=0,pady=10,padx=10)
        Email_Entry = tb.Entry(addacc,width=15,font=deffont,textvariable=email_var)
        Email_Entry.grid(column=1,row=1,pady=10,padx=10)
        Password_Entry = tb.Entry(addacc,width=15,font=deffont,textvariable=password_var)
        Password_Entry.grid(column=1,row=2,pady=10,padx=10)
        Color_Entry = tb.Entry(addacc,width=15,font=deffont,textvariable=color_var)
        Color_Entry.grid(column=1,row=3,pady=10,padx=10)
        options = ["day1","day2","day3"]
        Combo_Box = tb.Combobox(addacc,values=options)
        style = tb.Style()
        style.configure('Custom.TCheckbutton', font=('Helvetica', 18),foreground='#C0C0C0')
        Catagory = tb.Checkbutton(addacc,width=15,text="Catagory",onvalue=1,offvalue=0,style='Custom.TCheckbutton',variable=catagory_var,command=lambda:clear(1))
        Submit = tb.Button(addacc,takefocus=False,width=15,style='Custom.TButton',text="Submit",command=lambda:(database(name_var.get(),email_var.get(),password_var.get(),color_var.get(),catagory_var.get()),clear(0)))
        Catagory.grid(column=0,row=4, sticky='w')
        Submit.grid(column=1,row=4, sticky='e')
        Combo_Box.grid(column=2,row=4,sticky='w')
def EDIT():
    global editwindow,addwindow
    if not editwindow.get() and not addwindow.get():
        editwindow.set(True)
        editacc = Toplevel(root)
        windowWidth = 450
        windowHeight = 300
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
        editacc.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        root.resizable(False, False)
        editacc.protocol("WM_DELETE_WINDOW", lambda: (editwindow.set(False) , editacc.destroy()))
def database(name,email,password,color,catagory):
    print(name,email,password,color,catagory)
    cun.execute('''CREATE TABLE IF NOT EXISTS database (
    cata     TEXT,
    ID       TEXT,
    [order]  TEXT,
    suborder TEXT,
    name     TEXT,
    email    TEXT,
    password TEXT,
    color    TEXT DEFAULT ('6e40c0') 
);''')
addwindow = BooleanVar()
editwindow = BooleanVar()
#####################################################################
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 333
windowHeight = 450
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)
#####################################################################
main_frame = tb.Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = tb.Canvas(main_frame, width=100, height=405)
root.configure(bg='#110833')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = tb.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
second_frame = Frame(my_canvas, width=300, height=45*35) #50*45, 45 is y for each button and 50 is number of button
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
#####################################################################
for i in range(45):
    button = tb.Button(second_frame, text=f'Button {i}',takefocus=False,width=15,style=PRIMARY)
    if i % 2 == 0:
        button.place(x=15, y=i*35)
    else:
        button.place(x=190, y=(i-1)*35)


search = tb.Entry(root, textvariable=text_var,width=30)
edit = tb.Button(root, text='Edit',takefocus=False,width=5,style=PRIMARY,command=lambda:EDIT())
edit.pack(side='right', anchor='e')
search.pack(side='right', anchor='w',expand=True,padx=15,pady=5)
add = tb.Button(root, text='Add',takefocus=False,width=5,style=PRIMARY,command=lambda:ADD())
add.pack(side='left', anchor='e')
# Update scroll region to include all buttons
update_scrollregion()

# Bind mouse wheel scrolling
my_canvas.bind_all("<MouseWheel>", on_mousewheel)
text_var.trace_add("write", on_text_change)
root.mainloop()