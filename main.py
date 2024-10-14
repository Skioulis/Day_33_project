from http.client import responses
from sqlite3.dbapi2 import paramstyle

import requests
from datetime import datetime

# MY_LAT = 39.360519
# MY_LNG = 22.945320
MY_LAT = 51.57
MY_LNG = 38

def is_between(a, x, b):
    return min(a, b) < x < max(a, b)

# Checks if iss is visible from my position

def check_position(current_lat, current_long):
    # if is_between(current_lat - 5, MY_LAT, current_lat + 5):
    #     print("lat Is between")
    # else:
    #     print("lat is not between")
    #
    # if is_between(current_long - 5, MY_LNG, current_long + 5):
    #     print("long Is between")
    # else:
    #     print("long is not between")
    #
    # if ((is_between(current_lat - 5, MY_LAT, current_lat + 5))
    #         and (is_between(current_long - 5, MY_LNG, current_long + 5))):
    #     print("It is Visible")
    # else:
    #     print ("Not visible")

    return ((is_between(current_lat - 5, MY_LAT, current_lat + 5))
            and (is_between(current_long - 5, MY_LNG, current_long + 5)))



parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


# This section get the iss current p[ostiont


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()


iss_lat=float(iss_data["iss_position"]["latitude"])
iss_long=float(iss_data["iss_position"]["longitude"])




# This section checks my sunset and sunrise at my location

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# (39.359008, 22.953859)
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])




time_now = datetime.now()


# to be deleted
print (iss_data["iss_position"])


print(check_position(iss_lat,iss_long))



