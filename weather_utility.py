from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import pycountry
import requests
import json
from geopy.geocoders import Nominatim
import datetime 

owm = OWM('')


def get_weather_dict_old(city):
    mgr = owm.weather_manager()
    input_country = "Canada"
    city = "charlotte"
    country = pycountry.countries.get(name=input_country)
    #a2_country = country.alpha_2

    observation = mgr.weather_at_place(city)
    uvmgr = owm.uvindex_manager()
    uvi = uvmgr.uvindex_around_coords(43.6532, 79.3832)

    w = observation.weather
    """
    #debugging stuff
    print("Location: " , city , ", " ,  input_country , "[" , a2_country , "]")
    print("Detailed status: " , w.detailed_status)         

    print("uvi: " , uvi.value) #CHECK #might be wrong lol, idk
    print("Wind: " , w.wind("meters_sec")) #it's in meters per second for some reason CHECK
    print("Humidity: " , w.humidity) #CHECK              
    print("Temp: " , w.temperature('celsius')) # CHECK
            
    print("Clouds" , w.clouds) #maybe important
    print("Rain: " , w.rain) #probably important?                    
    """
    
    wd = {} #weather dictionary
    wd["desc"] = w.detailed_status 
    wd["humidity"] = w.humidity
    wd["temp"] = w.temperature('celsius')["temp"] #in celsius

    wd["wind"] = w.wind("meters_sec")["speed"] #in meters/sec for some reason
    wd["uvi"] = uvi.value
    return wd

def get_coords(city):
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(city)
    #debuggin
    #print(location.address)
    #print(location.longitude)
    #print(location.latitude)
    return (location.longitude, location.latitude)

def get_weather_dict(lat, lon):
    wd = {}

    api_key = "55aa234ef58918da44065e2e0f9cd91c"

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lon, lat, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    #print(type(data)) #this is all the weather data lol. Literally all of it
    return data

def process_weather_dict(wd):
    new_wd = {}


    return new_wd

city = "toronto"
coords = get_coords(city)
wd = get_weather_dict(coords[0], coords[1])
#for key in wd:
#    print("Key: " , key , " Value: " , wd[key])

print("---------------------------------------")
print(wd)