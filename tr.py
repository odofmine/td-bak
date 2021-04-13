import json

data = []

with open('list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('list.json', 'w', encoding='utf-8') as f:
    for item in data:
        with open(f"{item['id']}/metrics.json", 'r', encoding='utf-8') as f2:
            metrics = json.load(f2)

            item['annual_return'] = metrics['strategy']['annual_return_ratio']
            item['sharpe_ratio'] = metrics['strategy']['sharpe_ratio']

    with open(f'list.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

