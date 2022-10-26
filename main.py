#from __future__ import print_function
import requests
from twilio.rest import Client
import config

#from telesign.messaging import MessagingClient

account_sid = config.account_sid
auth_token = config.auth_token
phone_number = config.phone_number
phone_to_send = config.phone_to_send
my_number = config.my_number
from_number = config.from_number
master_API = config.master_API

parameters = {
    "lat": 6.512990,
    "lon": 3.321320,
    "lang": "en",
    "hours": 48,
    "key": master_API,
}

response = requests.get(url="https://api.weatherbit.io/v2.0/forecast/hourly", params=parameters)
response.raise_for_status()

will_rain = False
weather_data = response.json()
for num in range(12):
    weather_code = weather_data["data"][num]["weather"]["code"]
    if weather_code < 700:
        will_rain = True
print(will_rain)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body="It's going to rain today 😩. Remember to bring an ⛱.\n Love you.",
                from_=from_number,
                to=phone_to_send
                )
    print(message.status)
