# this progran print live location of the internation space station ISS

import requests
import json


url = "http://api.open-notify.org/iss-now.json"


get_location = requests.get(url)
get_location.raise_for_status()
data = get_location.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
timestamp = data['timestamp']
message = data['message']
print(f"ISS current location is {timestamp}, its latitude is {latitude}, and its longitude is {longitude} ")


#    2nd method by using def function






def iss_location():
    url = "http://api.open-notify.org/iss-now.json"


    get_location = requests.get(url)
    get_location.raise_for_status()
    data = get_location.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    message = data['message']
    print(f"ISS current location is {timestamp}, its latitude is {latitude}, and its longitude is {longitude} ")

iss_location()





