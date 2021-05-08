import json
import glob

from datetime import datetime, timedelta

dirs = glob.glob('./3d/*/')

base = {
    "strategy": {
      "name": "trend-m-1",
      "version": "1.0"
    },
    "type": "3d",
    "source": "bitmex-bitstamp",
    "frequency": "1d",
    "currency": "btc",
    "product": "perp",
    "status": "done"
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

    item = {**item, **base}

    data.append(item)

with open(f'list-3d.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
