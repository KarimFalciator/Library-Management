import tkinter as tk
from tkinter import ttk

def login_UI():

    login = tk.Tk()
    login.geometry('300x500')
    login.title('customer login')

    notebook = ttk.Notebook(login)
    notebook.pack(pady=0, expand=True)


    customer_tab = ttk.Frame(notebook, width=300, height=490)
    notebook.add(customer_tab, text='Customer Login')
    customerID_label = ttk.Label(customer_tab, text = 'User_ID')
    customerID_label.pack(padx=10, pady=10)
    customerID_entry = ttk.Entry(customer_tab, text = 'User_ID')
    customerID_entry.pack(padx=10, pady=20)


    librarian_tab = ttk.Frame(notebook, width=300, height=490)
    notebook.add(librarian_tab, text='Librarian Login')
    librarianID_label = ttk.Label(librarian_tab, text = 'Librarian_ID')
    librarianID_label.pack(padx=10, pady=10)

    notebook.pack(fill='both', expand=False)
    




    #librarian_id = ttk.Label(text = 'librarian_ID')




    tk.mainloop()






if __name__ == "__main__":  # for testing
    login_UI()