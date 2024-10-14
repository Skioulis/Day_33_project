from http.client import responses
from sqlite3.dbapi2 import paramstyle
from xml.etree.ElementTree import tostring

import requests
from datetime import datetime

# MY_LAT = 39.360519
# MY_LNG = 22.945320
MY_LAT = 51.57
MY_LNG = 38

def is_between(a, x, b):
    return min(a, b) < x < max(a, b)

# Checks if iss is visible from my position

def check_position():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    print(iss_data["iss_position"]) # to be DELETED

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])

    return ((is_between(iss_lat - 5, MY_LAT, iss_lat + 5))
            and (is_between(iss_long - 5, MY_LNG, iss_long + 5)))








# This section get the iss current p[ostiont







# This section checks my sunset and sunrise at my location
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    # (39.359008, 22.953859)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now<= sunrise:
        print("is night") # to be DELETED
        return True
    else:
        print("is Day") # to be DELETED
        return False





# to be deleted



if check_position() and is_night() :
    print("look UP")

else:
    print("cant see")



