# visualization.py
import matplotlib.pyplot as plt

def plot_temperature(forecast):
    days = list(range(1, len(forecast) + 1))
    temperatures = [day['Temperature'] for day in forecast]
    
    plt.plot(days, temperatures, label="Temperature")
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Forecast')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example forecast data to test the plot
    sample_forecast = [
        {'Temperature': 25, 'Humidity': 45, 'Wind Speed': 10, 'Weather Type': 'Sunny'},
        {'Temperature': 28, 'Humidity': 50, 'Wind Speed': 12, 'Weather Type': 'Cloudy'},
        # Add more days for testing
    ]
    
    plot_temperature(sample_forecast)
