# -*- coding: utf-8 -*-

import json
import os

from datetime import datetime
from urllib.request import urlopen

from dotenv import load_dotenv

load_dotenv()

# Date and Time
YEAR = datetime.now().strftime('%Y')
MONTH = datetime.now().strftime('%m')
DAY = datetime.now().strftime('%d')
HOUR = datetime.now().strftime('%H')
MIN = datetime.now().strftime('%M')
SEC = datetime.now().strftime('%S')

# API Keys
NEWS_KEY = os.getenv('NEWS_KEY')
WEATHER_KEY = os.getenv('WEATHER_KEY') # This is a 'WOEID' and not an actual key

# API URLs
HEBDATE_URL = 'https://www.hebcal.com/hebcal?'\
    + f'v=1&cfg=json&maj=on&min=on&mod=on&year=now&month={MONTH}&d={DAY}'
CURRENCY_URL = 'https://api.exchangeratesapi.io/latest?base=USD'
NEWS_URL = f'http://newsapi.org/v2/top-headlines?country=il&apiKey={NEWS_KEY}'
WEATHER_URL = f'https://www.metaweather.com/api/location/{WEATHER_KEY}'


def gregorian_date():
    return f'{DAY}/{MONTH}/{YEAR}'


def hebrew_date():
    # Scrapping of Hebrew dates every begining of a year
    # This option might be added in the future to reduce complexity
    if f'{DAY}/{MONTH}' == '01/01':
        pass
    try:
        with urlopen(HEBDATE_URL) as response:
            source = response.read().decode('utf-8')
            heb_dates = json.loads(source)
        return heb_dates['items'][0]['hebrew']  # Today's date in Hebrew
    except:
        return 'לא ניתן להציג תאריך עברי'    


def time():
    return f'{HOUR}:{MIN}:{SEC}'


def currency():
    try:
        with urlopen(CURRENCY_URL) as response:
            source = response.read()
            curr_dict = json.loads(source)
            base_rate = curr_dict['rates']['ILS']
            USD = '$ - USD: ' + str(round(base_rate, 4))
            EUR = '€ - EUR: ' + str(round(base_rate / curr_dict['rates']['EUR'], 4))
            GBP = '£ - GBP: ' + str(round(base_rate / curr_dict['rates']['GBP'], 4))
            JPY = '¥ - JPY: ' + str(round(base_rate / curr_dict['rates']['JPY'], 4))
            return [USD, EUR, GBP, JPY]
    except:
        return ['שגיאה' ,'לא ניתן להציג שערי מט"ח']


def news():
    # Sign-up for a free API Key at:
    # https://newsapi.org/s/israel-news-api
    try:
        with urlopen(NEWS_URL) as response:
            source = response.read()
            news_titles = json.loads(source)['articles']
            news = []
            for i in news_titles:
                news.append(i['title'])
            return news
    except:
        return ['שגיאה' ,'לא ניתן להציג חדשות']


def weather():
    # https://metaweather.com/api/
    pass


def gmail():
    pass


def google_calendar():
    pass


def stocks():
    pass


def inspiration():
    pass
