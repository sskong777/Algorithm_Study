import sys

n, m = map(int, sys.stdin.readline().split())

lib = dict()
lib_num = dict()

for p in range(1, n+1):
    v = sys.stdin.readline().strip()
    lib[v] = p
    lib_num[str(p)]=v

for p in range(1, m+1):
    v = sys.stdin.readline().strip()

    if v.isdigit():
        print(lib_num[v])
    else:
        print(lib[v])
