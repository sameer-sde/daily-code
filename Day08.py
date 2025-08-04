import requests

def get_weather(city):
    use_dummy_data = True  # Set to False to use real API

    if use_dummy_data:
        print(f"Showing dummy weather data for {city} 🌤️")
        return {
            "temperature": "28°C",
            "description": "Partly cloudy",
            "humidity": "60%",
            "wind": "15 km/h"
        }

    # Replace with your OpenWeatherMap API key if you want real data
    api_key = "your_api_key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return {"error": data.get("message", "Unknown error")}

        weather = {
            "temperature": f"{data['main']['temp']}°C",
            "description": data['weather'][0]['description'],
            "humidity": f"{data['main']['humidity']}%",
            "wind": f"{data['wind']['speed']} km/h"
        }
        return weather
    except Exception as e:
        return {"error": str(e)}

# -------------------------------

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_info = get_weather(city_name)

    print("\n📍 Weather Report:")
    for key, value in weather_info.items():
        print(f"{key.title()}: {value}")
