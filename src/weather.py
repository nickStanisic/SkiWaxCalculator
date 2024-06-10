import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')
min_lat = 37
lat_increases = 5
min_long = -108
long_increases = 6

@dataclass
class TemperatureData:
    time: int
    temp: float

@dataclass
class coloradoData:
    lat: int
    long: int
    temperature_data: list[TemperatureData]


def get_weather_data(lat, lon, API_key, units):
    resp = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units={units}').json()
    return resp

def get_temperature_data(lat,lon):
    data = get_weather_data(lat,lon,api_key,"imperial")
    temperature_list = []
    for i in range (0,data.get('cnt')):
        tempData = TemperatureData(
            time = data.get('list')[i].get('dt'),
            temp = data.get('list')[i].get('main').get('temp')
        )
        temperature_list.append(tempData)
    return temperature_list
def get_temperatures_for_colorado():
    colorado_temperature_list = []
    for i in range (min_lat,min_lat + lat_increases):
        for j in range (min_long,min_long + long_increases):
            colorado_temperature = coloradoData (
                lat = i,
                long = j,
                temperature_data = get_temperature_data(i,j)
            )
            colorado_temperature_list.append(colorado_temperature)
    return colorado_temperature_list

