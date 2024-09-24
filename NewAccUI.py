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

        self.conn = database.connect_to_db('log_info.db')

        self.newAcc_customer_tab()
        self.newAcc_librarian_tab()
        self.newAcc_help_tab()

#customer tab ---------------------------------------------------------------

    def newAcc_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(customer_tab, text='New Customer')

        self.Cfirstname_label = ttk.Label(customer_tab, text='First Name')
        self.Cfirstname_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.Cfirstname_entry = ttk.Entry(customer_tab)
        self.Cfirstname_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.Csurname_label = ttk.Label(customer_tab, text='Surname')
        self.Csurname_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.Csurname_entry = ttk.Entry(customer_tab)
        self.Csurname_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.Cemail_label = ttk.Label(customer_tab, text='Email')
        self.Cemail_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.Cemail_entry = ttk.Entry(customer_tab)
        self.Cemail_entry.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        self.Caddress_label = ttk.Label(customer_tab, text='Address')
        self.Caddress_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.Caddress_entry = ttk.Entry(customer_tab)
        self.Caddress_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.customerPass_label = ttk.Label(customer_tab, text='Password')
        self.customerPass_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.customerPass_entry = ttk.Entry(customer_tab, show='•')
        self.customerPass_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')

        self.CpassConfirm_label = ttk.Label(customer_tab, text='Confirm Password')
        self.CpassConfirm_label.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        self.CpassConfrim_entry = ttk.Entry(customer_tab, show='•')
        self.CpassConfrim_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        
        self.show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
        self.show_pass_button.grid(row=5, column=2, padx=5, pady=5, sticky='w')
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_customer)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_customer)

        self.submit_button = ttk.Button(customer_tab, text='Create', width=10, command=self.new_customer_record)
        self.submit_button.grid(row=6, column=0, padx=5, pady=5, sticky='w')

    def show_password_customer(self, event):
        self.customerPass_entry.config(show='')
        self.CpassConfrim_entry.config(show='')
        
    def hide_password_customer(self, event):
        self.customerPass_entry.config(show='•')
        self.CpassConfrim_entry.config(show='•')

    def new_customer_record(self):
        id = database.generate_customer_id()
        password = self.customerPass_entry.get()
        first_name = self.Cfirstname_entry.get()
        surname = self.Csurname_entry.get()
        email = self.Cemail_entry.get()
        address = self.Caddress_entry.get()

        print(id, password, first_name, surname, email, address)


        database.new_customer(self.conn, id, password, first_name, surname, email, address)
        print("Created new customer account")
        self.new.destroy()
    
        C_id_window = tk.Tk()
        C_id_window.title('New Customer ID')
        C_id_window.geometry('200x100')
        C_id_window.resizable(False, False)
        C_id_window_label = ttk.Label(C_id_window, text='Your new Customer ID is: {id}')
        C_id_window_label.pack(pady=10)

        advice_label = ttk.Label(C_id_window, text='Please keep this ID safe, you will need it to login')
        advice_label.pack(pady=10)

    def close_connection(self):
        if self.conn:
            database.close_connection(self.conn)
            self.conn = None

    
#librarian tab --------------------------------------------------------------

    def newAcc_librarian_tab(self):
        librarian_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(librarian_tab, text='New Librarian')
        
        self.Lfirstname_label = ttk.Label(librarian_tab, text='First Name')
        self.Lfirstname_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.Lfirstname_entry = ttk.Entry(librarian_tab)
        self.Lfirstname_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.Lsurname_label = ttk.Label(librarian_tab, text='Surname')
        self.Lsurname_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.Lsurname_entry = ttk.Entry(librarian_tab)
        self.Lsurname_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.Lemail_label = ttk.Label(librarian_tab, text='Email')
        self.Lemail_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.Lemail_entry = ttk.Entry(librarian_tab)
        self.Lemail_entry.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        self.Laddress_label = ttk.Label(librarian_tab, text='Address')
        self.Laddress_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.Laddress_entry = ttk.Entry(librarian_tab)
        self.Laddress_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.librarianPass_label = ttk.Label(librarian_tab, text='Password')
        self.librarianPass_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.librarianPass_entry = ttk.Entry(librarian_tab, show='•')
        self.librarianPass_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        
        self.LpassConfrim_label = ttk.Label(librarian_tab, text='Confirm Password')
        self.LpassConfrim_label.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        self.LpassConfrim_entry = ttk.Entry(librarian_tab, show='•')
        self.LpassConfrim_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        
        self.Lshow_pass_button = ttk.Button(librarian_tab, text='👁', width=4)
        self.Lshow_pass_button.grid(row=5, column=2, padx=5, pady=5, sticky='w')
        
        self.Lshow_pass_button.bind('<ButtonPress>', self.show_password_librarian)
        self.Lshow_pass_button.bind('<ButtonRelease>', self.hide_password_librarian)

        self.submit_button = ttk.Button(librarian_tab, text='Create', width=10, command=self.new_librarian_record)
        self.submit_button.grid(row=6, column=0, padx=5, pady=5, sticky='w')


    def new_librarian_record(self):
        l_id = database.generate_librarian_id()
        password = self.librarianPass_entry.get()
        first_name = self.Lfirstname_entry.get()
        surname = self.Lsurname_entry.get()
        email = self.Lemail_entry.get()
        address = self.Laddress_entry.get()

        database.new_librarian(self.conn, password, first_name, surname, email, address)

        self.new.destroy()

        L_id_window = tk.Tk()
        L_id_window.title('New Customer ID')
        L_id_window.geometry('200x100')
        L_id_window.resizable(False, False)
        L_id_window_label = ttk.Label(L_id_window, text='Your new Customer ID is: {id}')
        L_id_window_label.pack(pady=10)

        advice_label = ttk.Label(L_id_window, text='Please keep this ID safe, you will need it to login')
        advice_label.pack(pady=10)

    def show_password_librarian(self, event):
        self.librarianPass_entry.config(show='')
        self.LpassConfrim_entry.config(show='')
        
    def hide_password_librarian(self, event):
        self.librarianPass_entry.config(show='•')
        self.LpassConfrim_entry.config(show='•')

#help tab -----------------------------------------------------------------------

    def newAcc_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        
        self.help_label = ttk.Label(help_tab, text='Id is a unique number pregenerated show after creating the account')
        self.help_label.pack(padx=10, pady=10)
        
        self.help_label = ttk.Label(help_tab, text='Problem Creating Account?')
        self.help_label.pack(padx=10, pady=10)

        self.help_label = ttk.Label(help_tab, text='Contact us at b34226@sfc.potteries.ac.uk or ask a librarian for help')
        self.help_label.pack(padx=10, pady=10)
    

if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = CreateAccUI(login)
    login.mainloop()