import smtplib


def run(email, body1):
    sender = "TheToDoAppTeam2021@outlook.com"
    receiver = email
    password = "12345!@#$%qwertQWERT"
    subject = "Python"
    body = body1

    message = f'''From: {sender}
    To: {receiver}
    Subject: {subject} \n
    {body}
    '''

    server = smtplib.SMTP("smtp.outlook.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Email sent!")

    except smtplib.SMTPAuthenticationError:
        print("Unable to sign in...")
