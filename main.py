# main.py
from simulation import simulate_period
from visualization import plot_temperature

def summarize_forecast(forecast):
    total_temp = sum([day['Temperature'] for day in forecast])
    total_humidity = sum([day['Humidity'] for day in forecast])
    max_temp = max([day['Temperature'] for day in forecast])
    min_temp = min([day['Temperature'] for day in forecast])
    
    avg_temp = total_temp / len(forecast)
    avg_humidity = total_humidity / len(forecast)
    
    weather_types = [day['Weather Type'] for day in forecast]
    sunny_days = weather_types.count('Sunny')
    rainy_days = weather_types.count('Rainy')
    snowy_days = weather_types.count('Snowy')
    cloudy_days = weather_types.count('Cloudy')

    print("\nForecast Summary:")
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Average Humidity: {avg_humidity:.2f}%")
    print(f"Max Temperature: {max_temp:.2f}°C")
    print(f"Min Temperature: {min_temp:.2f}°C")
    print(f"Sunny Days: {sunny_days}")
    print(f"Rainy Days: {rainy_days}")
    print(f"Snowy Days: {snowy_days}")
    print(f"Cloudy Days: {cloudy_days}")

def main():
    days = int(input("Enter the number of days to simulate: "))
    
    # Ask user for the season
    season = input("Enter the season (Summer, Winter, Spring, Autumn): ").capitalize()

    try:
        forecast = simulate_period(days, season)
        
        for i, day_weather in enumerate(forecast, start=1):
            print(f"Day {i}: {day_weather}")
        
        plot_temperature(forecast)
        
        # Print forecast summary
        summarize_forecast(forecast)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
