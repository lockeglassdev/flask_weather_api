from flask import Blueprint

weather_bp = Blueprint("weather",__name__,url_prefix="/weather")

@weather_bp.route("/<country>",methods=["GET"])
def weather_endpoint(country:str):
    return f"{country} weather..."