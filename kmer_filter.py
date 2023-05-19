import json
from collections import Counter

# jtk: jellyfish kmer count result with '--text' flag set
def jtk_iterator(path):
    f = open(path)
    header_size = int(f.read(9)) # 读取接下来的json大小
    header_s = f.read(header_size).replace('\x00', '') # 读取json，其末端可能有\x00填充，需要切掉
    header = json.loads(header_s)
    while True:
        s = f.readline()
        if s == "":
            break
        else:
            pair = s.strip().split()
            yield pair[0], int(pair[1])
    f.close()

jtk_path = "/home/user/duanran/repo/spider-web/ref/NC_008253.jtk"
fk_path = "/home/user/duanran/repo/spider-web/ref/NC_008253.filtered.fk"
of = open(fk_path, "w")
jtk = jtk_iterator(jtk_path)
for key, val in jtk:
    c = Counter(key)
    proportion = (c['C'] + c['G']) / len(key)
    
