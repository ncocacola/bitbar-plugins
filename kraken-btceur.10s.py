#!/usr/local/bin/python
# coding: utf-8

# Kraken: last trade price
# BitBar plugin
#
# by Nicolas Khadivi
# Shows the last price BTCEUR price from Kraken.

import json
import requests
import sys

url = "https://api.kraken.com/0/public/Ticker"
payload = {"pair": "XXBTZEUR"}

try:
    response = requests.get(url, params=payload)
except:
    print "Error"
    print "---"
    print "Could not connect to the Internet | color = red"
    sys.exit(-1)

obj = response.json()
ticker = obj['result']['XXBTZEUR']

price = float(ticker['c'][0])
day = (float(ticker['l'][0]), float(ticker['h'][0]))

print "€{0:.2f}".format(price)
print "---"
print "Price: €{0:.2f}".format(price)
print "Low: €{0:.2f}".format(day[0])
print "High: €{0:.2f}".format(day[1])
