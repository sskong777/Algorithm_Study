# [13423] Three Dots

def binary_search(start, end, target):

    while start <= end:

        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for _ in range(int(input())):
    count = 0
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()

    for i in range(n-1):
        for j in range(i+1, n):
            dist = abs(array[j]-array[i])
            if binary_search(0, n-1, array[j] + dist):
                count += 1
    print(count)
