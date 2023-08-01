K = int(input())
building_nums = list(map(int,input().split()))

answer = [[] for _ in range(K)]

def dfs(building_nums, depth):

    mid = len(building_nums)//2

    answer[depth].append(building_nums[mid])

    if len(building_nums) == 1:
        return

    dfs(building_nums[:mid], depth+1)
    dfs(building_nums[mid+1:], depth+1)

dfs(building_nums,0)

for i in answer:
    print(*i)

# def dfs(inorder, depth):
#
#     # 트리의 root index를 찾아낸다.
#     mid = (len(inorder) // 2)
#
#     # 해당 깊이에 해당하는 node를 추가한다.
#     answer[depth].append(inorder[mid])
#
#     if len(inorder) == 1:
#         return
#
#     dfs(inorder[:mid], depth+1)
#     dfs(inorder[mid+1:], depth+1)
#
# dfs(inorder, 0)
#
# for i in answer:
#     print(*i)