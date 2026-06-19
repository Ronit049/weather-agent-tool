import requests


def weather_data_call():
    lat = 26.9124
    lon = 75.7873

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "lat": lat,
            "lon": lon,
            "appid": "YOUR_API_KEY",
            "units": "metric"
        }
    )

    return response.json()


def get_current_weather(city: str, unit: str = "celsius") -> dict:

    city_data = {
        # all your cities here
    }

    data = city_data.get(
        city.lower(),
        {
            "temp": 30,
            "condition": "Clear",
            "humidity": 50
        }
    )

    temp = (
        data["temp"]
        if unit == "celsius"
        else round(data["temp"] * 9 / 5 + 32, 1)
    )

    return {
        "city": city,
        "temperature": temp,
        "unit": unit,
        "condition": data["condition"],
        "humidity": data["humidity"],
        "source": "Simulated Weather Database"
    }