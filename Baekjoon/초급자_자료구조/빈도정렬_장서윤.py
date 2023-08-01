from collections import OrderedDict

n, c = map(int, input().split())

ls = list(map(int, input().strip().split()))

f = OrderedDict()

for i in ls:
    if i in f.keys():
        f[i] += 1
    else:
        f[i] = 1

f = dict(sorted(f.items(), key=lambda x:x[1], reverse=True))

for k in f.keys():
    for _ in range(f[k]):
        print(k, end=" ")