import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection
from tkinter import StringVar

class AppointmentsWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Manage Appointments")
        self.win.geometry("600x450")

        # PATIENT SELECTION
        tk.Label(self.win, text="Select Patient").grid(row=0, column=0, padx=10, pady=5)
        self.patient_var = StringVar()
        self.patient_dropdown = ttk.Combobox(self.win, textvariable=self.patient_var, state="readonly", width=30)
        self.patient_dropdown.grid(row=0, column=1, pady=5)
        tk.Button(self.win, text="Add New Patient", command=self.open_add_patient).grid(row=0, column=2, padx=5)
        self.load_patients()

        # DOCTOR SELECTION
        tk.Label(self.win, text="Select Doctor").grid(row=1, column=0, padx=10, pady=5)
        self.doctor_var = StringVar()
        self.doctor_dropdown = ttk.Combobox(self.win, textvariable=self.doctor_var, state="readonly", width=30)
        self.doctor_dropdown.grid(row=1, column=1, pady=5)
        self.load_doctors()

        # DATE ENTRY
        tk.Label(self.win, text="Date (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5)
        self.date = tk.Entry(self.win)
        self.date.grid(row=2, column=1, pady=5)

        # BOOK BUTTON
        tk.Button(self.win, text="Book Appointment", command=self.add_appointment).grid(row=3, columnspan=3, pady=10)

        # APPOINTMENT LIST
        self.tree = ttk.Treeview(self.win, columns=("ID", "Patient ID", "Doctor ID", "Date"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.load_appointments()

    def load_patients(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM patients")
        self.patients = cursor.fetchall()
        conn.close()
        self.patient_dropdown['values'] = [f"{p[0]} - {p[1]}" for p in self.patients]

    def load_doctors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM doctors")
        self.doctors = cursor.fetchall()
        conn.close()
        self.doctor_dropdown['values'] = [f"{d[0]} - {d[1]}" for d in self.doctors]

    def add_appointment(self):
        selected_patient = self.patient_var.get()
        selected_doctor = self.doctor_var.get()
        date = self.date.get()

        if not selected_patient or not selected_doctor or not date:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            pid = selected_patient.split(" - ")[0]
            did = selected_doctor.split(" - ")[0]

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO appointments (patient_id, doctor_id, date) VALUES (%s, %s, %s)", (pid, did, date))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Appointment booked")
            self.load_appointments()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_appointments(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def open_add_patient(self):
        from gui.patients import PatientsWindow
        PatientsWindow()
