import tkinter as tk
from tkinter import ttk
import NewAccUI
import database

class login_UI:

    def __init__(self, login):
        self.login = login
        self.login.title('Login')
        self.login.geometry('215x300')
        self.login.resizable(False, False)

        self.notebook = ttk.Notebook(login)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.conn = database.connect_to_db('library.db')

        self.create_customer_tab()
        self.create_librarian_tab()
        self.create_help_tab()

#customer tab ---------------------------------------------------------------

    def create_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(customer_tab, text='Customer Login')
        
        self.customerID_label = ttk.Label(customer_tab, text='Customer ID')
        self.customerID_label.pack(padx=10, pady=10)
        self.customerID_entry = ttk.Entry(customer_tab)
        self.customerID_entry.pack(padx=10, pady=5)
        
        self.customerPass_label = ttk.Label(customer_tab, text='Password')
        self.customerPass_label.pack(padx=10, pady=5)
        self.customerPass_entry = ttk.Entry(customer_tab, show='•')
        self.customerPass_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_customer)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_customer)

        self.submit_button = ttk.Button(customer_tab, text='Submit', width=10, command=self.submit_customer)
        self.submit_button.pack(padx=5, pady=5)

    def show_password_customer(self, event):
        self.customerPass_entry.config(show='')
        
    def hide_password_customer(self, event):
        self.customerPass_entry.config(show='•')

    def submit_customer(self):
        customerID = self.customerID_entry.get()
        customerPass = self.customerPass_entry.get()

        check = database.check_customer_login(self.conn, customerID, customerPass)

        if check:
            success_label = ttk.Label(self.login, text='Login Successful', foreground='#009B0F', font=('Arial', 13))
            success_label.pack(pady=5)
            
            self.login.after(3500, self.login.destroy)
        else:
            error_label = ttk.Label(self.login, text='Invalid ID or password', foreground='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            
            self.login.after(7000, error_label.destroy)

    def close_connection(self):
        if self.conn:
            database.close_connection(self.conn)
            self.conn = None

#librarian tab --------------------------------------------------------------

    def create_librarian_tab(self):
        librarian_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(librarian_tab, text='Librarian Login')
        
        self.librarianID_label = ttk.Label(librarian_tab, text='Librarian ID')
        self.librarianID_label.pack(padx=10, pady=10)
        self.librarianID_entry = ttk.Entry(librarian_tab)
        self.librarianID_entry.pack(padx=10, pady=5)
        
        self.librarianPass_label = ttk.Label(librarian_tab, text='Password')
        self.librarianPass_label.pack(padx=10, pady=5)
        self.librarianPass_entry = ttk.Entry(librarian_tab, show='•')
        self.librarianPass_entry.pack(padx=10, pady=5)
        
        self.show_pass_button = ttk.Button(librarian_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)
        
        self.show_pass_button.bind('<ButtonPress>', self.show_password_librarian)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_librarian)

        self.submit_button = ttk.Button(librarian_tab, text='Submit', width=10, command=self.submit_librarian)
        self.submit_button.pack(padx=5, pady=5)

    def submit_librarian(self):
        librarianID = self.librarianID_entry.get()
        librarianPass = self.librarianPass_entry.get()

        check = database.check_librarian_login(self.conn, librarianID, librarianPass)

        if check:
            success_label = ttk.Label(self.login, text='Login Successful', foreground='#009B0F', font=('Arial', 13))
            success_label.pack(pady=5)
            
            self.login.after(3500, self.login.destroy)
        else:
            error_label = ttk.Label(self.login, text='Invalid ID or password', foreground='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            
            self.login.after(7000, error_label.destroy)

    def show_password_librarian(self, event):
        self.librarianPass_entry.config(show='')
        
    def hide_password_librarian(self, event):
        self.librarianPass_entry.config(show='•')

#help tab -------------------------------------------------------------------

    def create_help_tab(self):
        help_tab = ttk.Frame(self.notebook, width=300, height=490)
        self.notebook.add(help_tab, text='Help')
        
        self.help_label = ttk.Label(help_tab, text='Unable to login?')
        self.help_label.pack(padx=10, pady=10)
        
        self.create_account_button = ttk.Button(help_tab, text='Create a new Account', width=22, command=self.run_new_account)
        self.create_account_button.pack(padx=10, pady=10)

        self.C_Reset_button = ttk.Button(help_tab, text='User Reset Password', width=22)
        self.C_Reset_button.pack(padx=10, pady=10)

        self.L_Reset_button = ttk.Button(help_tab, text='Librarian Reset Password', width=22)
        self.L_Reset_button.pack(padx=10, pady=10)

    def run_new_account(self):
        NewAccUI.CreateAccUI(tk.Tk())
        self.login.destroy()

# if __name__ == "__main__":  # for testing
#     login = tk.Tk()
#     log = login_UI(login)
#     login.mainloop()



# class Database:
#     def __init__(self, db):
#         self.conn = sqlite3.connect(db)
#         self.cur = self.conn.cursor()
#         self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
#         self.conn.commit()

#     def insert(self, title, author, year, isbn):
#         self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
#         self.conn.commit()

#     def view(self):
#         self.cur.execute("SELECT * FROM book")
#         rows = self.cur.fetchall()
#         return rows

#     def search(self, title="", author="", year="", isbn=""):
#         self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
#         rows = self.cur.fetchall()
#         return rows

#     def delete(self, id):
#         self.cur.execute("DELETE FROM book WHERE id=?", (id,))
#         self.conn.commit()

#     def update(self, id, title, author, year, isbn):
#         self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
#         self.conn.commit()

#     def __del__(self):
#         self.conn.close()