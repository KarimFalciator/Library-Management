import customtkinter as ctk
from tkinter import ttk
import database
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        self.create_students_tab()
    
    def create_teacher_tab(self):
        teacher_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(teacher_tab, text='Teacher')

        self.teacherID_label = ctk.CTkLabel(teacher_tab, text='Teacher Id')
        self.teacherID_label.pack(padx=10, pady=10)
        self.teacherID_entry = ctk.CTkEntry(teacher_tab)
        self.teacherID_entry.pack(padx=10, pady=5)

        self.student_email_label = ctk.CTkLabel(teacher_tab, text='Email')
        self.student_email_label.pack(padx=10, pady=5)
        self.student_email_entry = ctk.CTkEntry(teacher_tab)
        self.student_email_entry.pack(padx=10, pady=5)

        self.submit_button = ctk.CTkButton(teacher_tab, text='Send Email', width=10, command=lambda: self.submit_t_email())
        self.submit_button.pack(padx=5, pady=5)

    def submit_t_email(self):
        t_ID = self.teacherID_entry.get()
        t_email = self.student_email_entry.get()

        teacher = database.check_t_email(self.conn, t_ID, t_email)

        if teacher:
            send_t_email = send_t_email()
            success_label = ctk.CTkLabel(self.login, text='Login Successful', text_color='#009B0F', font=('Arial', 13))
            success_label.pack(pady=5)
            self.login.after(3500, self.login.destroy)
        else:
            error_label = ctk.CTkLabel(self.login, text='Invalid ID or password', text_color='#FF0400', font=('Arial', 13))
            error_label.pack(pady=5)
            self.login.after(7000, error_label.destroy)

    def send_t_email(self):
        sender_email = "karimfalciator@gmail.com"  # Your email address
        sender_password = "Lepassword1"  # Your email password
        receiver_email = "karimfalciator@example.com"  # Recipient's email address

        # Create the email subject and body
        subject = "Test Reset Password Email"
        body = "This is a test email sent from Python!"

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the Gmail SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Log in to your account
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")

        
    def create_students_tab(self):
        student_tab = ctk.CTkFrame(self.notebook, width=300, height=400)
        self.notebook.add(student_tab, text='Student')

        self.studentID_label = ctk.CTkLabel(student_tab, text='Student ID')
        self.studentID_label.pack(padx=10, pady=10)
        self.studentID_entry = ctk.CTkEntry(student_tab)
        self.studentID_entry.pack(padx=10, pady=5)

        self.student_email_label = ctk.CTkLabel(student_tab, text='Email')
        self.student_email_label.pack(padx=10, pady=5)
        self.student_email_entry = ctk.CTkEntry(student_tab)
        self.student_email_entry.pack(padx=10, pady=5)

        self.submit_button = ctk.CTkButton(student_tab, text='Submit', width=10, command=lambda: self.submit_s_email())
        self.submit_button.pack(padx=5, pady=5)

    def submit_s_email(self):
        teacherID = self.teacherID_entry.get()
        email = self.student_email_entry.get()
        database.send_reset_email(self.conn, teacherID, email)

if __name__ == "__main__":  # for testing
    reset = ctk.CTk()
    log = reset_password_UI(reset)
    reset.mainloop()
    