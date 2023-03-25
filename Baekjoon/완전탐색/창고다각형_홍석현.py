# 가장 높은 기둥을 기준으로 양 옆의 면적을 따로 계산해서 합산.

N = int(input())

arr = [0] * 1001
for i in range(N):
    x,y = map(int,input().split())
    arr[x] = y

# 가장 높은 기둥의 인덱스를 먼저 구한다.
max_index = arr.index(max(arr))

# 왼쪽 넓이 구하기
left_height = 0
left_sum = 0
for i in range(max_index):
    left_height = max(left_height, arr[i])
    left_sum += left_height

# 가장 높은 기둥 넓이 구하기
center_sum = arr[max_index]

# 오른쪽 넓이 구하기
right_height = 0
right_sum = 0
for i in range(1000,max_index,-1):
    right_height = max(right_height, arr[i])
    right_sum += right_height

sum_area = left_sum + center_sum + right_sum
print(sum_area)
