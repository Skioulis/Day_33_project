from http.client import responses
from sqlite3.dbapi2 import paramstyle

import requests
from datetime import datetime

MY_LAT = 39.359008
MY_LNG = 22.953859

# response = requests.get(url="https://api.kanye.rest")
#
#
# print(response.json()["quote"])

# longitude = response.json()["iss_position"]["longitude"]


# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)
# print(iss_position[1])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


# This section get the iss current p[ostiont


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


iss_lat=float(data["iss_position"]["latitude"])
iss_long=float(data["iss_position"]["longitude"])



# This section checks my sunset and sunrise at my location

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# (39.359008, 22.953859)
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()

