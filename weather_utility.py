from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import pycountry

owm = OWM('')
mgr = owm.weather_manager()

def get_weather_dict(city):
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
