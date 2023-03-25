n = int(input())
ans = False

if n == 0:
    print("NO")
    ans = True

while n != 0:
   if n % 3 == 2:
        print("NO")
        ans = True
        break
   n //= 3 # 나머지 1이어도 괜찮으니까

if ans == False:
    print("YES")