import os
import requests
import datetime

def date_getter():
    data = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata")
    data = data.json()
    value = data['datetime']
    value, not_req = value.split("T")
    y, m, d = value.split("-")
    return d,m,y


def time_getter():
    x = datetime.datetime.now()
    h = x.strftime("%H")
    m = x.strftime("%M")
    return int(h), int(m)

def news_getter():
    API_KEY = os.environ['news-token']
    URL = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={API_KEY}"
    data = requests.get(URL)
    data = data.json()
    if data['status'] == "ok":
        article = data['articles'][0]
        title = article['title']
        description = article['description']
        url = article['url']
        image_url = article['urlToImage']
    return title, description, url, image_url

def weather_getter():
    API_KEY = os.environ['weather-token']
    URL = f"http://api.openweathermap.org/data/2.5/weather?q=Kolkata&units=metric&appid={API_KEY}"
    data = requests.get(URL)
    data = data.json()
    desc = data['weather'][0]['main']
    temp = data['main']['temp']
    feel = data['main']['feels_like']
    min = data['main']['temp_min']
    max = data['main']['temp_max']
    humid = data['main']['humidity']
    image_url = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
    return desc, temp, feel, min, max, humid, image_url

def color_getter():
    URL = "https://www.colr.org/json/color/random"
    data = requests.get(URL)
    data = data.json()
    hex = data['colors'][0]['hex']
    return hex

def meme_getter():
    URL = "http://api.pymeme.repl.co/"
    
    while True:
        data = requests.get(URL)
        data = data.json()
        nsfw = data['meme']['nsfw']
        if not nsfw:
            break

    post = data['meme']['post url']
    image_url = data['meme']['image url']
    title = data['meme']['title']

    return post, image_url, title

def shower_getter():
    URL = "http://api.pymeme.repl.co/shower"
    
    while True:
        data = requests.get(URL)
        data = data.json()
        nsfw = data['meme']['nsfw']
        if not nsfw:
            break

    post = data['meme']['post url']
    title = data['meme']['title']

    return post, title