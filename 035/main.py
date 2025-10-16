import requests
from twilio.rest import Client
import os


account_sid = os.getenv("ACCOUNT_SID") 
auth_token = os.getenv("AUTH_TOKEN")

api_key = os.getenv("API_KEY")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lon":10.412990,
    "lat":5.485660,
    "appid": api_key,
}
response = requests.get(OWM_endpoint, params= weather_params)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)

if weather_data['weather'][0]['id'] < 700 :
    print("BRING YOUR UMBRELLA")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= 'It will rain today, take your umbrella',
        from_='+19378602474',
        to = "+237673279934"
    )
    print(message.status)