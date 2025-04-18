import customtkinter as ctk
from tkinter import ttk
import database
import reset_password
from main_ui import main_UI
from newacc_ui import CreateAccUI
from encription import hash_password
import json
import os

class login_UI:

    def __init__(self, login):
        self.login = login

        if os.path.exists('saved_settings.json'):
            with open('saved_settings.json', 'r') as file:
                settings = json.load(file)
        else:
            with open('default_settings.json', 'r') as file:
                settings = json.load(file)

        self.font = settings['Font']
        self.font_size = int(settings["Font_size"])
        self.theme = settings["Theme"]
        self.zoom = max(0.5, min(float(settings["Zoom"]), 3))

        width = int(300 * self.zoom)
        height = int(400 * self.zoom)

        self.login.title('Login')
        self.login.geometry(f'{width}x{height}')
        self.login.resizable(False, False)

        ctk.set_appearance_mode(self.theme)
        ctk.set_default_color_theme("blue")

        self.conn = database.connect_to_db('lending.db')

        # Apply ttk Notebook style to match CustomTkinter appearance
        style = ttk.Style()
        style.theme_use('default')

        # Customizing the notebook tabs to match CustomTkinter
        style.configure('TNotebook', background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1])
        style.configure('TNotebook.Tab', font=(self.font, self.font_size), padding=[10, 5], background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0])
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

        self.teacherID_label = ctk.CTkLabel(teacher_tab, text='Teacher ID', font=(self.font, self.font_size))
        self.teacherID_label.pack(padx=10, pady=10)
        self.teacherID_entry = ctk.CTkEntry(teacher_tab, font=(self.font, self.font_size))
        self.teacherID_entry.pack(padx=10, pady=5)

        self.teacherPass_label = ctk.CTkLabel(teacher_tab, text='Password', font=(self.font, self.font_size))
        self.teacherPass_label.pack(padx=10, pady=5)
        self.teacherPass_entry = ctk.CTkEntry(teacher_tab, show='•', font=(self.font, self.font_size))
        self.teacherPass_entry.pack(padx=10, pady=5)

        # Use the button for holding password visibility
        self.show_pass_button = ctk.CTkButton(teacher_tab, text='👁', font=(self.font, self.font_size), width=4, command=lambda: self.toggle_password(True))
        self.show_pass_button.pack(padx=5, pady=5)
        
        # Bind <ButtonRelease-1> to hide the password
        self.show_pass_button.bind('<ButtonRelease-1>', lambda event: self.toggle_password(False))

        self.submit_button = ctk.CTkButton(teacher_tab, text='Submit', font=(self.font, self.font_size), width=10, command=lambda: self.submit_teacher())
        self.submit_button.pack(padx=5, pady=5)

    def submit_teacher(self):
        teacherID = self.teacherID_entry.get()
        teacherPass = self.teacherPass_entry.get()
        teacherPass = hash_password(self.teacherPass_entry.get())
        print(teacherPass)

        check = database.check_teacher_login(self.conn, teacherID, teacherPass)

        if check:
            print('Login Successful')
            success_label = ctk.CTkLabel(self.login, text='Login Successful', text_color='#009B0F', font=(self.font, self.font_size))
            success_label.pack(pady=5)

     
            # Open main UI
            main_UI(ctk.CTk(), teacherID)

            # Properly destroy the login window
            self.login.destroy()
        else:
            error_label = ctk.CTkLabel(self.login, text='Invalid ID or password', text_color='#FF0400', font=(self.font, self.font_size))
            error_label.pack(pady=5)

            # Schedule error message removal and store the callback ID
            self.error_callback_id = self.login.after(7000, error_label.destroy)

    def toggle_password(self, show):
        if show:
            self.teacherPass_entry.configure(show='')  # Show password
        else:
            self.teacherPass_entry.configure(show='•')  # Hide password

    def create_help_tab(self):
        help_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(help_tab, text='Help')

        self.help_label = ctk.CTkLabel(help_tab, text="help", font=(self.font, self.font_size))
        self.help_label.pack(padx=20, pady=20)

        self.help_label = ctk.CTkLabel(help_tab, text='Unable to login?', font=(self.font, self.font_size))
        self.help_label.pack(padx=10, pady=10)

        self.t_Reset_button = ctk.CTkButton(help_tab, text='Reset Password', font=(self.font, self.font_size), width=22, command=self.reset_teacher_password)
        self.t_Reset_button.pack(padx=10, pady=10)

        self.t_new_button = ctk.CTkButton(help_tab, text='New Account', font=(self.font, self.font_size), width=22, command=self.new_teacher_account)
        self.t_new_button.pack(padx=10, pady=10)

        self.help_label = ctk.CTkLabel(help_tab, text='Contact your manager', font=(self.font, self.font_size))
        self.help_label.pack(padx=10, pady=10)

    def new_teacher_account(self):
        self.login.destroy()
        newacc_window = ctk.CTkToplevel()
        ctk.set_appearance_mode(self.theme)
        CreateAccUI(newacc_window)

        
    def reset_teacher_password(self):
        self.login.destroy()
        reset_window = ctk.CTkToplevel()  # Create a Toplevel window for reset password
        ctk.set_appearance_mode(self.theme)  # Keep the same appearance mode
        reset_password.reset_password_UI(reset_window)  # Pass the new window to the reset password UI


if __name__ == "__main__":  # for testing
    login = ctk.CTk()
    log = login_UI(login)
    login.mainloop()