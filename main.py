import requests
from datetime import datetime

MY_LAT = 50.114422
MY_LONG = 19.063950

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
needed_lat = 45.000000
needed_lat1 = 55.000000
needed_long = 14.000000
needed_long1 = 24.000000

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if iss_latitude > 45 and iss_latitude < 55:
    if iss_longitude > 14 and iss_longitude < 24:
        if time_now.hour > sunset and time_now.hour < sunrise:
            print("lookup")




