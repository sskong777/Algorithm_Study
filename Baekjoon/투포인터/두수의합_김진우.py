n = int(input())
arr = list(map(int,input().split()))
x = int(input())

'''
완탐 코드
cnt = 0
# li.sort()
for i in range(n):
    for j in range(i+1, n):
        print(li[i],li[j])
        if li[i] + li[j] == x :
            cnt += 1
            print(f'cnt : {cnt}')

print(cnt)
'''

left = 0
right = len(arr) - 1

arr.sort()
print(f'arr : {arr}')
cnt = 0

while left < right:
    ans = arr[left] + arr[right]
    if ans == x:
        cnt += 1
        left += 1
        right -= 1
        # print(f'left, right, cnt : {left, right, cnt}')
    elif ans < x:
        left += 1
        # print(f'left, right : {left, right}')
    else:
        right -= 1
        # print(f'left, right : {left, right}')
print(cnt)