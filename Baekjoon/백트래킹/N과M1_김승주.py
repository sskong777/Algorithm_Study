
from itertools import permutations


n , m = map(int, input().split())
per = list(range(1,n+1))


for i in permutations(per,m):
    for j in i :
        print(j, end =' ')
    print()