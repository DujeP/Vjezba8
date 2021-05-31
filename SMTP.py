import smtplib, ssl

port = 465
smtp_server = "smtp.mail.yahoo.com"
sender_email = "duje.popovic@yahoo.com"
receiver_email = "petrapopovic144@yahoo.com"
password = input("Unesite sifru: ")
message = """\
Subject: Dobar dan

Saljem vam poruku preko Pythona."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
