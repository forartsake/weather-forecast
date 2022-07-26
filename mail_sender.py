import smtplib

mail = 'Enter your main mail'
password = 'Enter your pass'
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mail, password=password)


def send_email(from_mail: str, to_mail: str, message):
    """Sends an email when rain is expected"""
    connection.sendmail(from_addr=from_mail, to_addrs=to_mail,
                        msg="Subject:Weather forecast\n\n"
                            f"Take an umbrella. Rain is expected:  {message}")
    print("E-mail has been sent")
    connection.close()
