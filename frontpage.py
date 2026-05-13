"""
frontpage.py - Main GUI for Face Recognition Attendance System
"""
from tkinter import *
import os
from datetime import datetime

root = Tk()
root.configure(background="white")
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")


def function1():
    os.system("python dataset_capture.py")

def function2():
    os.system("python training_dataset.py")

def function3():
    os.system("python recognizer.py")

def attend():
    today = str(datetime.now().date())
    att_file = os.path.join(os.getcwd(), "firebase", "attendance_files", f"attendance{today}.xls")
    if os.path.exists(att_file):
        os.startfile(att_file)
    else:
        from tkinter import messagebox
        messagebox.showinfo("Info", "No attendance file found for today. Run 'Recognize + Attendance' first.")

def function6():
    root.destroy()


# Title label
Label(
    root,
    text="FACE RECOGNITION ATTENDANCE SYSTEM",
    font=("times new roman", 20),
    fg="white",
    bg="maroon",
    height=2
).grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

# Buttons
Button(root, text="Create Dataset",       font=("times new roman", 20), bg="#0D47A1", fg='white', command=function1).grid(row=3, columnspan=2, sticky=W+E+N+S, padx=5, pady=5)
Button(root, text="Train Dataset",        font=("times new roman", 20), bg="#0D47A1", fg='white', command=function2).grid(row=4, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Recognize + Attendance",font=("times new roman", 20), bg="#0D47A1", fg='white', command=function3).grid(row=5, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Attendance Sheet",     font=("times new roman", 20), bg="#0D47A1", fg='white', command=attend).grid(row=6,  columnspan=2, sticky=N+E+W+S, padx=5, pady=5)
Button(root, text="Exit",                 font=("times new roman", 20), bg="maroon",  fg='white', command=function6).grid(row=9, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

root.mainloop()
