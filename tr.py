import json
import glob

from datetime import datetime, timezone, timedelta

dirs = glob.glob('./*/')

base = {
    "strategy": {
      "name": "trend-m-1",
      "version": "1.0"
    },
    "source": "bitmex-bitstamp",
    "frequency": "1d",
    "currency": "btc",
    "product": "perp",
    "status": "done"
}

data = []

dirs = [x[2:-1] for x in dirs]
dirs = [x for x in dirs if not x.endswith('3d')]
dirs = sorted(list(map(lambda x : int(x), dirs)), reverse=True)

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    item['id'] = str(ts)
    item['date'] = str(dt)

    with open(f"{ts}/price.json", 'r', encoding='utf-8') as f4:
        prices = json.load(f4)

        start_ts = prices[0][0] / 1000
        end_ts = prices[-1][0] / 1000

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')


    with open(f"{ts}/metrics.json", 'r', encoding='utf-8') as f2:
        metrics = json.load(f2)

        item['annual_return'] = metrics['strategy']['annual_return_ratio']
        item['sharpe_ratio'] = metrics['strategy']['sharpe_ratio']

    with open(f"{ts}/statistic.json", 'r', encoding='utf-8') as f3:
        statistic = json.load(f3)

        item['max_retracement'] = statistic['dollar_retracement']

    item = {**item, **base}
    data.append(item)

with open(f'list.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
