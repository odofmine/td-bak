import json
import glob

from datetime import datetime, timedelta

dirs = glob.glob('./*/')

data = []

dirs = [x[2:-1] for x in dirs]
dirs = [x for x in dirs if x.endswith('3d')]
dirs = sorted(list(map(lambda x : int(x[0:-3]), dirs)), reverse=True)

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    item['id'] = str(ts) + '-3d'
    item['date'] = str(dt)

    data.append(item)

with open(f'list-3d.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
