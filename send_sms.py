import os
from twilio .rest import Client

account_sid = "AC2ef3b3f1129a5c58646cd19aee908ebf"
auth_token = "24c223d8c58749119ef0f2110387b74c"
client = Client(account_sid, auth_token)

message = client.messages.create(to='+17057617145',
                                 from_='+12262712087',
                                 body="Do you have SPECIAL trash")

print(message)
