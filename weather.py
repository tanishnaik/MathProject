# weather.py
import random

class Weather:
    def __init__(self, temperature_range, humidity_range, wind_speed_range):
        self.temperature_range = temperature_range
        self.humidity_range = humidity_range
        self.wind_speed_range = wind_speed_range
    
    def generate_temperature(self):
        return random.uniform(*self.temperature_range)
    
    def generate_humidity(self):
        return random.randint(*self.humidity_range)
    
    def generate_wind_speed(self):
        return random.uniform(*self.wind_speed_range)
    
    def generate_daily_weather(self):
        conditions = ['Sunny', 'Rainy', 'Cloudy', 'Snowy']
        temperature = self.generate_temperature()
        humidity = self.generate_humidity()
        wind_speed = self.generate_wind_speed()
        weather_type = random.choices(conditions, weights=[0.5, 0.2, 0.2, 0.1], k=1)[0]
        
        return {
            "Temperature": temperature,
            "Humidity": humidity,
            "Wind Speed": wind_speed,
            "Weather Type": weather_type
        }
