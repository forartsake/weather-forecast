import requests
import datetime

LATITUDE = 48.208176
LONGITUDE = 14.552812

api_key = 'Enter your api open weather key'
endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': 48.208176,
    'lon': 14.552812,
    'exclude': 'current,minutely,daily',
    'appid': api_key
}

response = requests.get(url=endpoint, params=parameters)
# raise an exception whether something goes wrong
response.raise_for_status()

data = response.json()
# shows the weather forecast for the next twelve hours (prints the result only in case of rain)
message = {}
for hour in range(12):
    if data['hourly'][hour]['weather'][0]['id'] < 600:
        time = datetime.datetime.fromtimestamp(data['hourly'][hour]['dt']).strftime('%Y-%m-%d %H:%M:%S')
        description = data['hourly'][hour]['weather'][0]['description']
        message[time] = description
