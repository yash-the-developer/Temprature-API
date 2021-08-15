import bs4
import requests
from flask import Flask

app = Flask(__name__)

TEMPERATURE_TAG = 'BNeawe iBp4i AP7Wnd'
TARGET_URL = "https://www.google.com/search?q=temprature+at+"


@app.route('/')
def main():
    return 'API is working!'


@app.route("/temperature/<place>")
def temperature(place):
    postRequest = requests.get(TARGET_URL + place)
    result = findByClass(postRequest.text, TEMPERATURE_TAG)
    return result

def findByClass(text, className):
    soup = bs4.BeautifulSoup(text, 'lxml')
    result = soup.find_all("div", {"class": className})

    try:
        return result[0].getText()
    except Exception:
        return "no result found"
