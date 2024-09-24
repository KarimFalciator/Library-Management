import tkinter as tk
from tkinter import ttk
import database

class login_UI:

    def __init__(self, login):
        self.login = login
        self.login.title('Login')
        self.login.geometry('215x300')
        self.login.resizable(False, False)

        self.conn = database.connect_to_db('your_database_path.db')

        self.notebook = ttk.Notebook(login)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.create_customer_tab()

    def create_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(customer_tab, text="Customer")

        self.customerID_label = ttk.Label(customer_tab, text="Customer ID")
        self.customerID_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.customerID_entry = ttk.Entry(customer_tab)
        self.customerID_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.customerPass_label = ttk.Label(customer_tab, text="Password")
        self.customerPass_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.customerPass_entry = ttk.Entry(customer_tab, show="*")
        self.customerPass_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.submit_button = ttk.Button(customer_tab, text='Submit', width=10, command=self.submit_customer)
        self.submit_button.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    def submit_customer(self):
        customer_id = self.customerID_entry.get()
        password = self.customerPass_entry.get()

        # Check login credentials
        result = database.check_customer_login(self.conn, customer_id, password)
        if result:
            print("Login successful")
        else:
            print("Login failed. Invalid ID or password.")

    def __del__(self):
        if self.conn:
            database.close_connection(self.conn)
            self.conn = None

if __name__ == "__main__":
    login = tk.Tk()
    app = login_UI(login)
    login.mainloop()
