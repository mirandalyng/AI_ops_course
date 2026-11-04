import httpx 
from pydantic_ai import RunContext
from deps import WeatherDeps 


def get_weather(ctx: RunContext[WeatherDeps], lat: float, lon: float):
    """get current weather from latitude and longitude"""
    response = httpx.get(
        "https://api.open-meteo.com/v1/forecast", 
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"}, 
        timeout=30,
    )

    response.raise_for_status()
    current = response.json().get("current")
    temperature = current.get("temperature_2m")


    return f"Current temperature in {ctx.deps.city} is {temperature} Celsius"

def geocode(city: str) -> dict: 
    response = httpx.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
    )

    response.raise_for_status()
    place = response.json().get("results")[0]
    return {"latitude": place.get("latitude"), "longitude": place.get("longitude")}