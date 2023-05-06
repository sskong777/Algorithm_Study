s = input()

cnt = 0
for i in range(len(s)-1):
    if s[i] == '0' and s[i+1] == '1':
        cnt += 1
    if s[i] == '1' and s[i+1] == '0':
        cnt += 1

if cnt % 2 == 0:
    print(cnt//2)
else:
    print(cnt//2+1)