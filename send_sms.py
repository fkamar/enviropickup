import os
from twilio .rest import Client

account_sid = "******"
auth_token = "******"
client = Client(account_sid, auth_token)

message = client.messages.create(to='insert number',
                                 from_='EnviroPickupNumber',
                                 body="Do you have SPECIAL trash")

print(message)
