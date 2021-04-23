import json
import os
import glob
import calendar

from datetime import datetime

dirs = glob.glob('./*/')

base = {
    "strategy": {
      "name": "t4",
      "version": "1.0"
    },
    "source": "bitmex-bitstamp",
    "frequency": "1d",
    "currency": "btc",
    "product": "perp",
    "status": "done"
}

data = []

for d in dirs:
    ts = d[2:-1]
    dt = datetime.utcfromtimestamp(int(ts))

    item = {}

    item['id'] = ts
    item['date'] = str(dt)

    with open(f"{d}price.json", 'r', encoding='utf-8') as f4:
        prices = json.load(f4)

        start_ts = prices[0][0] / 1000
        end_ts = prices[-1][0] / 1000

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')


    with open(f"{d}metrics.json", 'r', encoding='utf-8') as f2:
        metrics = json.load(f2)

        item['annual_return'] = metrics['strategy']['annual_return_ratio']
        item['sharpe_ratio'] = metrics['strategy']['sharpe_ratio']

    with open(f"{d}statistic.json", 'r', encoding='utf-8') as f3:
        statistic = json.load(f3)

        item['max_retracement'] = statistic['dollar_retracement']

    item = {**item, **base}
    data.append(item)

with open(f'list.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

