import json
import glob
import shutil

from datetime import datetime, timedelta

dirs = glob.glob('./fof/*/')

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

bts = 1628240933

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)

    if ts < bts:
        continue

    base_dir = f'xxxx/td/fof/{ts}'

    print(f'remove {base_dir}({dt})')
    shutil.rmtree(base_dir)
