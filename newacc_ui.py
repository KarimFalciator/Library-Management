import tkinter as tk
from tkinter import ttk
import OldCodes2.database as database

class CreateAccUI:

    def __init__(self, new):
        self.new = new
        self.new.title('New Account')
        self.new.geometry('400x500')
        self.new.resizable(False, False)

        self.notebook = ttk.Notebook(new)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.conn = database.connect_to_db('library.db')

        # self.newAcc_customer_tab()
        self.newAcc_teacher_tab()
        self.newAcc_help_tab()

#customer tab ---------------------------------------------------------------

    # def newAcc_customer_tab(self):
    #     customer_tab = ttk.Frame(self.notebook, width=300, height=490)
    #     self.notebook.add(customer_tab, text='New Customer')

    #     self.Cfirstname_label = ttk.Label(customer_tab, text='First Name')
    #     self.Cfirstname_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    #     self.Cfirstname_entry = ttk.Entry(customer_tab)
    #     self.Cfirstname_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')

    #     self.Csurname_label = ttk.Label(customer_tab, text='Surname')
    #     self.Csurname_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    #     self.Csurname_entry = ttk.Entry(customer_tab)
    #     self.Csurname_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    #     self.Cemail_label = ttk.Label(customer_tab, text='Email')
    #     self.Cemail_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    #     self.Cemail_entry = ttk.Entry(customer_tab)
    #     self.Cemail_entry.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    #     self.Caddress_label = ttk.Label(customer_tab, text='Address')
    #     self.Caddress_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    #     self.Caddress_entry = ttk.Entry(customer_tab)
    #     self.Caddress_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    #     self.customerPass_label = ttk.Label(customer_tab, text='Password')
    #     self.customerPass_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    #     self.customerPass_entry = ttk.Entry(customer_tab, show='•')
    #     self.customerPass_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')

    #     self.CpassConfirm_label = ttk.Label(customer_tab, text='Confirm Password')
    #     self.CpassConfirm_label.grid(row=4, column=1, padx=10, pady=5, sticky='w')
    #     self.CpassConfrim_entry = ttk.Entry(customer_tab, show='•')
    #     self.CpassConfrim_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        
    #     self.show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
    #     self.show_pass_button.grid(row=5, column=2, padx=5, pady=5, sticky='w')
        
    #     self.show_pass_button.bind('<ButtonPress>', self.show_password_customer)
    #     self.show_pass_button.bind('<ButtonRelease>', self.hide_password_customer)

    #     self.submit_button = ttk.Button(customer_tab, text='Create', width=10, command=self.new_customer_record)
    #     self.submit_button.grid(row=6, column=0, padx=5, pady=5, sticky='w')

    # def show_password_customer(self, event):
    #     self.customerPass_entry.config(show='')
    #     self.CpassConfrim_entry.config(show='')
        
    # def hide_password_customer(self, event):
    #     self.customerPass_entry.config(show='•')
    #     self.CpassConfrim_entry.config(show='•')

    # def new_customer_record(self):
    #     c_id = database.generate_customer_id()
    #     password = self.customerPass_entry.get()
    #     first_name = self.Cfirstname_entry.get()
    #     surname = self.Csurname_entry.get()
    #     email = self.Cemail_entry.get()
    #     address = self.Caddress_entry.get()

    #     print(c_id, password, first_name, surname, email, address)


    #     database.new_customer(self.conn, c_id, password, first_name, surname, email, address)
    #     print("Created new customer account")
    #     self.new.destroy()
    
    #     C_id_window = tk.Tk()
    #     C_id_window.title('New Customer ID')
    #     C_id_window.geometry('200x100')
    #     C_id_window.resizable(False, False)
    #     C_id_window_label = ttk.Label(C_id_window, text='Your new Customer ID is:' + str(c_id))
    #     C_id_window_label.pack(pady=10)

    #     advice_label = ttk.Label(C_id_window, text='Please keep this ID safe, you will need it to login')
    #     advice_label.pack(pady=10)

    # def close_connection(self):
    #     if self.conn:
    #         database.close_connection(self.conn)
    #         self.conn = None

    
# Teacher tab --------------------------------------------------------------

    def newAcc_teacher_tab(self):
        teacher_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(teacher_tab, text='New Teacher')
        
        self.t_fname_label = ttk.Label(teacher_tab, text='First Name')
        self.t_fname_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.t_fname_entry = ttk.Entry(teacher_tab)
        self.t_fname_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.t_lname_label = ttk.Label(teacher_tab, text='Surname')
        self.t_lname_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.t_lname_entry = ttk.Entry(teacher_tab)
        self.t_lname_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.t_email_label = ttk.Label(teacher_tab, text='Email')
        self.t_email_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.t_email_entry = ttk.Entry(teacher_tab)
        self.t_email_entry.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        self.t_address_label = ttk.Label(teacher_tab, text='Address')
        self.t_address_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.t_address_entry = ttk.Entry(teacher_tab)
        self.t_address_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.teacherPass_label = ttk.Label(teacher_tab, text='Password')
        self.teacherPass_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.teacherPass_entry = ttk.Entry(teacher_tab, show='•')
        self.teacherPass_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        
        self.t_passconfirm_label = ttk.Label(teacher_tab, text='Confirm Password')
        self.t_passconfirm_label.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        self.t_passconfirm_entry = ttk.Entry(teacher_tab, show='•')
        self.t_passconfirm_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        
        self.t_showpass = ttk.Button(teacher_tab, text='👁', width=4)
        self.t_showpass.grid(row=5, column=2, padx=5, pady=5, sticky='w')
        
        self.t_showpass.bind('<ButtonPress>', self.show_password_teacher)
        self.t_showpass.bind('<ButtonRelease>', self.hide_password_teacher)

        self.submit_button = ttk.Button(teacher_tab, text='Create', width=10, command=self.new_teacher_record)
        self.submit_button.grid(row=6, column=0, padx=5, pady=5, sticky='w')


    def new_teacher_record(self):
        t_id = database.generate_teacher_id()
        t_pass = self.teacherPass_entry.get()
        t_fname = self.t_fname_entry.get()
        t_lname = self.t_lname_entry.get()
        t_email = self.t_email_entry.get()
        t_address = self.t_address_entry.get()

        database.new_teacher(self.conn, t_id, t_pass, t_fname, t_lname, t_email, t_address)

        self.new.destroy()

        t_id_window = tk.Tk()
        t_id_window.title('New Customer ID')
        t_id_window.geometry('200x100')
        t_id_window.resizable(False, False)
        t_id_window_label = ttk.Label(t_id_window, text='Your new Customer ID is:' + str(t_id))
        t_id_window_label.pack(pady=10)

        advice_label = ttk.Label(t_id_window, text='Please keep this ID safe, you will need it to login')
        advice_label.pack(pady=10)

    def show_password_teacher(self, event):
        self.teacherPass_entry.config(show='')
        self.t_passconfirm_entry.config(show='')
        
    def hide_password_teacher(self, event):
        self.teacherPass_entry.config(show='•')
        self.t_passconfirm_entry.config(show='•')

#help tab -----------------------------------------------------------------------

    def newAcc_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        
        self.help_label = ttk.Label(help_tab, text='Id is a unique number pregenerated show after creating the account')
        self.help_label.pack(padx=10, pady=10)
        
        self.help_label = ttk.Label(help_tab, text='Problem Creating Account?')
        self.help_label.pack(padx=10, pady=10)

        self.help_label = ttk.Label(help_tab, text='Contact us at b34226@sfc.potteries.ac.uk or ask a teacher for help')
        self.help_label.pack(padx=10, pady=10)
    

if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = CreateAccUI(login)
    login.mainloop()