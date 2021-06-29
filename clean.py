import json
import glob
import shutil

from datetime import datetime, timedelta

dirs = glob.glob('./fof/*/')

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    id = str(ts)
    date = str(dt)

    base_dir = f'fof/{ts}'

    with open(f"{base_dir}/metrics.json", 'r', encoding='utf-8') as f:
        metrics = json.load(f)['fof']

        metric = metrics['max_drawdown']
        if metric > 0.3:
          print(metric)
          shutil.rmtree(f'xx/fof/{id}')
