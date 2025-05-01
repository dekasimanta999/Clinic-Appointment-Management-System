import tkinter as tk

class PatientsWindow:
    def __init__(self):
        win = tk.Toplevel()
        win.title("Patients")
        win.geometry("300x200")
        tk.Label(win, text="Patient window working").pack()
 
