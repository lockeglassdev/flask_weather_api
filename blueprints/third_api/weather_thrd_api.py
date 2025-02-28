import requests
import os

WEATHER_API_KEY = "819712d29f4b4071bb702425252702"
WEATHER_URL_BASE = "https://api.weatherapi.com/v1"
CURRENT_DAY_TOPIC = "/current.json"
FORECAST_DAYS_TOPIC = "/forecast.json"

def current_weather_api(location:str,lang:str,days:int=1):
    result = None
    query_data = {
        "q":location,
        "lang":lang,
        "key":WEATHER_API_KEY
    }

    if days == 1:
        query = WEATHER_URL_BASE + CURRENT_DAY_TOPIC
        result = requests.get(query,params=query_data)
    else:
        query = WEATHER_URL_BASE + FORECAST_DAYS_TOPIC
        query_data["days"] = days
        result = requests.get(query,params=query_data)

    if result.status_code == 200:
        return result.json()
    
    return None

if __name__ == "__main__":
    print(current_weather_api("Mexico","es",2))