import sys
n = int(input())

stack=[]
results=[]
chk = True
start=1
for i in range(n):
    target = int(sys.stdin.readline())

    while start <= target:
        stack.append(start)
        results.append('+')
        start += 1

    if stack[-1]==target:
        stack.pop()
        results.append("-")
    else:
        chk=False
        break

if chk==False:
    print("NO")
else:
    for result in results:
        print(result)      




        