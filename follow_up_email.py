import database
import smtplib
from email.message import EmailMessage

class follow_email:

    def __init__(self, t_id, s_id, s_email, ref):
        self.conn = database.connect_to_db('lending.db')
        self.t_id = t_id
        self.s_id = s_id
        self.s_email = s_email
        self.ref = ref

    def submit_t_email(self):
        s_email_check = database.check_s_email(self.conn, self.s_id, self.s_email)
        late_check = database.check_late(self.conn, self.ref) #have to create the function in database check if booked r_date is Null/None
        




        if s_email_check:
            self.otp = self.generate_otp()
            self.send_t_email(t_id, t_email)
        else:
            None

    def send_t_email(self, s_id, receiver_email):
        sender_email = "karimfalciator@gmail.com"  # later change to the email of the library
        sender_password = "iveu rkbv tlwl edzc"  # later change to the password of the library

        # Create the email message
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        msg = EmailMessage()
        msg['Subject'] = 'Borrowed Resource Due Date'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(f'Your OTP is {'otp'}')

        # Send the email
        server.send_message(msg)
        server.quit()

    def follow_password(self):
        t_id = self.teacherID_entry.get()
        new_password = self.pass_entry.get()
        confirm_password = self.passconfirm_entry.get()

        if new_password == confirm_password and new_password != '':
            database.update_teacher_password(self.conn, t_id, new_password)
        else:
            None
