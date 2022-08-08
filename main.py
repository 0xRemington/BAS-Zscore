import csv
import time
import requests
import ccxt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
Bid = None
Time = None
Ask = None
Spread = None

fieldnames = ["bid", 'ask', 'spread', "time"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        res = requests.get('https://ftx.com/api/markets/BTC-PERP/orderbook?depth=1').json()
        res2 = requests.get('https://ftx.com/api/markets/BTC-PERP/candles?resolution=15').json()

        info = {
            "bid": Bid,
            "ask": Ask,
            "spread": Spread,
            "time": Time
        }

        csv_writer.writerow(info)
        print(Bid, Ask)
        Bid = res['result']['bids'][0][1]
        Ask = res['result']['asks'][0][1]
        Spread = Bid - Ask

        Time = time.time()

    time.sleep(1)

