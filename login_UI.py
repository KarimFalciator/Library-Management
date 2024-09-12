from tkinter import *

def login_UI():
    login = Tk()
    login.title = 'Login Screen'
    login.geometry = '400x200'
    login.resizable(False, False)
    
    userID_label = Label(login, text="UserID")
    userID_label.grid(row=1, column=0, padx=10, pady=20, sticky="W")

    password_label = Label(login, text="Password")
    password_label.grid(row=2, column=0, padx=10, pady=20, sticky="W")

    userID_entry = Entry(login, width="30")
    userID_entry.grid(row=1, column=1, padx=30, pady=20, sticky="E")

    password_entry = Entry(login, width="30", show='•')
    password_entry.grid(row=2, column=1, padx=30, pady=20, sticky="E")

    forgot_button = Button(login, text="forgot password", width=20)
    forgot_button.grid(row=3, column=1, padx=10, pady=10)

    submit_button = Button(login, text="Submit", width=20)
    submit_button.grid(row=3, column=2, padx=10, pady=10)

    Create_button = Button(login, text="New Account", width=20)
    Create_button.grid(row=3, column=0, padx=10, pady=10)

    mainloop()



if __name__ == "__main__":  # for testing
    login_UI()