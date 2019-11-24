from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import trash
import send_sms

# Send address through this file

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])     # must this be closed?

def sms_reply():

    body = request.values.get('Body', None)
    contact = request.values.get('from', None)

    resp = MessagingResponse()

    # Recording Addresses
    """
    df = pd.read_csv("LondonAddressesDatabase.csv")
    address = df.loc[df['UnitFullAddress'] == str(body)]['Latitude'].values[0], df.loc[df['UnitFullAddress'] == str(body)]['Longitude'].values[0]
    """

    zone = None
    test = None

    if body == '50':
        send_sms.send_mes()
        resp.message("We've reached threshold. Send in the trucks!")

    else:

        zone, test = trash.zoneResponse(str(body))
        print(zone, test)


        resp.message("You are Zone: " + str(zone))

    return str(resp)

"""
in shell, run:

>python receive_sms.py
>ngrok http 5000
# paste url into Twilio console, a message comes in web hook, add "/sms" to end
"""
if __name__ == "__main__":
    app.run(debug=True)