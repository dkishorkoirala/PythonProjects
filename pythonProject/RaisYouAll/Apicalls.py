import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return "Sorry, I couldn't fetch the weather data."
    weather = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    return f"The weather in {city} is {weather} with a temperature of {temperature}°C."

# Add this to the chatbot's logic
if "weather" in user_input.lower():
    city = user_input.split("in ")[-1].strip()
    print(f"RaiseYouAll: {get_weather(city)}")