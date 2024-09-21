import tkinter as tk
from tkinter import ttk

def login_UI():

    login = tk.Tk()
    login.geometry('275x450')
    login.title('Login Page')

    notebook = ttk.Notebook(login)
    notebook.pack(pady=0, expand=True)

#customer tab ---------------------------------------------------------------

    customer_tab = ttk.Frame(notebook, width=300, height=490)
    notebook.add(customer_tab, text='Customer Login')

    customerID_label = ttk.Label(customer_tab, text = 'User ID')
    customerID_label.pack(padx=10, pady=5)
    customerID_entry = ttk.Entry(customer_tab)
    customerID_entry.pack(padx=10, pady=5)

    customerPass_label = ttk.Label(customer_tab, text = 'Password')
    customerPass_label.pack(padx=10, pady=5)
    customerPass_entry = ttk.Entry(customer_tab, show= '•')
    customerPass_entry.pack(padx=10, pady=5)

#show password button

    def show_password(event):
        customerPass_entry.config(show='')
        

    def hide_password(event):
        customerPass_entry.config(show='•')

    show_pass_button = ttk.Button(customer_tab, text='👁', width=4)
    show_pass_button.pack(padx=5, pady=5)
    show_pass_button.bind('<ButtonPress-1>', show_password)
    show_pass_button.bind('<ButtonRelease-1>', hide_password)

#help frame

    help_frame = ttk.Frame(customer_tab)
    help_frame.pack(padx=10, pady=10, fill='both', expand=True)

    ForgotPass_Button = ttk.Button(help_frame, text='Reset Password', width=15)
    ForgotPass_Button.pack(padx=10, pady=5)
    
    NewAcc_Button = ttk.Button(help_frame, text='Create Account', width=15)
    NewAcc_Button.pack(padx=10, pady=5)

#librarian tab --------------------------------------------------------------

    librarian_tab = ttk.Frame(notebook, width=300, height=490)
    notebook.add(librarian_tab, text='Librarian Login')

    librarianID_label = ttk.Label(librarian_tab, text = 'Librarian ID')
    librarianID_label.pack(padx=10, pady=10)
    librarianID_entry = ttk.Entry(librarian_tab)
    librarianID_entry.pack(padx=10, pady=5)

    librarianPass_label = ttk.Label(librarian_tab, text = 'Password')
    librarianPass_label.pack(padx=10, pady=5)
    librarianPass_entry = ttk.Entry(librarian_tab, show= '•')
    librarianPass_entry.pack(padx=10, pady=5)

#show password button

    def show_password(event):
        librarianPass_entry.config(show='')

    def hide_password(event):
        librarianPass_entry.config(show='•')

    show_pass_button = ttk.Button(librarian_tab, text='👁', width=4)
    show_pass_button.pack(padx=5, pady=5)
    show_pass_button.bind('<ButtonPress-1>', show_password)
    show_pass_button.bind('<ButtonRelease-1>', hide_password)

#help frame

    help_frame = ttk.Frame(librarian_tab)
    help_frame.pack(padx=10, pady=10, fill='both', expand=True)

    ForgotPass_Button = ttk.Button(help_frame, text='Reset Password', width=15)
    ForgotPass_Button.pack(padx=10, pady=5)
    
    NewAcc_Button = ttk.Button(help_frame, text='Create Account', width=15)
    NewAcc_Button.pack(padx=10, pady=5)




    notebook.pack(fill='both', expand=False)




    tk.mainloop()






if __name__ == "__main__":  # for testing
    login_UI()