
n = int(input())

for t in range(n):
    num = int(input())
    check = True
    for i in range(2,1000001):
        if num % i == 0 :
            print("NO")
            check = False
            break
    if check:
        print("YES")