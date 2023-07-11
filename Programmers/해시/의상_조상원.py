from collections import defaultdict
from itertools import permutations

def solution(clothes):
    answer = 0
    c = defaultdict(list)
    
    for v, k in clothes:
        c[k].append(v)
    
    print(c)
    tot = 1
    for k in c.keys():
        tot *= (len(c[k])+1)
    
    return tot - 1 