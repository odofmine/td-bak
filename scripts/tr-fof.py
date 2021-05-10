import json
import glob

from datetime import datetime, timezone, timedelta

dirs = glob.glob('./fof/*/')

base = {
    "type": "fof",
    "source": "bitmex-bitstamp",
    "frequency": "1d",
    "currency": "btc"
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

    with open(f"{base_dir}/base.json", 'r', encoding='utf-8') as f:
        prices = json.load(f)

        start_ts = prices[0][0]
        end_ts = prices[-1][0]

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')

    with open(f"{base_dir}/funds.json", 'r', encoding='utf-8') as f:
        funds = json.load(f)

        item['funds'] = funds

    item = {**item, **base}
    data.append(item)

with open(f'list-fof.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
