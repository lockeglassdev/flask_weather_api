"""
This module contains all the logic to make requests to 
the weather API and manage the information contained 
therein.
"""
import requests
from typing import List
from .models import WeatherDay

# WeatherAPI context
WEATHER_API_KEY = "somekey"
WEATHER_URL_BASE = "https://api.weatherapi.com/v1"
CURRENT_DAY_TOPIC = "/current.json"
FORECAST_DAYS_TOPIC = "/forecast.json"

def forecast_weather_api(location:str,lang:str,days:int=1) -> dict | None:
    """
    This function provides a conection to WeatherAPI, for get
    the forecast weather in the next days.

    :param location: The location weather to get
    :type location: str
    :param lang: The language of the response
    :type lang: str
    :param days: The next 'n' forecast weather days, defaults to 1
    :type days: int, optional
    :return: A dictionary with JSON data response if exists else None.
    :rtype: dict | None
    """
    result = None

    # The base obligatory params for a WeatherAPI request
    query_data = {
        "q":location,
        "lang":lang,
        "key":WEATHER_API_KEY
    }

    # Making the URL
    query = WEATHER_URL_BASE + FORECAST_DAYS_TOPIC

    # Add a user expected days
    query_data["days"] = days

    result = requests.get(query,params=query_data)

    if result.status_code == 200:
        return result.json()
    
    return None

def forecast_exctract_data(data:dict) -> List[WeatherDay]:
    """
    This function extracts only the required data to make
    a JSON response from the app clients.

    :param data: A JSON data response as a dict
    :type data: dict
    :return: A WatherDay object collection.
    :rtype: List[WeatherDay]
    """
    # Discrimine the location and forecast data
    location_info = data["location"]
    forecast = data["forecast"]["forecastday"]

    # This contains all WeatherDay objects
    day_list = []

    for day in forecast:
        new_day = WeatherDay(location_info,day["day"])
        day_list.append(new_day)

    return day_list

if __name__ == "__main__":
    pass
