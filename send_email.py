import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
USERNAME = "lola.berserker99@gmail.com"  # Replace with your email address
PASSWORD = "wujnitxzwzddayab"      # Replace with your email password
message = """
Subject: Github Email TEST CHECK

This is the test email.

Thanks!
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, USERNAME, message)  # From and TO
