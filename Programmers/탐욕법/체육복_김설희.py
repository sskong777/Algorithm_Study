def solution(n, lost, reserve):

    students = [1] * (n + 1)

    for r in reserve:
        students[r] = 2

    for l in lost:
        students[l] -= 1

    for i in range(1, n + 1):
        if students[i] == 0:
            if i-1 > 0 and students[i-1] == 2:
                students[i] = 1
                students[i-1] = 1
            elif i+1 <= n and students[i+1] == 2:
                students[i] = 1
                students[i+1] = 1

    return len([x for x in students if x > 0]) - 1


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))