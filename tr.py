import json

data = []

with open('list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('list.json', 'w', encoding='utf-8') as f:
    for item in data:
        item['strategy'] = {
            'name': 't4',
            'version': '1.0'
        }
        item['source'] = 'bitmex-bitstamp'
        item['start_point'] = '2014-01-01'
        item['end_point'] = '2021-01-01'
        item['frequency'] = '1d'
        item['year_return'] = '23%'
        item['max_retracement'] = '23%'
        item['sharpe_ratio'] = '1.2'

    with open(f'list.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

