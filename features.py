# -*- coding: utf-8 -*-

import json
import os

from datetime import datetime
from urllib.request import urlopen

from dotenv import load_dotenv


load_dotenv()

### Date and Time ###
YEAR = datetime.now().strftime('%Y')
MONTH = datetime.now().strftime('%m')
DAY = datetime.now().strftime('%d')
HOUR = datetime.now().strftime('%H')
MIN = datetime.now().strftime('%M')
SEC = datetime.now().strftime('%S')

### API Keys ###
# Sign up on http://newsapi.org/v2/top-headlines?country=il
NEWS_KEY = os.getenv('NEWS_KEY')

# Find your code at https://booked.co.il/
WEATHER_CITY_CODE = os.getenv('WEATHER_CITY_CODE')

# For future feature, not implemented currently
WEATHER_WOEID = os.getenv('WEATHER_WOEID')


### API URLs ###
HEBDATE_URL = 'https://www.hebcal.com/hebcal?'\
    + f'v=1&cfg=json&maj=on&min=on&mod=on&year=now&month={MONTH}&d={DAY}'
CURRENCY_URL = 'https://api.exchangeratesapi.io/latest?base=USD'
NEWS_URL = f'http://newsapi.org/v2/top-headlines?country=il&apiKey={NEWS_KEY}'
WEATHER_URL = f'https://w.bookcdn.com/weather/picture/32_{WEATHER_CITY_CODE}_1_25_000000_250_000000_ffffff_ffffff_1_2071c9_ffffff_0_6.png?scode=124&domid=407&anc_id=74406'

def gregorian_date():
    return f'{DAY}/{MONTH}/{YEAR}'


def time():
    return f'{HOUR}:{MIN}:{SEC}'


def currency():
    try:
        with urlopen(CURRENCY_URL) as response:
            source = response.read()
            curr_dict = json.loads(source)
            base_rate = curr_dict['rates']['ILS']
            USD = 'USD: ' + str(round(base_rate, 4))
            EUR = 'EUR: ' + str(round(base_rate / curr_dict['rates']['EUR'], 4))
            GBP = 'GBP: ' + str(round(base_rate / curr_dict['rates']['GBP'], 4))
            JPY = 'JPY: ' + str(round(base_rate / curr_dict['rates']['JPY'], 4))
            return [USD, EUR, GBP, JPY]
    except:
        return ['Error fetching' ,'currency data']


def currency_string():
    currency_string = '['
    currency_list = currency()
    for item in currency_list:
        currency_string += f'"{item}", '
    currency_string = currency_string[0:-2]
    currency_string += ']'
    return currency_string
    
    
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
        return ['Error fetching' ,'news data']


def weather():
    return WEATHER_URL


def gmail():
    pass


def google_calendar():
    pass


def stocks():
    pass


def inspiration():
    pass


# Scrapping of Hebrew dates every begining of a year
# This option might be added in the future to reduce complexity

# def hebrew_date():
#     if f'{DAY}/{MONTH}' == '01/01':
#         pass
#     try:
#         with urlopen(HEBDATE_URL) as response:
#             source = response.read().decode('utf-8')
#             heb_dates = json.loads(source)
#         return heb_dates['items'][0]['hebrew']  # Today's date in Hebrew
#     except:
#         return 'לא ניתן להציג תאריך עברי'    
