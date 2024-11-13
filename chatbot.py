import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class Chatbot:
    def __init__(self, name, weather_api_key):
        self.name = name
        self.weather_api_key = weather_api_key

    def get_input(self):
        user_input= input("Hello, I'm Omnia. How can I help you today?")
        return user_input

    def generate_response(self, user_input):
        if "hi" in user_input.lower():
            return "Hi! How can I help you today?"
        elif "hello" in user_input.lower():
            return ("Hello! How can I help you today?")
        elif "how are you" in user_input.lower():
            return "I'm a chatbot made by humans. I don't have any feelings."
        elif "weather" in user_input.lower():
            city = input("Which city or town would you like to know the weather for?")
            return self.get_weather(city)



class WeatherBot(Chatbot):
    def __init__(self, weather_api_key):
        super().__init__("Weather Bot")
        self.weather_api_key = weather_api_key

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}"
        response = requests.get(url)
        weather_data = response.json()
        return f"The weather in {city} is {weather_data['weather'][0]['description']}"




class ReminderBot(Chatbot):
    def __init__(self, reminder):
        super().__init__("Reminder Bot")
        self.reminder = reminder

    def create_reminder(self):
        pass
    def get_reminder(self):
        pass
    def delete_reminder(self):
        pass
    




