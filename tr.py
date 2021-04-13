import json
import os

from datetime import datetime

data = []

with open('list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('list.json', 'w', encoding='utf-8') as f:
    for item in data:
        item['currency'] = 'btc'
        item['product'] = 'coin-perp'
    json.dump(data, f, indent=2, ensure_ascii=False)

# with open('list.json', 'w', encoding='utf-8') as f:
#     for item in data:
#         with open(f"{item['id']}/metrics.json", 'r', encoding='utf-8') as f2:
#             metrics = json.load(f2)

#             item['annual_return'] = metrics['strategy']['annual_return_ratio']
#             item['sharpe_ratio'] = metrics['strategy']['sharpe_ratio']

#         with open(f"{item['id']}/statistic.json", 'r', encoding='utf-8') as f3:
#             statistic = json.load(f3)

#             item['max_retracement'] = statistic['dollar_retracement']

#         with open(f"{item['id']}/price.json", 'r', encoding='utf-8') as f4:
#             prices = json.load(f4)

#             start_ts = prices[0][0] / 1000
#             end_ts = prices[-1][0] / 1000

#             item['start_point'] = datetime.utcfromtimestamp(start_ts).strftime('%Y-%m-%d')
#             item['end_point'] = datetime.utcfromtimestamp(end_ts).strftime('%Y-%m-%d')

#         dt = item['date']
#         current_id = item['id']
#         target_id = f"{''.join(dt.split('-'))}001"

#         os.rename(current_id, target_id)
#         item['id'] = target_id

#     with open(f'list.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

