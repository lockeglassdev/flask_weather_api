from datetime import datetime
from typing import Tuple,Literal

class WeatherDay:
    def __init__(self,location:dict,metrics:dict,extra_data:dict=None):
        self.location = location
        self.metrics = metrics
        self.extra_data = extra_data

    @property
    def country(self):
        return self.location["country"]
    
    @property
    def region(self):
        return self.location["region"]

    @property
    def tz_info(self):
        return self.location["tz_id"]
    
    @property
    def humidity(self):
        return self.metrics["avghumidity"]
    
    @property
    def rain_probability(self):
        return self.metrics["daily_chance_of_rain"]
    
    @property
    def snow_probaility(self):
        return self.metrics["daily_chance_of_snow"]
    
    @property
    def condition(self):
        return self.metrics["condition"]["text"]
    
    @property
    def other_details(self):
        return self.extra_data
    
    def get_temperature(self,metric:Literal["f"]|Literal["c"]) -> Tuple[float,float]:
        match metric:
            case "f":    
                maxt = self.metrics["maxtemp_c"]
                mint = self.metrics["mintemp_c"]
            case "c":
                maxt = self.metrics["maxtemp_f"]
                mint = self.metrics["mintemp_f"]
            case _:
                return None

        return mint,maxt
    
    def get_wind(self,metric:Literal["mph"]|Literal["kph"]):
        match metric:
            case "kph":
                wind_m = self.metrics["maxwind_kph"]
            case "mph":
                wind_m = self.metrics["maxwind_mph"]
            case _:
                return None
        return wind_m
    
    def get_precipitation(self,metric:Literal["mm"]|Literal["in"]):
        match metric:
            case "mm":
                precip = self.metrics["totalprecip_mm"]
            case "in":
                precip = self.metrics["totalprecip_in"]
            case _:
                return None
            
        return precip
    
    def is_rainy_day(self):
        return True if self.metrics["daily_will_it_rain"] > 0 else False
    
    def is_snow_day(self):
        return True if self.metrics["daily_will_it_snow"] > 0 else False