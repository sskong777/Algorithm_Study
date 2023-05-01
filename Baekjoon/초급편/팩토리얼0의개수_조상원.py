
n = int(input())
import math

check = list(str(math.factorial(n)))

c = 0

while check:
    t = check.pop()
    if t != '0':
        print(c)
        break
    c+=1





