import requests

API_KEY = '5481ecf4e9b3487729ba6c69014944d7'  # Replace with your OpenWeatherMap API key
GEOCODING_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_lat_lon(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
    }
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        return lat, lon
    else:
        print(f"Error fetching data for city {city_name}: {response.status_code}")
        return None

def get_current_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

def main():
    city_name = input("Enter city name: ")
    weather_data = get_current_weather(city_name)
    if weather_data:
        print(f"Current weather in {city_name}:")
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        print(f"Temperature: {temp}°C")
        print(f"Description: {description.capitalize()}")

if __name__ == "__main__":
    main()
