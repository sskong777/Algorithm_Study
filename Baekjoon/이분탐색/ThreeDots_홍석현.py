# 재귀
# def binary_search(array,target,start,end):
#     if start > end:
#         return
#     mid = (start+end)//2
#
#     if array[mid] == target:
#         return mid
#
#     #중간점의 값보다 찾고자하는 값이 작은경우, - 왼쪽 확인
#     elif array[mid] > target:
#         return binary_search(array,target,start,mid-1)
#     # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 - 오른쪽 확인
#     else:
#         return binary_search(array,target,mid+1,end)

# 이진탐색 반복문
def binary_search(target,start,end):
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return 1
        #중간점의 값보다 찾고자하는 값이 작은경우, - 왼쪽 확인
        elif arr[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 - 오른쪽 확인
        else:
            start = mid + 1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0

    start, end = 0, N-1

    for i in range(N-1):
        for j in range(i+1,N):
            dist = abs(arr[j] - arr[i])
            if binary_search(dist+arr[j],start,end):
                ans += 1

    print(ans)




# 시간 초과
# import itertools
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     arr.sort()
#     cnt = 0
#
#     combis = itertools.combinations(arr,3)
#     for dots in combis:
#         if dots[1]-dots[0] == dots[2]-dots[1]:
#             cnt += 1
#
#     print(cnt)
#
