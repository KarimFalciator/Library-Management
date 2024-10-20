import tkinter as tk
from tkinter import ttk
import database

class main_UI:

    def __init__(self, main):
        self.main = main
        self.main.title('Lending Management System')
        self.main.geometry('600x300')
        self.main.resizable(False, False)

        self.Notebook = ttk.Notebook(main)
        self.Notebook.pack(pady=0, expand=True, fill='both')

        self.create_home_tab()
        self.create_read_tab()
        self.create_resourcelist_tab()
        self.create_settings_tab()
        self.create_help_tab()

    # home tab ---------------------------------------------------------------
    
    def create_home_tab(self):
        home_tab = ttk.Frame(self.Notebook, width=300, height=490)
        self.Notebook.add(home_tab, text='Home')

        columns = ('ref', 's_id', 'r_id', 'b_date', 'd_date', 'r_date')
        self.current_tree = ttk.Treeview(home_tab, columns=columns, show='headings')

        # Define headings
        self.current_tree.heading('ref', text='Reference')
        self.current_tree.heading('s_id', text='Student ID')
        self.current_tree.heading('r_id', text='Resource ID')
        self.current_tree.heading('b_date', text='Borrowed Date')
        self.current_tree.heading('d_date', text='Due Date')
        self.current_tree.heading('r_date', text='Returned Date')

        # Define column widths
        self.current_tree.column('ref', width=80)
        self.current_tree.column('s_id', width=90)
        self.current_tree.column('r_id', width=90)
        self.current_tree.column('b_date', width=90)
        self.current_tree.column('d_date', width=90)
        self.current_tree.column('r_date', width=90)

        self.current_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(home_tab, orient='vertical', command=self.current_tree.yview)
        scrollbar.grid(row=0, column=5, sticky='ns')
        self.current_tree.configure(yscrollcommand=scrollbar.set)

        # Add Borrowed ResourceForm
        tk.Label(home_tab, text="Student ID:").grid(row=1, column=0, padx=5, pady=5)
        self.borrowed_resource_name = tk.Entry(home_tab)
        self.borrowed_resource_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(home_tab, text="Genre:").grid(row=2, column=0, padx=5, pady=5)
        self.borrowed_resource_genre = tk.Entry(home_tab)
        self.borrowed_resource_genre.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(home_tab, text="Add Borrowed resource", command=self.add_borrowed_resource).grid(row=3, column=0, columnspan=2, pady=10)

    def add_borrowed_resource(self):
        # Fetch details from entry widgets
        name = self.borrowed_resource_name.get()
        genre = self.borrowed_resource_genre.get()
        borrowed_date = "Today"  # Static for now
        returned_date = "Not yet"  # Static for now

        # Insert into Treeview
        self.current_tree.insert('', 'end', values=(name, genre, borrowed_date, returned_date))

        # Clear the entry fields
        self.borrowed_resource_name.delete(0, 'end')
        self.borrowed_resource_genre.delete(0, 'end')


    #  read tab -----------------------------------------------------------------
    def create_read_tab(self):
        read_tab = ttk.Frame(self.Notebook, width=500, height=490)
        self.Notebook.add(read_tab, text='Previous Read resources')

        columns = ('Name', 'Genre', 'Borrowed', 'Returned')
        current_tree = ttk.Treeview(read_tab, columns=columns, show='headings')

        # Define headings
        current_tree.heading('Name', text='Name of resource')
        current_tree.heading('Genre', text='Genre')
        current_tree.heading('Borrowed', text='Borrowed')
        current_tree.heading('Returned', text='Returned')

        # Define column widths
        current_tree.column('Name', width=170)
        current_tree.column('Genre', width=110)
        current_tree.column('Borrowed', width=110)
        current_tree.column('Returned', width=110)

        current_tree.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(read_tab, orient='vertical', command=current_tree.yview)
        scrollbar.grid(row=5, column=5, sticky='ns')

        current_tree.configure(yscrollcommand=scrollbar.set)

    # resource list tab --------------------------------------------------------------
    def create_resourcelist_tab(self):
        resourcelist_tab = ttk.Frame(self.Notebook, width=300, height=490)
        self.Notebook.add(resourcelist_tab, text='List of resources')

        columns = ('Name', 'Author', 'Genre')
        self.resourcelist_tree = ttk.Treeview(resourcelist_tab, columns=columns, show='headings')

        # Define headings
        self.resourcelist_tree.heading('Name', text='Name of resource')
        self.resourcelist_tree.heading('Author', text='Author')
        self.resourcelist_tree.heading('Genre', text='Genre')

        # Define column widths
        self.resourcelist_tree.column('Name', width=170)
        self.resourcelist_tree.column('Author', width=110)
        self.resourcelist_tree.column('Genre', width=110)

        self.resourcelist_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(resourcelist_tab, orient='vertical', command=self.resourcelist_tree.yview)
        scrollbar.grid(row=0, column=5, sticky='ns')

        self.resourcelist_tree.configure(yscrollcommand=scrollbar.set)

        # Add Resource Form
        tk.Label(resourcelist_tab, text="resource Name:").grid(row=1, column=0, padx=5, pady=5)
        self.resource_name = tk.Entry(resourcelist_tab)
        self.resource_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(resourcelist_tab, text="Author:").grid(row=2, column=0, padx=5, pady=5)
        self.resource_author = tk.Entry(resourcelist_tab)
        self.resource_author.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(resourcelist_tab, text="Genre:").grid(row=3, column=0, padx=5, pady=5)
        self.resource_genre = tk.Entry(resourcelist_tab)
        self.resource_genre.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(resourcelist_tab, text="Add Resource", command=self.add_resource).grid(row=4, column=0, columnspan=2, pady=10)

    def add_resource(self):
        # Fetch details from entry widgets
        name = self.resource_name.get()
        author = self.resource_author.get()
        genre = self.resource_genre.get()

        # Insert into Treeview
        self.resourcelist_tree.insert('', 'end', values=(name, author, genre))

        # Clear the entry fields
        self.resource_name.delete(0, 'end')
        self.resource_author.delete(0, 'end')
        self.resource_genre.delete(0, 'end')


    # settings
    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.Notebook, width=300, height=490)
        self.Notebook.add(settings_tab, text='Settings')

    # help tab -------------------------------------------------------------------
    def create_help_tab(self):
        help_tab = ttk.Frame(self.Notebook, width=300, height=490)
        self.Notebook.add(help_tab, text='Help')

if __name__ == "__main__":  # for testing
    login = tk.Tk()
    log = main_UI(login)
    login.mainloop()
