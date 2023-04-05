n,m = map(int,input().split())
arr = list(map(int,input().split()))


# arr.sort()
left = 0
right = 1
cnt = 0
while left <= right and right <= n:
    arr_sum = sum(arr[left:right])
    if  arr_sum < m :
        right += 1
    elif arr_sum > m :
        left += 1
    else:
        cnt += 1
        right +=1

print(cnt)
