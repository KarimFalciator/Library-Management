import database
import smtplib
from email.message import EmailMessage

class follow_email:

    def __init__(self, t_id, s_email, ref, r_type, r_description, r_date):
        self.conn = database.connect_to_db('lending.db')
        self.t_id = t_id
        self.s_email = s_email
        self.ref = ref
        self.r_type = r_type
        self.r_description = r_description
        self.r_date = r_date

        self.send_l_email()

    def send_l_email(self):
        late_check = database.check_late(self.conn, self.ref) #have to create the function in database check if booked r_date is Null/None
        sender_email = "karimfalciator@gmail.com"  # later change to the email of the library
        sender_password = "iveu rkbv tlwl edzc"  # later change to the password of the library
        if late_check: 
            # Create the email message
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)

            msg = EmailMessage()
            msg['Subject'] = 'Borrowed Resource Due Date'
            msg['From'] = sender_email
            msg['To'] = self.s_email
            msg.set_content(f'Your {self.r_type, self.r_description} is due on {self.r_date}. Please return it on time to avoid any late fees.')

            # Send the email
            server.send_message(msg)
            server.quit()
        else:
            None

def main():
    follow_email(111111, 'karimfalciator@gmail.com', 1, 'camera', 'xyz', 222)

if __name__ == "__main__":
    main()