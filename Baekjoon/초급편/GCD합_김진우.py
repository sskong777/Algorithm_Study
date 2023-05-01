import sys
def gcd(a, b):  
        return a
    else:
        return gcd(b, a % b)


n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))  
    temp = 0
    for j in range(1, len(a)):  
        for k in range(1, len(a)):
            if j < k:  
                temp += gcd(a[j], a[k])
            else:
                pass
    print(temp)
