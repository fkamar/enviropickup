# enviropickup
A sustainable solution for your trash.

addressDatabase.py generates the LondonAddressesDatabase.csv file which contains the data from the Open Portal system that is transformed for our use. 

trash-2.py is the algorithm used to tabulate the number of residents with specialized garbage by finding the zone of the address they text to the EnviroPickup number

receive_sms.py contains the code for the Twilio API to know how to respond to incoming texts while send_sms.py supports this file.
