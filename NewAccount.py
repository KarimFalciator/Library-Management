from tkinter import *


def login_UI():
    login = Tk()
    login.title = 'New Account'
    login.geometry = '400x200'
    login.resizable(False, False)

    userID_label = Label(login, text= database.userid)
    userID_label.grid(row=1, column=0, padx=10, pady=20, sticky="W")

    userID_label = Label(login, text="Your New User ID")
    userID_label.grid(row=1, column=1, padx=10, pady=20, sticky="W")

    password_label = Label(login, text="Password")
    password_label.grid(row=2, column=0, padx=10, pady=20, sticky="W")

    userID_label = Label(login, text="Username")
    userID_label.grid(row=1, column=0, padx=10, pady=20, sticky="W")

    password_entry = Entry(login, width="30", show='•')
    password_entry.grid(row=2, column=1, padx=30, pady=20, sticky="E")

    submit_button = Button(login, text="Done", width=20)
    submit_button.grid(row=3, column=2, padx=10, pady=10)


    mainloop()

login_UI()