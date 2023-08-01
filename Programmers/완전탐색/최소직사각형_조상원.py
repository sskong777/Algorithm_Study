def solution(sizes):
    answer = 0
    s = [(i, j) if i > j else (j, i) for i, j in sizes ]
    
    
    a = max(s, key=lambda x: x[0])
    b = max(s, key=lambda x: x[1])
    print(a, b)
    print(s)
    return a[0] * b[1]