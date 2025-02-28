import requests
from typing import Tuple,List

WEATHER_API_KEY = "819712d29f4b4071bb702425252702"
WEATHER_URL_BASE = "https://api.weatherapi.com/v1"
CURRENT_DAY_TOPIC = "/current.json"
FORECAST_DAYS_TOPIC = "/forecast.json"

def current_weather_api(location:str,lang:str,days:int=1) -> dict | None:
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

    # The base query params for WeatherAPI
    query_data = {
        "q":location,
        "lang":lang,
        "key":WEATHER_API_KEY
    }

    query = WEATHER_URL_BASE + FORECAST_DAYS_TOPIC
    query_data["days"] = days
    result = requests.get(query,params=query_data)

    if result.status_code == 200:
        return result.json()
    
    return None

def forecast_exctract_data(data:dict) -> Tuple[dict,List[dict]]:
    """
    This function extracts only the required data to make
    a JSON response from the app clients.

    :param data: A JSON data response as a dict
    :type data: dict
    :return: The location info and the forecast of next days.
    :rtype: Tuple[dict,List[dict]]
    """
    location_info = data["location"]
    forecast = data["forecast"]["forecastday"]

    return location_info,forecast

if __name__ == "__main__":
    pass