import sys
input = sys.stdin.readline

n, m , k = map(int,input().split())

count =0
while 1:
    n = n-2 # 여학생 2명 
    m = m-1 # 남학생 1명 제해봤을때!
    
    if n+m < k or n  < 0 or m<0:
        print(count)
        exit()
    count+=1