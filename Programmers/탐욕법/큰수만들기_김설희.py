# 완전탐색 시간 초과로 불가능 -> 그리디 알고리즘 (스택 이용)
'''
def solution(number, k):

    n = len(number)
    index = [0] * k
    result = []
    def dfs(v, total):
        if v == k:
            num = ""
            for i in range(n):
                if i not in index:
                    num += number[i]
            result.append(int(num))
        else:
            for i in range(total, n):
                index[v] = i
                dfs(v + 1, i + 1)


    dfs(0, 0)

    return str(max(result))
'''

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
