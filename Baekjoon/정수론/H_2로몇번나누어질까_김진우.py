'''
import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def f(x):
    cnt = 0
    for i in range(1,x):
        print(i)
        if x%2 == 0:
            print("if 문 입니다")
            print(f'x : {x}')
            x = x//(2)
            cnt += 1

            print(f'cnt : {cnt}')
        else:
            print("else 문 입니다")
            break
    return 2**cnt

ans = 0
for i in range(a,b+1):
    ans += f(i)

print(ans)
# print(f(40))
'''

'''
a, b = map(int, input().split())


def f(x):
    return b // x - a // x + 1 - bool(a % x)


i = 0
ans = 0
while 1:
    if f(2 ** i) == 0:
        print(ans)
        break

    ans += f(2 ** i) * 2 ** max(0, i-1)
    i += 1
'''

a,b = map(int, input().split())

def f(number) :
  if number == 0 :
    return 0
  elif number == 1 :
    return 1
  elif number % 2 == 0 :
    return number // 2 + 2 * f(number // 2)
  elif number % 2 == 1 :
    return number // 2 + 2 * f(number // 2) + 1

print(f(b) - f(a - 1))


#모르겠따~~~~~~~~~~~~~~~~~~~~~~~