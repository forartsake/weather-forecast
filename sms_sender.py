from twilio.rest import Client

account_sid = "Enter your account sid"
auth_token = "Enter your auth token"

client = Client(account_sid, auth_token)


def send_sms(message, number_from: str, number_to: str):
    """ Sends a sms to the given number when rain is expected"""
    client.messages.create(body=f"{message}", from_=number_from, to=number_to)
    print('SMS has been sent')
