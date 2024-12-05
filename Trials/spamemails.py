import smtplib
from email.message import EmailMessage

x = 0
for i in range(0, 1):
    sender_email = "karimfalciator@gmail.com"  # Your email address
    sender_password = "iveu rkbv tlwl edzc"  # Your email password

    # Create the email message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = EmailMessage()
    msg['Subject'] = 'Your OTP'
    msg['From'] = sender_email
    # msg['To'] = 'lahmarnour0@gmail.com'
    msg.set_content(f'suka blyat')

    # Send the email
    server.send_message(msg)
    server.quit()
    print(x)
    x =+ 1