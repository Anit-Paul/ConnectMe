import smtplib
from email.message import EmailMessage
import random

class Mail:
    def __init__(self):
        self.sender = 'meconnect474@gmail.com'
        self.password = 'lebv volk yzum jzjq'  # App password

    def send_email(self, receiver):
        otp = self.get_otp()  # You can replace this with self.get_otp()
        
        msg = EmailMessage()
        msg['Subject'] = 'Your Email Verification OTP'
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.set_content(f"""
Hi,

Here is your One-Time Password (OTP) for email verification:

    {otp}

Please do not share this code with anyone.

Best regards,
ConnectMe Team
""")

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(self.sender, self.password)
                connection.send_message(msg)
                return True
        except Exception as e:
            print("Error sending email:", e)
            return False

    def get_otp(self):
        s=""
        for i in range(4):
            s+=random.choice("0123456789")
        return s

