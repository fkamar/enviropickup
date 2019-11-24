from twilio.rest import Client

# Confirmation sent through this file
def send_mes():
    account_sid = "ACfd1b44eac82dc1894035f5b86b967c48"
    auth_token = "16f4cc09309c0ef7ea3773d35a8826cd"

    client = Client(account_sid, auth_token)

    numbers = {'Brian Qian':'+16477708436', 'Farah': '+17057617145'}
    # client.messages.create(to="+16477708436", from_="+16475592146", body= "Message to London")

    for name, number in numbers.items():
            message = client.messages.create(
                to=number,
                from_="+16475592146",
                body="Hi " + name + ", your garbage is scheduled for pick-up for tomorrow at 9:00 am!\n" + "Your garbage zone is Zone " + str(zone))
            print(message.sid)
"""
>python send_sms.py
"""