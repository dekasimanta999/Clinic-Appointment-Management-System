import tkinter as tk
from gui.patients import PatientsWindow
from gui.doctors import DoctorsWindow
from gui.appointments import AppointmentsWindow

class DashboardWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Clinic Dashboard")
        self.win.geometry("300x300")

        tk.Button(self.win, text="Manage Patients", width=25, command=PatientsWindow).pack(pady=10)
        tk.Button(self.win, text="Manage Doctors", width=25, command=DoctorsWindow).pack(pady=10)
        tk.Button(self.win, text="Manage Appointments", width=25, command=AppointmentsWindow).pack(pady=10)

        self.win.mainloop()
