import tkinter as tk
from PIL import Image, ImageTk
#Window
root = tk.Tk()
root.geometry("800x700")
root.title("Account Overview")
def read_from_db():
    cursor.execute("SELECT *, oid FROM Student")
    data = c.fetchall()
    showData = ''
    for data in Student:
        showData += str(data) + "\n"

root.mainloop()