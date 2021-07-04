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

not_comps = ['fof', 'base', 'btc', 'eth', 'etc']

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    item['id'] = str(ts)
    item['date'] = str(dt)

    base_dir = f'fof/{ts}'

    with open(f"{base_dir}/fof.json", 'r', encoding='utf-8') as f:
        prices = json.load(f)

        start_ts = prices[0][0]
        end_ts = prices[-1][0]

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')

    with open(f"{base_dir}/funds.json", 'r', encoding='utf-8') as f:
        funds = json.load(f)

        # for intersected in list(set(funds) & set(not_comps)):
        #     funds.remove(intersected)

        item['funds'] = funds

    with open(f"{base_dir}/metrics.json", 'r', encoding='utf-8') as f:
        metrics = json.load(f)['fof']

        item ['max_retracement'] = metrics['max_drawdown']
        item ['annual_return'] = metrics['annual_return_ratio']
        item ['sharpe_ratio'] = metrics['sharpe_ratio']

    item = {**item, **base}
    data.append(item)

with open(f'list-fof.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
