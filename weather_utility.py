from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('')
mgr = owm.weather_manager()


observation = mgr.weather_at_place('Toronto, CA')

uvmgr = owm.uvindex_manager()
uvi = uvmgr.uvindex_around_coords(43.6532, 79.3832)
print("uvi: " , uvi.value)

w = observation.weather

print("Detailed status: " , w.detailed_status)         

print("Wind: " , w.wind("meters_sec")) #it's in meters per second for some reason CHECK
print("Humidity: " , w.humidity) #CHECK              
print("Temp: " , w.temperature('celsius')) # CHECK
print("Rain: " , w.rain)                    
print("Heat: " , w.heat_index)              
print("Clouds" , w.clouds)
print("UV: " , w.weather_icon_name)      
print(type(w))
"""
forecast = mgr.forecast_at_place('Leiria, PT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())
print(answer)


"""