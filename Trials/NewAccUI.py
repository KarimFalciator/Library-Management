import tkinter as tk
from tkinter import ttk
import database  # Import the database module

class CreateAccUI:

    def __init__(self, new):
        self.new = new
        self.new.title('New Account')
        self.new.geometry('400x500')
        self.new.resizable(False, False)

        self.conn = database.connect_to_db()

        self.notebook = ttk.Notebook(new)
        self.notebook.pack(pady=0, expand=True, fill='both')

        self.newAcc_customer_tab()
        

    def newAcc_customer_tab(self):
        customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(customer_tab, text="Customer")

        self.firstname_label = ttk.Label(customer_tab, text="First Name")
        self.firstname_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.firstname_entry = ttk.Entry(customer_tab)
        self.firstname_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.surname_label = ttk.Label(customer_tab, text="Surname")
        self.surname_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.surname_entry = ttk.Entry(customer_tab)
        self.surname_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.email_label = ttk.Label(customer_tab, text="Email")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.email_entry = ttk.Entry(customer_tab)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.address_label = ttk.Label(customer_tab, text="Address")
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.address_entry = ttk.Entry(customer_tab)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.customerPass_label = ttk.Label(customer_tab, text="Password")
        self.customerPass_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.customerPass_entry = ttk.Entry(customer_tab, show="*")
        self.customerPass_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.submit_button = ttk.Button(customer_tab, text='Create', width=10, command=self.new_customer_record)
        self.submit_button.grid(row=7, column=0, padx=5, pady=5, sticky='w')

    def new_customer_record(self):
        password = self.customerPass_entry.get()
        first_name = self.firstname_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        # Insert new customer data into the database
        database.new_customer(self.conn, password, first_name, surname, email, address)
        print("New customer account created.")
        self.new.destroy()

    def __del__(self):
        database.close_connection(self.conn)

if __name__ == "__main__":
    new = tk.Tk()
    app = CreateAccUI(new)
    new.mainloop()
