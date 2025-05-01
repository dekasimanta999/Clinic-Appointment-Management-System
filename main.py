import tkinter as tk
from gui.login import LoginWindow
from styles import apply_style

if __name__ == "__main__":
    root = tk.Tk()
    apply_style()
    LoginWindow(root)
    root.mainloop()
    
