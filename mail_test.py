from mail import Mail
from getpass import getpass

sender = input("Sender ID: ")
sender_password = getpass(prompt="Sender Password: ")

mailing = Mail(sender, sender_password)

receiver = input("Receiver ID: ")
email_subject = "Email Subject"
email_content = """
Line1
Line2
Line3
Line4
Line5
"""

mailing.define_message(receiver, email_subject, email_content)

mailing.send_email()
