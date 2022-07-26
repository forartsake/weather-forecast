import sms_sender
import mail_sender
from weather import message

if __name__ == '__main__':
    send_from = 'Enter a phone number'
    send_to = 'Enter a phone number'
    my_email = 'Enter an email'
    to_email = 'Enter an email'
    sms_sender.send_sms(number_from=send_from, number_to=send_to, message=message)
    mail_sender.send_email(from_mail=my_email, to_mail=to_email, message=message)
