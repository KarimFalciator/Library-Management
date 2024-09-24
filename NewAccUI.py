import tkinter as tk
from tkinter import ttk
import database

class CreateAccUI:

    def __init__(self, new):
        self.new = new
        self.new.title('New Account')
        self.new.geometry('400x500')
        self.new.resizable(False, False)

        self.notebook = ttk.Notebook(new)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.conn = database.connect_to_db('customers.db')

        self.newAcc_customer_tab()
        self.newAcc_librarian_tab()
        self.newAcc_help_tab()

#customer tab ---------------------------------------------------------------

    def newAcc_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(customer_tab, text='New Customer')
        
        # self.customerID_label = ttk.Label(customer_tab, text='Your New Customer ID')
        # self.customerID_label.grid(row=0, column=0, padx=10, pady=10, sticky='NESW')
        # self.CgeneratedID_label = ttk.Label(customer_tab, text='Db Customer ID')
        # self.CgeneratedID_label.grid(row=0, column=1, padx=10, pady=5, sticky='NESW')
        
        self.customerPass_label = ttk.Label(customer_tab, text='Password')
        self.customerPass_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.customerPass_entry = ttk.Entry(customer_tab, show='•')
        self.customerPass_entry.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        self.CpassConfirm_label = ttk.Label(customer_tab, text='Confirm Password')
        self.CpassConfirm_label.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.CpassConfrim_entry = ttk.Entry(customer_tab, show='•')
        self.CpassConfrim_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        
        self.show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
        self.show_pass_button.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_customer)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_customer)

        self.Cfirstname_label = ttk.Label(customer_tab, text='First Name')
        self.Cfirstname_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.Cfirstname_entry = ttk.Entry(customer_tab)
        self.Cfirstname_entry.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        self.Csurname_label = ttk.Label(customer_tab, text='Surname')
        self.Csurname_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.Csurname_entry = ttk.Entry(customer_tab)
        self.Csurname_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        self.Cemail_label = ttk.Label(customer_tab, text='Email')
        self.Cemail_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.Cemail_entry = ttk.Entry(customer_tab)
        self.Cemail_entry.grid(row=6, column=0, padx=10, pady=5, sticky='w')

        self.Caddress_label = ttk.Label(customer_tab, text='Address')
        self.Caddress_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        self.Caddress_entry = ttk.Entry(customer_tab)
        self.Caddress_entry.grid(row=6, column=1, padx=10, pady=5, sticky='w')

        self.submit_button = ttk.Button(customer_tab, text='Create', width=10, command=self.new_customer_record)
        self.submit_button.grid(row=7, column=0, padx=5, pady=5, sticky='w')

    def show_password_customer(self, event):
        self.customerPass_entry.config(show='')
        self.CpassConfrim_entry.config(show='')
        
    def hide_password_customer(self, event):
        self.customerPass_entry.config(show='•')
        self.CpassConfrim_entry.config(show='•')

    def new_customer_record(self):
        password = self.customerPass_entry.get()
        first_name = self.Cfirstname_entry.get()
        surname = self.Csurname_entry.get()
        email = self.Cemail_entry.get()
        address = self.Caddress_entry.get()

        print(password, first_name, surname, email, address)


        database.new_customer(self.conn, password, first_name, surname, email, address)
        print("Created new customer account")
        self.new.destroy()

    def close_connection(self):
        if self.conn:
            database.close_connection(self.conn)
            self.conn = None

    
#librarian tab --------------------------------------------------------------

    def newAcc_librarian_tab(self):
        librarian_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(librarian_tab, text='New Librarian')
        
        # self.librarianID_label = ttk.Label(librarian_tab, text='Librarian ID')
        # self.librarianID_label.grid(row=0, column=0, padx=10, pady=10, sticky='NESW')
        # self.Lgenerated_ID_label = ttk.Label(librarian_tab, text='Db Librarian ID')
        # self.Lgenerated_ID_label.grid(row=0, column=1, padx=10, pady=5, sticky='NESW')

        self.librarianPass_label = ttk.Label(librarian_tab, text='Password')
        self.librarianPass_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.librarianPass_entry = ttk.Entry(librarian_tab, show='•')
        self.librarianPass_entry.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        
        self.LpassConfrim_label = ttk.Label(librarian_tab, text='Confirm Password')
        self.LpassConfrim_label.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.LpassConfrim_entry = ttk.Entry(librarian_tab, show='•')
        self.LpassConfrim_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        
        self.show_pass_button = ttk.Button(librarian_tab, text='👁', width=4)
        self.show_pass_button.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_librarian)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_librarian)
        
        self.firstname_label = ttk.Label(librarian_tab, text='First Name')
        self.firstname_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.firstname_entry = ttk.Entry(librarian_tab)
        self.firstname_entry.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        self.surname_label = ttk.Label(librarian_tab, text='Surname')
        self.surname_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.surname_entry = ttk.Entry(librarian_tab)
        self.surname_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        self.email_label = ttk.Label(librarian_tab, text='Email')
        self.email_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.email_entry = ttk.Entry(librarian_tab)
        self.email_entry.grid(row=6, column=0, padx=10, pady=5, sticky='w')

        self.address_label = ttk.Label(librarian_tab, text='Address')
        self.address_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        self.address_entry = ttk.Entry(librarian_tab)
        self.address_entry.grid(row=6, column=1, padx=10, pady=5, sticky='w')

        self.submit_button = ttk.Button(librarian_tab, text='Create', width=10, command=self.new_librarian_record)
        self.submit_button.grid(row=7, column=0, padx=5, pady=5, sticky='w')


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