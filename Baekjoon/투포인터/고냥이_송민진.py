import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

if len(s) == 1:
    print(1)
elif len(set(s)) <= n:
    print(len(s))

else:
    end = 0
    max_len = 0
    types = []
    for start in range(len(s)):
        types = {s[start]}
        tmp_len = 0
        end = start
        while end < len(s):
            if s[end] not in types:
                types.add(s[end])
                if len(types) > n:
                    break
            end += 1
            tmp_len += 1
            if end == len(s) - 1:
                break
        max_len = max(max_len, tmp_len)

    print(max_len)