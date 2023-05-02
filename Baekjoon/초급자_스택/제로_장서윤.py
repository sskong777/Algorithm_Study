K = int(input())

top_ = -1
size = 0

stack = [None for _ in range(K)]


def pop():
    global top_, size
    stack[top_] = None
    top_ -= 1
    size -= 1


def push(value):
    global top_, size

    top_ += 1
    stack[top_] = value
    size += 1


for i in range(K):
    v = int(input())
    if v == 0:
        pop()
    else:
        push(v)

print(sum(stack[0:size]))
