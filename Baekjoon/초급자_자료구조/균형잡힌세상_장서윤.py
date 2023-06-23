import sys



pair = {')': '(',
        ']': '[',
        '}': '{'}


def braket(sentence):
    stack = list()
    if sentence == ".":
        return "end"

    for j in sentence:
        if j in '{[(':
            stack.append(j)

        elif j in '}])':
            if len(stack) == 0:
                print("no")
                return
            close = stack.pop()
            if pair[j] != close:
                print("no")
                return

    if len(stack) == 0:
        print("yes")
    else:
        print("no")


while True:
    sentence = sys.stdin.readline().rstrip()
    if braket(sentence)=="end":
        break