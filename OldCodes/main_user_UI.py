import tkinter as tk
from tkinter import ttk
import NewAccUI
import database


class login_UI:

    def __init__(self, user_w):
        self.main_user = user_w
        self.main_user.title('Login')
        self.main_user.geometry('400x500')
        self.main_user.resizable(False, False)

        self.notebook = ttk.Notebook(login)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.create_home_tab()
        self.create_list_tab()
        self.create_help_tab()

    # customer tab ---------------------------------------------------------------

    def create_home_tab(self):
        home_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(home_tab, text='Home')


    # list tab --------------------------------------------------------------

    def create_list_tab(self):
        list_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(list_tab, text='Book List')


    # settings tab
    def create_settings_tab(self):
        list_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(list_tab, text='Settings')



    # help tab -------------------------------------------------------------------

    def create_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')

        self.help_label = ttk.Label(help_tab, text='Unable to pre-order a book?')
        self.help_label.pack(padx=10, pady=10)

        self.contact_label = ttk.Label(help_tab, text='Contact us at b34226@sfc.potteries.ac.uk', width=22)
        self.contact_label.pack(padx=10, pady=10)





if __name__ == '__main__':
    login = tk.Tk()
    log = login_UI(login)  # Instantiate the login_UI class
    login.mainloop()