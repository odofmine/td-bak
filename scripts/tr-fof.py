import json
import glob

from datetime import datetime, timezone, timedelta

dirs = glob.glob('./fof/*/')

base = {
    "type": "fof",
    "source": "bitmex-bitstamp",
    "frequency": "1d",
    "currency": "btc",
    "funds": [
      "base", "t4", "t5"
    ]
}

data = []

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    item['id'] = str(ts)
    item['date'] = str(dt)

    base_dir = f'fof/{ts}'

    with open(f"{base_dir}/base.json", 'r', encoding='utf-8') as f4:
        prices = json.load(f4)

        start_ts = prices[0][0]
        end_ts = prices[-1][0]

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')

    item = {**item, **base}
    data.append(item)

with open(f'list-fof.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
