"""
This module was created to create an abstraction that 
makes the WeatherApi response more manageable, handling 
it through the WeatherDay class that maps all that 
information to be instantiated in an object.
"""
from typing import Tuple,Literal

class WeatherDay:
    """
    This class extracts all the information from an API 
    response to make it easier to access and explore.
    """
    def __init__(self,location:dict,metrics:dict,extra_data:dict=None):
        self.location = location
        self.metrics = metrics
        self.extra_data = extra_data

    @property
    def country(self) -> str:
        """
        :return:The country name
        :rtype: str
        """
        return self.location["country"]
    
    @property
    def region(self) -> str: 
        """
        :return: The region name
        :rtype: str
        """
        return self.location["region"]

    @property
    def tz_info(self) -> str:
        """
        :return: _description_
        :rtype: str
        """
        return self.location["tz_id"]
    
    @property
    def humidity(self) -> float:
        """
        :return: Current humidity day
        :rtype: float
        """
        return self.metrics["avghumidity"]
    
    @property
    def rain_probability(self) -> float:
        """
        :return: The probability of rain
        :rtype: float
        """
        return self.metrics["daily_chance_of_rain"]
    
    @property
    def snow_probaility(self) -> float:
        """
        :return: The probability of snow
        :rtype: float
        """
        return self.metrics["daily_chance_of_snow"]
    
    @property
    def condition(self) -> str:
        """
        :return: A text with the forecast day
        :rtype: str
        """
        return self.metrics["condition"]["text"]
    
    @property
    def other_details(self) -> dict:
        """
        :return: Extra data from request to use.
        :rtype: dict
        """
        return self.extra_data
    
    def get_temperature(self,metric:Literal["f"]|Literal["c"]) -> Tuple[float,float]:
        """
        :param metric: Metric of response ("f" | "c")
        :type metric: Literal[&quot;f&quot;] | Literal[&quot;c&quot;]
        :return: A tuple (min,max) with expected temperatures
        :rtype: Tuple[float,float]
        """
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
    
    def get_wind(self,metric:Literal["mph"]|Literal["kph"]) -> float:
        """
        :param metric: Metric of response ("mph" | "kph")
        :type metric: Literal["mph"] | Literal["kph&quot"]
        :return: An expected wind speed
        :rtype: float
        """
        match metric:
            case "kph":
                wind_m = self.metrics["maxwind_kph"]
            case "mph":
                wind_m = self.metrics["maxwind_mph"]
            case _:
                return None
        return wind_m
    
    def get_precipitation(self,metric:Literal["mm"]|Literal["in"]) -> float:
        """
        :param metric: Metric of response ("mm" | "in")
        :type metric: Literal["mm"] | Literal["in"]
        :return: An expected precipitation level
        :rtype: float
        """
        match metric:
            case "mm":
                precip = self.metrics["totalprecip_mm"]
            case "in":
                precip = self.metrics["totalprecip_in"]
            case _:
                return None
            
        return precip
    
    def is_rainy_day(self) -> bool:
        """
        :return: If it rains
        :rtype: bool
        """
        return True if self.metrics["daily_will_it_rain"] > 0 else False
    
    def is_snow_day(self) -> bool:
        """
        :return: If it snow
        :rtype: bool
        """
        return True if self.metrics["daily_will_it_snow"] > 0 else False