import tkinter as tk
from tkinter import ttk

class CreateAccUI:

    def __init__(self, new):
        self.new = new
        self.new.title('New Account')
        self.new.geometry('215x300')
        self.new.resizable(False, False)

        self.notebook = ttk.Notebook(new)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.newAcc_customer_tab()
        self.newAcc_librarian_tab()
        self.newAcc_help_tab()

#customer tab ---------------------------------------------------------------

    def newAcc_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(customer_tab, text='New Customer')
        
        self.customerID_label = ttk.Label(customer_tab, text='Generated Customer ID')
        self.customerID_label.pack(padx=10, pady=10)
        #this will be generated by the system and displayed here to be done when database is implemented
        # self.CgeneratedId_label = ttk.Entry(customer_tab, text=Generated Customer ID)
        # self.Cgenerated_label.pack(padx=10, pady=5)
        
        self.customerPass_label = ttk.Label(customer_tab, text='Password')
        self.customerPass_label.pack(padx=10, pady=5)
        self.customerPass_entry = ttk.Entry(customer_tab, show='•')
        self.customerPass_entry.pack(padx=10, pady=5)

        self.CpassConfirm_label = ttk.Label(customer_tab, text='Password Confirm')
        self.CpassConfirm_label.pack(padx=10, pady=5)
        self.CpassConfrim_entry = ttk.Entry(customer_tab, show='•')
        self.CpassConfrim_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_customer)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_customer)

        self.submit_button = ttk.Button(customer_tab, text='Create', width=10, command=self.new_customer_record)
        self.submit_button.pack(padx=5, pady=5)

    def new_customer_record(self):
        # Placeholder for the function to be defined later
        print("Creating new customer account")
        self.new.destroy()

    def show_password_customer(self, event):
        self.customerPass_entry.config(show='')
        self.CpassConfrim_entry.config(show='')
        
    def hide_password_customer(self, event):
        self.customerPass_entry.config(show='•')
        self.CpassConfrim_entry.config(show='•')

#librarian tab --------------------------------------------------------------

    def newAcc_librarian_tab(self):
        librarian_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(librarian_tab, text='New Librarian')
        
        self.librarianID_label = ttk.Label(librarian_tab, text='Librarian ID')
        self.librarianID_label.pack(padx=10, pady=10)
        #this will be generated by the system and displayed here to be done when database is implemented
        # self.Lgenerated_ID_label = ttk.label(librarian_tab, text=Generated Librarian ID)
        # self.Lgenerated_label.pack(padx=10, pady=5)
        
        self.librarianPass_label = ttk.Label(librarian_tab, text='Password')
        self.librarianPass_label.pack(padx=10, pady=5)
        self.librarianPass_entry = ttk.Entry(librarian_tab, show='•')
        self.librarianPass_entry.pack(padx=10, pady=5)
        
        self.LpassConfrim_label = ttk.Label(librarian_tab, text='Confirm Password')
        self.LpassConfrim_label.pack(padx=10, pady=5)
        self.LpassConfrim_entry = ttk.Entry(librarian_tab, show='•')
        self.LpassConfrim_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(librarian_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_librarian)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_librarian)
        
        self.submit_button = ttk.Button(librarian_tab, text='Create', width=10, command=self.new_librarian_record)
        self.submit_button.pack(padx=5, pady=5)

    def new_librarian_record(self):
        # Placeholder for the function to be defined later
        print("Creating new librarian account")
        self.new.destroy()

    def show_password_librarian(self, event):
        self.librarianPass_entry.config(show='')
        self.LpassConfrim_entry.config(show='')
        
    def hide_password_librarian(self, event):
        self.customerPass_entry.config(show='•')
        self.CpassConfrim_entry.config(show='•')


    def newAcc_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        
        self.help_label = ttk.Label(help_tab, text='Id is a unique number pregenerated')
        self.help_label.pack(padx=10, pady=10)
        
        self.help_label = ttk.Label(help_tab, text='Problem Creating Account?')
        self.help_label.pack(padx=10, pady=10)

        self.help_label = ttk.Label(help_tab, text='Contact us b34226@sfc.potteries.ac.uk')
        self.help_label.pack(padx=10, pady=10)
    
    def show_password(self, event):
        self.librarianPass_entry.config(show='')
        
    def hide_password(self, event):
        self.librarianPass_entry.config(show='•')



if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = CreateAccUI(login)
    login.mainloop()