import tkinter as tk
from tkinter import ttk
import newacc_ui
import database

class login_UI:

    def __init__(self, login):
        self.login = login
        self.login.title('Login')
        self.login.geometry('215x300')
        self.login.resizable(False, False)

        self.notebook = ttk.Notebook(login)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.conn = database.connect_to_db('lending.db')

        self.create_teacher_tab()
        self.create_help_tab()

# Teacher tab --------------------------------------------------------------

    def create_teacher_tab(self):
        teacher_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(teacher_tab, text='Teacher Login')
        
        self.teacherID_label = ttk.Label(teacher_tab, text='Teacher ID')
        self.teacherID_label.pack(padx=10, pady=10)
        self.teacherID_entry = ttk.Entry(teacher_tab)
        self.teacherID_entry.pack(padx=10, pady=5)
        
        self.teacherPass_label = ttk.Label(teacher_tab, text='Password')
        self.teacherPass_label.pack(padx=10, pady=5)
        self.teacherPass_entry = ttk.Entry(teacher_tab, show='•')
        self.teacherPass_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(teacher_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_teacher)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_teacher)

        self.submit_button = ttk.Button(teacher_tab, text='Submit', width=10, command=self.submit_teacher)
        self.submit_button.pack(padx=5, pady=5)

    def submit_teacher(self):
        teacherID = self.teacherID_entry.get()
        teacherPass = self.teacherPass_entry.get()

        check = database.check_teacher_login(self.conn, teacherID, teacherPass)

        if check:
            success_label = ttk.Label(self.login, text='Login Successful', foreground='#009B0F', font=('Arial', 13))
            success_label.pack(pady=5)
            
            self.login.after(3500, self.login.destroy)
        else:
            error_label = ttk.Label(self.login, text='Invalid ID or password', foreground='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            
            self.login.after(7000, error_label.destroy)

    def show_password_teacher(self, event):
        self.teacherPass_entry.config(show='')
        
    def hide_password_teacher(self, event):
        self.teacherPass_entry.config(show='•')

#help tab -------------------------------------------------------------------

    def create_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        
        self.help_label = ttk.Label(help_tab, text='Unable to login?')
        self.help_label.pack(padx=10, pady=10)
        
        self.create_account_button = ttk.Button(help_tab, text='Create a new Account', width=22, command=self.run_new_account)
        self.create_account_button.pack(padx=10, pady=10)

        self.L_Reset_button = ttk.Button(help_tab, text='Teacher Reset Password', width=22)
        self.L_Reset_button.pack(padx=10, pady=10)

    def run_new_account(self):
        newacc_ui.CreateAccUI(tk.Tk())
        self.login.destroy()

if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = login_UI(login)
    login.mainloop()