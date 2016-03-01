#!/usr/local/bin/python
# coding: utf-8

# Kraken: last trade price
# BitBar plugin
#
# by Nicolas Khadivi
# Shows the last price BTCEUR price from Kraken.

import json
import requests

url = "https://api.kraken.com/0/public/Ticker"
payload = {"pair": "XXBTZEUR"}

response = requests.get(url, params=payload)
obj = response.json()

price = float(obj['result']['XXBTZEUR']['c'][0])
print "€{0:.2f}".format(price)
