import customtkinter as ctk
from tkinter import ttk
import database
import smtplib
from email.message import EmailMessage
import random
import string

class reset_password_UI:

    def __init__(self, reset):
        self.reset = reset
        self.reset.title('Reset Password')
        self.reset.geometry('300x400')
        self.reset.resizable(False, False)

        self.conn = database.connect_to_db('lending.db')

        # Apply ttk Notebook style to match CustomTkinter appearance
        style = ttk.Style()
        style.theme_use('default')

        # Customizing the notebook tabs to match CustomTkinter
        style.configure('TNotebook', background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1])
        style.configure('TNotebook.Tab', font=('Arial', 12), padding=[10, 5], background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0])
        style.map("TNotebook.Tab", background=[("selected", ctk.ThemeManager.theme["CTkButton"]["fg_color"][1])])

        # Create a ttk Notebook, styled to match CustomTkinter
        self.notebook = ttk.Notebook(self.reset)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Add customtkinter styled frames as tabs
        self.create_teacher_tab()
        self.create_otp_tab()
    
    def create_teacher_tab(self):
        teacher_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(teacher_tab, text='Teacher')

        self.teacherID_label = ctk.CTkLabel(teacher_tab, text='Teacher Id')
        self.teacherID_label.pack(padx=10, pady=10)
        self.teacherID_entry = ctk.CTkEntry(teacher_tab)
        self.teacherID_entry.pack(padx=10, pady=5)

        self.teacher_email_label = ctk.CTkLabel(teacher_tab, text='Email')
        self.teacher_email_label.pack(padx=10, pady=5)
        self.teacher_email_entry = ctk.CTkEntry(teacher_tab)
        self.teacher_email_entry.pack(padx=10, pady=5)

        self.submit_button = ctk.CTkButton(teacher_tab, text='Send Email', width=10, command=lambda: self.submit_t_email())
        self.submit_button.pack(padx=5, pady=5)

    def submit_t_email(self):
        t_id = self.teacherID_entry.get()
        t_email = self.teacher_email_entry.get()

        teacher = database.check_t_email(self.conn, t_id, t_email)

        if teacher:
            self.otp = self.generate_otp()
            self.send_t_email(t_id, t_email, self.otp)
            self.success_label = ctk.CTkLabel(self.reset, text='Reset Successful', text_color='#009B0F', font=('Arial', 13))
            self.success_label.pack(pady=5)
            self.reset.after(3500, self.success_label.destroy)
        else:
            error_label = ctk.CTkLabel(self.reset, text='Invalid ID or password', text_color='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            self.reset.after(7000, error_label.destroy)

    def generate_otp(self):
        otp = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return otp

    def send_t_email(self, t_id, receiver_email, otp):
        sender_email = "karimfalciator@gmail.com"  # Your email address
        sender_password = "iveu rkbv tlwl edzc"  # Your email password

        # Create the email message
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # login to the server
        server.login(sender_email, sender_password)

        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = 'Your OTP'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # write the OTP in the email message
        msg.set_content(f'Your OTP is {otp}')

        # Send the email
        server.send_message(msg)
        server.quit()

        
    def create_otp_tab(self):
        otp_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(otp_tab, text='OTP Verify')

        self.otp_label = ctk.CTkLabel(otp_tab, text='confirm otp sent by email')
        self.otp_label.pack(padx=10, pady=10)
        self.otp_entry = ctk.CTkEntry(otp_tab)
        self.otp_entry.pack(padx=10, pady=5)

        self.submit_button = ctk.CTkButton(otp_tab, text='Submit', width=10, command=self.verify_otp)
        self.submit_button.pack(padx=5, pady=5)

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == self.otp:
            self.reset_pass_window()
        else:
            error_label = ctk.CTkLabel(self.notebook, text='Invalid OTP', text_color='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            self.after(7000, error_label.destroy)

    def reset_pass_window(self):
        self.reset_window = ctk.CTkToplevel(self.reset)
        self.reset_window.title("Reset Password")
        self.reset_window.geometry("300x200")

        self.pass_label = ctk.CTkLabel(self.reset_window, text="Enter Password.")
        self.pass_label.pack(padx=10, pady=10)
        self.pass_entry = ctk.CTkEntry(self.reset_window)
        self.pass_entry.pack(padx=10, pady=5)

        self.passconfirm_label = ctk.CTkLabel(self.reset_window, text="Confirm Password.")
        self.passconfirm_label.pack(padx=10, pady=10)
        self.passconfirm_entry = ctk.CTkEntry(self.reset_window)
        self.passconfirm_entry.pack(padx=10, pady=5)

        self.submit_button = ctk.CTkButton(self.reset_window, text='Submit', width=10, command=self.reset_password)
        self.submit_button.pack(padx=5, pady=5)

    def reset_password(self):
        new_password = self.pass_entry.get()
        confirm_password = self.passconfirm_entry.get()
        if new_password == confirm_password:
            database.update_teacher_password(self.conn, self.teacherID_entry.get(), new_password)
            self.success_label = ctk.CTkLabel(self.reset, text='Password Reset Successful', text_color='#009B0F', font=('Arial', 13))
            self.success_label.pack(pady=5)
            self.reset.after(3500, self.success_label.destroy)
        else:
            error_label = ctk.CTkLabel(self.reset, text='Passwords do not match', text_color='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            self.reset.after(7000, error_label.destroy)


# if __name__ == "__main__":  # for testing
#     reset = ctk.CTk()
#     log = reset_password_UI(reset)
#     reset.mainloop()
    