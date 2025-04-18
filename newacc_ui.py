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

        self.conn = database.connect_to_db('lending.db')

        self.newAcc_teacher_tab()
        self.newAcc_help_tab()
    
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

        self.submit_button = ttk.Button(teacher_tab, text='Create', width=10, command=self.compare_pass)
        self.submit_button.grid(row=6, column=0, padx=5, pady=5, sticky='w')

    def compare_pass(self):
        if self.teacherPass_entry.get() == self.t_passconfirm_entry.get() and self.teacherPass_entry.get() != '' and self.t_email_entry.get() != '' and self.t_fname_entry.get() != '' and self.t_lname_entry.get() != '':
            self.new_teacher_record()
        else:
            self.worng_pass_label = ttk.Label(self.new, text='Passwords do not match or a field is empty', foreground='red')
            self.worng_pass_label.pack(pady=10)
    
    def new_teacher_record(self):
        t_id = database.generate_teacher_id()
        t_pass = self.teacherPass_entry.get()
        t_fname = self.t_fname_entry.get()
        t_lname = self.t_lname_entry.get()
        t_email = self.t_email_entry.get()

        database.new_teacher(self.conn, t_id, t_pass, t_fname, t_lname, t_email)

        self.new.destroy()

        t_id_window = tk.Tk()
        t_id_window.title('New Customer ID')
        t_id_window.geometry('300x170')
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
    

# if __name__ == "__main__":  # for testing
#     login = tk.Tk()
#     log = CreateAccUI(login)
#     login.mainloop()