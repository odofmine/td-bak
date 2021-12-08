import json
import glob
import shutil

from datetime import datetime, timedelta

dirs = glob.glob('./fof/*/')

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

start = 1634625570
end = 1626950546

for ts in dirs:
    dt = datetime.utcfromtimestamp(ts)

    base_dir = f'/Users/lizhe/Workspace/td/fof/{ts}'

    with open(f'{base_dir}/remark.md', 'w') as f:
        f.write('#### 备注')

    # print(f'remove {base_dir}({dt})')
    # shutil.rmtree(base_dir)
