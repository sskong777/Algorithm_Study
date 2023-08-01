from itertools import product

def solution(word):
    answer = 0
    
    a = ['A', 'E', 'I', 'O', 'U']
    temp = []
    for i in range(1, 6):
        for w in product(a, repeat=i):
            temp.append(''.join(w))
    
    temp.sort()
    answer = temp.index(word) + 1
    
    return answer