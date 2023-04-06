# def two_pointer(arr, target):
#     count = 0
#     left, right = 0, len(arr)-1
#     while left < right:
#         curr_sum = sum(arr[left:right])
#         if curr_sum == target:
#             left += 1
#             count += 1
#         elif curr_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return count

N, M = map(int,input().split())
arr = list(map(int,input().split()))

start, end, count, ssum = 0, 0, 0, 0

while True:
    # 부분합이 M과 같거나 큰 경우 start를 이동시킨다.
    if ssum >= M:
        ssum -= arr[start]
        start += 1
    # 부분합이 M과 작은 경우 end를 이동시킨다.
    elif end == N:
        break
    else:
        ssum += arr[end]
        end += 1

    # 부분합이 M과 같은 경우 count를 증가시킨다.
    if ssum == M:
        count += 1

print(count)