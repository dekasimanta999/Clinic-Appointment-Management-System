# styles.py
from tkinter import ttk

def apply_style():
    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' for a modern feel

    style.configure("TButton",
                    font=("Segoe UI", 10),
                    padding=6)

    style.configure("TLabel",
                    font=("Segoe UI", 10))

    style.configure("TEntry",
                    padding=5)

    style.configure("Treeview.Heading",
                    font=("Segoe UI", 10, "bold"),
                    foreground="#295b5b")

    style.configure("Treeview",
                    font=("Segoe UI", 10),
                    rowheight=25)
