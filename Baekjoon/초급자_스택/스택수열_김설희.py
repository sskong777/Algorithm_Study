import sys

# 1 부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 뽑아서 늘어놓는 것!!! => pop 한 숫자들을 기준으로 생각해야 함

n = int(sys.stdin.readline())
stack = []
result = []
start = 1
check = True

for _ in range(n):
    k = int(sys.stdin.readline())

    while start <= k:
        stack.append(start)
        result.append('+')
        start += 1

    if stack[-1] == k:
        stack.pop()
        result.append('-')
    else:
        check = False
        break

if check == False:
    print('NO')
else:
    for i in result:
        print(i)


