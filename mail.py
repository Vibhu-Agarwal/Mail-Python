import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:

    def __init__(self, sender_id, sender_password):
        self.sender_email_id = sender_id
        self.sender_email_password = sender_password
        self.receiver_email_id = ""

        self.message_subject = "Default Subject"
        self.message_content = "This is a one liner message body"
        self.message = MIMEMultipart()

    def message_fill(self):
        self.message['From'] = self.sender_email_id
        self.message['To'] = self.receiver_email_id
        self.message['Subject'] = self.message_subject
        self.message.attach(MIMEText(self.message_content))

    def define_message(self, email_receiver, email_subject, email_content):
        self.receiver_email_id = email_receiver
        self.message_subject = email_subject
        self.message_content = email_content

    def send_email(self):
        if self.receiver_email_id == "":
            print("No receiver email Provided")
            return False

        try:
            email_connection = smtplib.SMTP('smtp.gmail.com', 587)
        except:
            print("Error in establishing connection")
            return False

        try:
            email_connection.starttls()
        except:
            print("Error in starting TLS")
            email_connection.quit()
            return False

        try:
            email_connection.login(self.sender_email_id, self.sender_email_password)
        except:
            print("Error in Logging in")
            email_connection.quit()
            return False

        self.message_fill()

        try:
            email_connection.sendmail(self.sender_email_id, self.receiver_email_id, self.message.as_string())
        except:
            print("Error in sending mail.")
            email_connection.quit()
            return False

        email_connection.quit()

        print("Email Sent!")
        return True
