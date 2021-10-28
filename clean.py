import json
import glob
import shutil

from datetime import datetime, timedelta

dirs = glob.glob('./fof/*/')

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

start = 1626945267
end = 1626950546

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)

    if ts > end or ts < start:
        continue

    base_dir = f'/Users/lizhe/Workspace/td/fof/{ts}'

    print(f'remove {base_dir}({dt})')
    shutil.rmtree(base_dir)
