from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import pycountry
import requests
import json
from geopy.geocoders import Nominatim
import datetime 
from datetime import date

def get_coords(city):
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

def get_weather_dict(lat, lon):
    api_key = ""

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    #print(type(data)) #this is ALL the weather data lol. Literally all of it #very messy json. There are online formatters if you wish to view it
    return data

def process_weather_dict(wd):
    new_wd = {}
    wd = wd["daily"]

    for i in range(6):
        wdtemp = wd[i]
        cur = {}
        cur["date"] = wdtemp["dt"]
        cur["temp"] = wdtemp["temp"]["day"]
        cur["humidity"] = wdtemp["humidity"]
        cur["wind"] = wdtemp["wind_speed"]
        cur["uv"] = wdtemp["uvi"]
        cur["icon_code"] = wdtemp["weather"][0]["icon"]
        new_wd[i] = cur
    return new_wd

#put in a city name string and it'll spit out the weather data for today and the 5 after it.
def get_weather_data(city): #basically this function calls the 3 above it. 
    
    coords = get_coords(city)
    wd = get_weather_dict(coords[0], coords[1])
    wd = process_weather_dict(wd)
    return wd


#good for debugging and viewing our data in a decent format
""" 
for key in wd: #the key is the offset from the first day so it goes from 0-5 (0 being today and 5 being 5 days from today)
    day = wd[key]
    print("day: " , day)
    for key in day:
        print(key, ": " , day[key])
    print()
"""