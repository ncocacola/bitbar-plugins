#!/usr/local/bin/python
# coding: utf-8

# Kraken: last trade price
# BitBar plugin
#
# by Nicolas Khadivi
# Shows the last price BTCEUR price from Kraken.

import json
import urllib2

data = urllib2.urlopen("https://api.kraken.com/0/public/Ticker?pair=XBTEUR").read()
obj = json.loads(data)
price = float(obj['result']['XXBTZEUR']['c'][0])
print "€{0:.2f}".format(price)
