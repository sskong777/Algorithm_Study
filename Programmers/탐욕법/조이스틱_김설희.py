def solution(name):

    length = len(name)
    move = length - 1

    change = 0
    for i in range(length):
        change += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)

        next = i + 1
        while next < length and name[next] == "A":
            next += 1

        move = min(move, 2*i + length-next, i + 2*(length-next))

    return change + move

print(solution("JEROEN"))
print(solution("JAN"))

'''
print(chr(65))
print(ord("A"))
print(ord("J"))
print(ord("Z"))
'''