import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import warnings
import urllib3

from decouple import Config, Csv
config = Config('.env')
api_key = config.get("API_KEY")

# Suppress the urllib3 warning about SSL compatibility
warnings.filterwarnings("ignore", category=DeprecationWarning, module="urllib3")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# get weather from api
def get_weather(city):
    # api_key = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return icon_url, temperature, description, city, country


# function to search weather for a city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # get weather icon image
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # update description
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")


root = tk.Tk()
root.title('weather-application-py3')
root.geometry("400x400")

city_entry = tk.Entry(root, font="Helvetica 18")
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=search)
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica 20")
description_label.pack()

root.mainloop()


