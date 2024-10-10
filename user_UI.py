import tkinter as tk
from tkinter import ttk

class user_UI:

    def __init__(self, user):
        self.user = user
        self.user.title('Library Management System')
        self.user.geometry('215x300')
        self.user.resizable(False, False)


        self.notebook = ttk.Notebook(user)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.create_home_tab()
        self.create_booklist_tab()

# home tab ---------------------------------------------------------------

    def create_home_tab(self):
        home_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(home_tab, text='Customer Login')
        

# books list tab --------------------------------------------------------------

    def create_booklist_tab(self):
        booklist_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(booklist_tab, text='Lilst of books')
        

# settings
    
    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(settings_tab, text='Settings')




# help tab -------------------------------------------------------------------

    def create_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        

# if __name__ == "__main__":  # for testing
#     login = tk.Tk()
#     log = login_UI(login)
#     login.mainloop()
