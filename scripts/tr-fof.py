import json
import glob
import os

from datetime import datetime, timezone, timedelta
import shutil

dirs = glob.glob('./fof/*/')

base = {
    "type": "fof",
    "source": "",
    "frequency": ""
}

data = []

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

not_comps = ['fof', 'base', 'btc', 'eth', 'market_cap']

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)
    dt += timedelta(hours=8)

    item = {}

    item['id'] = str(ts)
    item['date'] = str(dt)

    base_dir = f'fof/{ts}'
    fund_name = 'fof'
    domain = ''

    if not os.path.exists(f'{base_dir}/remark.md'):
        shutil.copyfile('remark-example.md', f'{base_dir}/remark.md')

    with open(f'{base_dir}/config.json', 'r', encoding='utf-8') as f:
        configs = json.load(f)
        fund_name = configs['name']
        if 'domain' in configs:
            domain = configs['domain']

        item['domain'] = domain

    with open(f'{base_dir}/{fund_name}.json', 'r', encoding='utf-8') as f:
        fund = json.load(f)

        start_ts = fund[0][0]
        end_ts = fund[-1][0]

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')

        configs['start'] = item['start_point']
        configs['end'] = item['end_point']

    with open(f'{base_dir}/config.json', 'w', encoding='utf-8') as f:
        json.dump(configs, f, indent=2, ensure_ascii=False)

    with open(f"{base_dir}/funds.json", 'r', encoding='utf-8') as f:
        funds = json.load(f)

        for intersected in list(set(funds) & set(not_comps)):
            funds.remove(intersected)

        item['funds'] = funds

    with open(f"{base_dir}/stats.json", 'r', encoding='utf-8') as f:
        stats = json.load(f)
        item['ever_holded_count'] = len(stats['counts'])

    if os.path.exists(f'{base_dir}/candidates.json'):
        with open(f"{base_dir}/candidates.json", 'r', encoding='utf-8') as f:
            candidates = json.load(f)
            total_candidates_count = sum([x[1] for x in candidates])
            item['avg_ever_holded_count'] = round(total_candidates_count / len(fund), 4)
    else:
        item['avg_ever_holded_count'] = 0

    with open(f"{base_dir}/metrics.json", 'r', encoding='utf-8') as f:
        metrics = json.load(f)[fund_name]

        item['max_retracement'] = metrics['max_drawdown']
        item['annual_return'] = metrics['annual_return_ratio']
        item['sharpe_ratio'] = metrics['sharpe_ratio']

    item = {**item, **base}
    data.append(item)

with open(f'list-fof.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
