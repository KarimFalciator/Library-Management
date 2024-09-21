import tkinter as tk
from tkinter import ttk

class login_UI:

    def __init__(self, login):
        self.login = login
        self.login.title('Login')
        self.login.geometry('215x300')
        self.login.resizable(False, False)

        self.notebook = ttk.Notebook(login)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.create_customer_tab()
        self.create_librarian_tab()
        self.create_help_tab()

#customer tab ---------------------------------------------------------------

    def create_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(customer_tab, text='Customer Login')
        
        self.customerID_label = ttk.Label(customer_tab, text='Customer ID')
        self.customerID_label.pack(padx=10, pady=10)
        self.customerID_entry = ttk.Entry(customer_tab)
        self.customerID_entry.pack(padx=10, pady=5)
        
        self.customerPass_label = ttk.Label(customer_tab, text='Password')
        self.customerPass_label.pack(padx=10, pady=5)
        self.customerPass_entry = ttk.Entry(customer_tab, show='•')
        self.customerPass_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password)

#librarian tab --------------------------------------------------------------

    def create_librarian_tab(self):
        librarian_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(librarian_tab, text='Librarian Login')
        
        self.librarianID_label = ttk.Label(librarian_tab, text='Librarian ID')
        self.librarianID_label.pack(padx=10, pady=10)
        self.librarianID_entry = ttk.Entry(librarian_tab)
        self.librarianID_entry.pack(padx=10, pady=5)
        
        self.librarianPass_label = ttk.Label(librarian_tab, text='Password')
        self.librarianPass_label.pack(padx=10, pady=5)
        self.librarianPass_entry = ttk.Entry(librarian_tab, show='•')
        self.librarianPass_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(librarian_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password)
        
    def create_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        
        self.help_label = ttk.Label(help_tab, text='Unable to login?')
        self.help_label.pack(padx=10, pady=10)
        
        self.C_Reset_button = ttk.Button(help_tab, text='User Reset Password')
        self.C_Reset_button.pack(padx=10, pady=10)

        self.L_Reset_button = ttk.Button(help_tab, text='Librarian Reset Password')
        self.L_Reset_button.pack(padx=10, pady=10)
    
    def show_password(self, event):
        self.librarianPass_entry.config(show='')
        
    def hide_password(self, event):
        self.librarianPass_entry.config(show='•')



if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = login_UI(login)
    login.mainloop()