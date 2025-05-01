import tkinter as tk
from tkinter import ttk, messagebox
from gui.dashboard import DashboardWindow

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinic Login")
        self.root.geometry("300x200")
        self.root.configure(bg="#e0f7f7")

        ttk.Label(root, text="Username").pack(pady=(20, 5))
        self.username = ttk.Entry(root, width=30)
        self.username.pack()

        ttk.Label(root, text="Password").pack(pady=(10, 5))
        self.password = ttk.Entry(root, show="*", width=30)
        self.password.pack()

        ttk.Button(root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.root.destroy()
            DashboardWindow()
        else:
            messagebox.showerror("Error", "Invalid Credentials")
