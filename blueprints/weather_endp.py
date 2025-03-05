"""
This module contains all the logic that handles the 
endpoint of user requests about the weather.
"""

from flask import Blueprint, request, jsonify
from .third_api.weather_thrd_api import forecast_exctract_data, forecast_weather_api

weather_bp = Blueprint("weather",__name__,url_prefix="/weather")

@weather_bp.route("/<country>",methods=["GET"])
def weather_endpoint(country:str):
    query = request.get_json()

    days = query["days"]
    language = query["lang"]
    temp_metric = query["temp_m"]
    wind_metric = query["wind_m"]
    precp_metric = query["percp_m"]

    # Extract the request data to handling it
    result = forecast_weather_api(country,language,days)
    days_obj = forecast_exctract_data(result)

    # Specifies the fields to convert to
    # JSON for sending it through a dict.
    format_objects = []
    for day in days_obj:
        new_fday = {
            "condition":day.condition,
            "temperature":day.get_temperature(temp_metric),
            "wind":day.get_wind(wind_metric),
            "precipitation":day.get_precipitation(precp_metric),
            "rainy_day":day.is_rainy_day(),
            "snowny_day":day.is_snow_day()
        }
        format_objects.append(new_fday)

    # The full response for the user
    response = {
        "country_data":{
            "country":days_obj[0].country,
            "tz_info":days_obj[0].tz_info,
            "region":days_obj[0].region
        },
        "weath_forecast":format_objects
    }

    # Convert into JSON/HTTP response
    return jsonify(response)