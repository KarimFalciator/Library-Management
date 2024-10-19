import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("custom_theme.json")

class login_UI:

    def __init__(self, login):
        self.login = login
        self.login.title('Login')
        self.login.geometry('300x400')
        self.login.resizable(False, False)

        # Apply ttk Notebook style to match CustomTkinter appearance
        style = ttk.Style()
        style.theme_use('default')

        # Customizing the notebook tabs to match CustomTkinter
        style.configure('TNotebook', background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1])
        style.configure('TNotebook.Tab', font=('Arial', 12), padding=[10, 5], background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0])
        style.map("TNotebook.Tab", background=[("selected", ctk.ThemeManager.theme["CTkButton"]["fg_color"][1])])

        # Create a ttk Notebook, styled to match CustomTkinter
        self.notebook = ttk.Notebook(self.login)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Add customtkinter styled frames as tabs
        self.create_teacher_tab()
        self.create_help_tab()

    def create_teacher_tab(self):
        teacher_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(teacher_tab, text='Teacher Login')

        self.teacherID_label = ctk.CTkLabel(teacher_tab, text='Teacher ID')
        self.teacherID_label.pack(padx=10, pady=10)
        self.teacherID_entry = ctk.CTkEntry(teacher_tab)
        self.teacherID_entry.pack(padx=10, pady=5)

        self.teacherPass_label = ctk.CTkLabel(teacher_tab, text='Password')
        self.teacherPass_label.pack(padx=10, pady=5)
        self.teacherPass_entry = ctk.CTkEntry(teacher_tab, show='•')
        self.teacherPass_entry.pack(padx=10, pady=5)

        self.show_pass_button = ctk.CTkButton(teacher_tab, text='👁', width=4)
        self.show_pass_button.pack(padx=5, pady=5)

        self.show_pass_button.bind('<ButtonPress>', self.show_password_teacher)
        self.show_pass_button.bind('<ButtonRelease>', self.hide_password_teacher)

        self.submit_button = ctk.CTkButton(teacher_tab, text='Submit', width=10, command=self.submit_teacher)
        self.submit_button.pack(padx=5, pady=5)

    def submit_teacher(self):
        teacherID = self.teacherID_entry.get()
        teacherPass = self.teacherPass_entry.get()

        check = True  # Placeholder for actual login logic

        if check:
            success_label = ctk.CTkLabel(self.login, text='Login Successful', foreground='#009B0F', font=('Arial', 13))
            success_label.pack(pady=5)
            self.login.after(3500, self.login.destroy)
        else:
            error_label = ctk.CTkLabel(self.login, text='Invalid ID or password', foreground='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            self.login.after(7000, error_label.destroy)

    def show_password_teacher(self, event):
        self.teacherPass_entry.configure(show='')

    def hide_password_teacher(self, event):
        self.teacherPass_entry.configure(show='•')

    def create_help_tab(self):
        help_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(help_tab, text='Help')

        self.help_label = ctk.CTkLabel(help_tab, text="help")
        self.help_label.pack(padx=20, pady=20)

		# help combo box
        self.help_optionmenu = ctk.CTkOptionMenu(help_tab, values=["Student", "Working Professional"])
        self.help_optionmenu.pack(padx=20, pady=20)


        # self.help_label = ctk.CTkLabel(help_tab, text='Unable to login?')
        # self.help_label.pack(padx=10, pady=10)

        # self.create_account_button = ctk.CTkButton(help_tab, text='Create a new Account', width=22)
        # self.create_account_button.pack(padx=10, pady=10)

        # self.t_Reset_button = ctk.CTkButton(help_tab, text='Teacher Reset Password', width=22)
        # self.t_Reset_button.pack(padx=10, pady=10)

if __name__ == "__main__":  # for testing
    login = ctk.CTk()
    log = login_UI(login)
    login.mainloop()