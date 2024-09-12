from tkinter import *

def main_UI():
    main_screen = Tk()
    main_screen.title = 'Main Screen'
    main_screen.geometry = '400x200'
    main_screen.resizable(False, False)

    name_label = Label(main_screen, text="Username")
    name_label.grid(row=1, column=0, padx=10, pady=20, sticky="W")

    password_label = Label(main_screen, text="Password")
    password_label.grid(row=2, column=0, padx=10, pady=20, sticky="W")

    name_entry = Entry(main_screen, width=30)
    name_entry.grid(row=1, column=1, padx=30, pady=20, sticky="E")

    password_entry = Entry(main_screen, width=30, show='•')
    password_entry.grid(row=2, column=1, padx=30, pady=20, sticky="E")

    forgot_button = Button(main_screen, text="forgot password", width=20)
    forgot_button.grid(row=3, column=1, padx=10, pady=10)

    submit_button = Button(main_screen, text="Submit", width=20)
    submit_button.grid(row=3, column=2, padx=10, pady=10)

    mainloop()



    mainloop()

main_UI()