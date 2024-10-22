# simulation.py
from weather import Weather

def get_seasonal_ranges(season):
    if season == 'Summer':
        return (25, 40), (20, 60), (5, 15)  # High temperature, moderate humidity
    elif season == 'Winter':
        return (-5, 10), (40, 80), (10, 30)  # Cold temperature, higher wind speed
    elif season == 'Spring':
        return (10, 25), (30, 70), (5, 20)  # Mild weather
    elif season == 'Autumn':
        return (10, 20), (40, 80), (5, 25)  # Cooler, more humid weather
    else:
        raise ValueError("Invalid season. Choose from: Summer, Winter, Spring, Autumn")

def simulate_period(days, season):
    temperature_range, humidity_range, wind_speed_range = get_seasonal_ranges(season)
    weather = Weather(temperature_range, humidity_range, wind_speed_range)
    forecast = []
    
    for _ in range(days):
        daily_weather = weather.generate_daily_weather()
        forecast.append(daily_weather)
    
    return forecast
