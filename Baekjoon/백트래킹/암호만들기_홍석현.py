# L, C = map(int,input().split())
# arr = list(input().split())
#
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# arr.sort()
#
# def check_dic(result):
#     flag = True
#     for i in range(len(result)-1):
#         if result[i] > result[i+1]:
#             flag = False
#     return flag
#
#
# def dfs(start,depth,result):
#     if depth == L:
#         v_cnt = 0
#         c_cnt = 0
#         for i in vowels:
#             if i in result:
#                 v_cnt += 1
#             else:
#                 c_cnt += 1
#         if v_cnt >= 1 and c_cnt >= 2 and check_dic(result):
#             print(''.join(result))
#
#     for i in range(start, C):
#         result.append(arr[i])
#         dfs(i+1,depth+1,result)
#         result.pop()
#
# dfs(0,0,[])

L, C = map(int, input().split())
arr = list(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

arr.sort()

def dfs(start, depth, result):
    if depth == L:
        v_cnt = sum(1 for c in result if c in vowels)
        c_cnt = len(result) - v_cnt
        if v_cnt >= 1 and c_cnt >= 2:
            print(''.join(result))
        return

    for i in range(start, C):
        result.append(arr[i])
        dfs(i+1, depth+1, result)
        result.pop()

dfs(0, 0, [])