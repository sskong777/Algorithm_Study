n , x = map(int , input().split())
a = list(map(int,(input().split())))
b = list(map(int,(input().split())))
# print(a,b)
# n일의 식단, 루틴을 진행하면 x키로만큼 빠짐
'''
10 5
1 3 2 2 5 7 1 3 1 5
3 5 6 5 3 1 3 5 1 3
'''

ans = 0

for i in range(n):
    routine = b[i] - a[i]
    print(routine)
    while routine>=0 :
        print(ans, routine)
        routine -= x
        ans += 1

if ans <= 0 :
    print(-1)
else:
    print(ans-1)
