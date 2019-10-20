"""
See more on:
    https://realpython.com/python-send-email/

Terminology:
    SMTP: Simple Mail Transfer Protocal
    SSL: Secure Sockets Layer
    TLS: Transport Layer Security
    MIME: Multipurpose Internet Mail Extensions 

SSL and TLS are two protocols that can be used to encrypt an SMTP connection.
"""
import email
import getpass
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = "*@gmail.com"
RECEIVER = ["*@gmail.com"]


class Email:
    def __init__(self, sender_email, receiver_email, smtp_server="smtp.gmail.com"):

        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server

    def sendemail(self, message, ssl=True):
        """
        There are two ways to start a secure connection with your email server:
            1. Start an SMTP connection that is secured from the beginning using SMTP_SSL().
            2. Start an unsecured SMTP connection that can then be encrypted using .starttls().
        """
        context = ssl.create_default_context()
        password = getpass.getpass()
        if ssl:
            port = 465
            with smtplib.SMTP_SSL(self.smtp_server, port, context=context) as server:
                server.login(self.sender_email, password)
                server.sendmail(self.sender_email, self.receiver_email, message)
        else:
            port = 587
            with smtplib.SMTP(self.smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.sender_email, password)
                server.sendmail(self.sender_email, self.receiver_email, message)

    def createmessage(self, subject):

        message = MIMEMultipart("alternative")
        message["Subject"] = subject  # "multipart test"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Bcc"] = self.receiver_email  # Recommended for mass emails

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""

        html = """\
        <html>
        <body>
            <p>Hi,<br>
            How are you?<br>
            <a href="http://www.realpython.com">Real Python</a> 
            has many great tutorials.
            </p>
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        return message.as_string()


if __name__ == "__main__":

    subject = "test email"

    email = Email(SENDER, RECEIVER)
    msg = email.createmessage(subject=subject)
    email.sendemail(msg)
