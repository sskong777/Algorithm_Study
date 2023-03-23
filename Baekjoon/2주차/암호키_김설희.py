n = int(input())

for _ in range(n):
    num = int(input())
    flag = False

    for i in range(2, 1000001):
        if num % i == 0:
            print("NO")
            flag = True
            break

    if flag == False:
        print("YES")
