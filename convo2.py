from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio .rest import Client

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    counter=48
    contact1=''
    while counter < 50:
        """Send a dynamic reply to an incoming text message"""
        # Get the message the user sent our Twilio number
        body = request.values.get('Body', None)
        contact = request.values.get('from')

        # Start our TwiML response
        resp = MessagingResponse()

        # Determine the right reply for this message
        if body == 'Hi' or body == 'Hello' or body == 'Hi!' or body == 'Hello!' or body == 'Hi ' or body == 'Hello':
            resp.message("Thank you for reaching out to EnviroPickup! Do you have any non-collectible garbage you would like us to pick-up? (Please consult http://www.london.ca/residents/Garbage-Recycling/Garbage/Pages/default.aspx for what the City of London constitutes as Special Waste)")
        elif body == 'Yes' or body == 'yes' or body == 'Yes ' or body == 'yes ':
            resp.message("What is your address?")
        elif body == 'No' or body == 'no' or body == 'No ' or body == 'no ':
            resp.message("Sorry we can not help you, but please refer to our website for more information about our collection dates/locations! :)")
        else:
            resp.message("Thank you for letting us now. We will text you when we send a truck to your house. Have a great day!")
            address = body
            if counter == 48:
                contact1=contact
            if contact!=contact1:
                counter += 1
        return str(resp)
    
    else:
        resp1 = MessagingResponse()
        outgoing_sms(contact1)
        resp1.message(body)
        return str(resp1)        
        resp2 = MessagingResponse()
        outgoing_sms(contact)
        resp2.message(body)
        return str(resp2)
        counter=48

def outgoing_sms(f):
    account_sid = "AC2ef3b3f1129a5c58646cd19aee908ebf"
    auth_token = "24c223d8c58749119ef0f2110387b74c"
    client = Client(account_sid, auth_token)

    replyText = client.messages.create(to= f,
                                     from_='+12262712087',
                                     body="Your garbage will be picked up today! Please place it on the curb :)")
    return str(replyText)

if __name__ == "__main__":
    app.run(debug=True)
    
