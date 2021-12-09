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
        f.write('#### 思路\n')
        f.write('回测目的，要验证的东西\n')
        f.write('\n')
        f.write('#### 参数\n')
        f.write('都有哪些可设置的参数以及固定的参数\n')
        f.write('* 参数 1\n')
        f.write('* 参数 2\n')
        f.write('* 参数 3\n')
        f.write('* 参数 4\n')
        f.write('\n')
        f.write('#### 描述\n')
        f.write('描述结果\n')
        f.write('\n')
        f.write('#### 总结\n')
        f.write('对于目的的总结，是否符合预期，或者是否有新的发现\n')

    # print(f'remove {base_dir}({dt})')
    # shutil.rmtree(base_dir)
