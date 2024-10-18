import tkinter as tk
from tkinter import ttk
from OldCodes2.login_UI import login_UI  # Assuming login_UI is a class in login_UI.py

if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = login_UI(login)  # Instantiate the login_UI class
    login.mainloop()