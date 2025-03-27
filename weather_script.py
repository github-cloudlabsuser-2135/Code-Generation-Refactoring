import requests

def fetch_weather_data(api_key, city):
    """
    Fetch weather data for a given city from OpenWeatherMap API.

    Args:
        api_key (str): Your OpenWeatherMap API key.
        city (str): The city name for which to fetch weather data.

    Returns:
        dict: Parsed JSON response containing weather data.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    API_KEY = "8513ba1357662bbe804556210318143a"  # Replace with your OpenWeatherMap API key
    CITY = "London"
    weather_data = fetch_weather_data(API_KEY, CITY)
    if weather_data:
        print(weather_data)