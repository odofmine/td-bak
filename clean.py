import json
import glob
import shutil

from datetime import datetime, timedelta

dirs = glob.glob('./bt/*/')

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    id = str(ts)
    date = str(dt)

    base_dir = f'xxx/bt/{ts}'

    with open(f"{base_dir}/params.json", 'r', encoding='utf-8') as f:
        metrics = json.load(f)

        if not 'pair' in metrics or not 'pstr' in metrics:
          print(dt)
          shutil.rmtree(base_dir)
