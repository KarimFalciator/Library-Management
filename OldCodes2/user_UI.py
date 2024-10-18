import tkinter as tk
from tkinter import ttk

class user_UI:

    def __init__(self, user):
        self.user = user
        self.user.title('Library Management System')
        self.user.geometry('550x300')
        self.user.resizable(False, False)


        self.notebook = ttk.Notebook(user)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.create_home_tab()
        self.create_read_tab()
        self.create_booklist_tab()
        self.create_settings_tab()
        self.create_help_tab()


# home tab ---------------------------------------------------------------
    
    def create_home_tab(self):
        home_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(home_tab, text='Home')

        columns = ('Name', 'Genre', 'Borrowed', 'Returned')
        previous_books_tree = ttk.Treeview(home_tab, columns=columns, show='headings', height=2)

    # Define headings

        previous_books_tree.heading('Name', text='Name of Book')
        previous_books_tree.heading('Genre', text='Genre')
        previous_books_tree.heading('Borrowed', text='Borrowed')
        previous_books_tree.heading('Returned', text='Returned')

    # Define column widths

        previous_books_tree.column('Name', width=170)
        previous_books_tree.column('Genre', width=110)
        previous_books_tree.column('Borrowed', width=110)
        previous_books_tree.column('Returned', width=110)

        previous_books_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

    # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(home_tab, orient='vertical', command=previous_books_tree.yview)
        scrollbar.grid(row=5, column=5, sticky='ns')

        previous_books_tree.configure(yscrollcommand=scrollbar.set)


#  read tab -----------------------------------------------------------------


    def create_read_tab(self):
        read_tab = ttk.Frame(self.notebook, width=500, height=490)
        self.notebook.add(read_tab, text='Previous Read Books')

        columns = ('Name', 'Genre', 'Borrowed', 'Returned')
        previous_books_tree = ttk.Treeview(read_tab, columns=columns, show='headings')

    # Define headings

        previous_books_tree.heading('Name', text='Name of Book')
        previous_books_tree.heading('Genre', text='Genre')
        previous_books_tree.heading('Borrowed', text='Borrowed')
        previous_books_tree.heading('Returned', text='Returned')

    # Define column widths

        previous_books_tree.column('Name', width=170)
        previous_books_tree.column('Genre', width=110)
        previous_books_tree.column('Borrowed', width=110)
        previous_books_tree.column('Returned', width=110)

        previous_books_tree.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

    # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(read_tab, orient='vertical', command=previous_books_tree.yview)
        scrollbar.grid(row=5, column=5, sticky='ns')

        previous_books_tree.configure(yscrollcommand=scrollbar.set)
        

# books list tab --------------------------------------------------------------

    def create_booklist_tab(self):
        booklist_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(booklist_tab, text='List of books')
        

# settings
    
    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(settings_tab, text='Settings')


# help tab -------------------------------------------------------------------

    def create_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        

if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = user_UI(login)
    login.mainloop()
