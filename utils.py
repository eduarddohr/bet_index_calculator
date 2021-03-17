import urllib.request, urllib.error, urllib.parse
import re
import pandas as pd
from models import Company


def downloadHTML(url):
    response = urllib.request.urlopen(url)
    web_content = response.read().decode('utf-8')
    return web_content


def extract_price(content):
    value_search = re.search("<strong class=\"value\">([0-9.,]*)</strong>", content)
    price = value_search.group(1)
    return price


def get_BET_index(number_of_companies=16):
    html = downloadHTML("https://m.bvb.ro/FinancialInstruments/Indices/IndicesProfiles")
    table = pd.read_html(html)
    whole_dataframe = table[4]
    df_bet_index = whole_dataframe[["Company", "Symbol", "Ref. price", "Weight (%)"]]

    bet_index = []

    for index, row in df_bet_index.iterrows():
        bet_index.append(Company(row['Company'], row['Symbol'], row['Ref. price'], row['Weight (%)']))
        if index == number_of_companies - 1:
            break

    return bet_index
