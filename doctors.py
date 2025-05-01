import tkinter as tk
from tkinter import messagebox, ttk
from db import get_connection

class DoctorsWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Manage Doctors")
        self.win.geometry("500x400")

        tk.Label(self.win, text="Name").grid(row=0, column=0)
        self.name = tk.Entry(self.win)
        self.name.grid(row=0, column=1)

        tk.Label(self.win, text="Specialization").grid(row=1, column=0)
        self.spec = tk.Entry(self.win)
        self.spec.grid(row=1, column=1)

        tk.Button(self.win, text="Add Doctor", command=self.add_doctor).grid(row=2, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.win, columns=("ID", "Name", "Specialization"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.grid(row=3, columnspan=2)

        tk.Button(self.win, text="Delete Selected", command=self.delete_doctor).grid(row=4, columnspan=2, pady=10)

        self.load_doctors()

    def add_doctor(self):
        name = self.name.get()
        spec = self.spec.get()

        if not name or not spec:
            messagebox.showerror("Error", "All fields are required")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialization) VALUES (%s, %s)", (name, spec))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Doctor added")
        self.load_doctors()

    def load_doctors(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctors")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def delete_doctor(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "No doctor selected")
            return

        doc_id = self.tree.item(selected[0])['values'][0]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM doctors WHERE id = %s", (doc_id,))
        conn.commit()
        conn.close()
        self.load_doctors()
        messagebox.showinfo("Deleted", "Doctor removed")
