import json
import glob

from datetime import datetime, timedelta

dirs = glob.glob('./bt/*/')

base = {
    "type": "bt",
    "frequency": "1d",
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

    base_dir = f'bt/{ts}'

    with open(f"{base_dir}/price.json", 'r', encoding='utf-8') as f1:
        prices = json.load(f1)

        start_ts = prices[0][0]

        if len(str(start_ts)) > 10:
            data = list(map(lambda x : [int(x[0] / 1000), x[1]], prices))

            with open(f"{base_dir}/price.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)


    with open(f"{base_dir}/price.json", 'r', encoding='utf-8') as f2:
        prices = json.load(f2)

        start_ts = prices[0][0]
        end_ts = prices[-1][0]

        item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
        item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')


    with open(f"{base_dir}/metrics.json", 'r', encoding='utf-8') as f3:
        metrics = json.load(f3)

        item['annual_return'] = metrics['strategy']['annual_return_ratio']
        item['sharpe_ratio'] = metrics['strategy']['sharpe_ratio']


    with open(f"{base_dir}/statistic.json", 'r', encoding='utf-8') as f4:
        statistic = json.load(f4)

        item['max_retracement'] = statistic['dollar_retracement']

    with open(f"{base_dir}/params.json", 'r', encoding='utf-8') as f5:
        params = json.load(f5)

        if 'pair' in params:
            item['source'] = params['pair']
            item['currency'] = params['pair'].split('usd')[0]
            print(params['pair'])
        else:
            item['source'] = 'btcusd'
            item['currency'] = 'btc'

        if 'pstr' in params:
            item['strategy'] = {
                'name': params['pstr'],
                'version': '1.0'
            }
        else:
            item['strategy'] = {
                'name': 'trend-m-1',
                'version': '1.0'
            }

    item = {**item, **base}
    data.append(item)

with open('list-bt.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
