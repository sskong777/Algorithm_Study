import sys
from collections import deque

N = int(input())

class C:
    b = 0
    w = 0
    direction = 0

c = C()
dq = deque()

def rotate(val):
    amt = 90 if val == 'r' else -90
    c.direction = (c.direction + amt) % 360

def count(val):
    print(c.w if val == 'w' else c.b)

def push(val):
    dq.appendleft(val)
    if val == 'w': c.w += 1
    else: c.b += 1

def pop(popleft = False):
    if not dq: return 
    val = dq.popleft() if popleft else dq.pop()
    if val == 'w': c.w -= 1
    else: c.b -= 1

def run(cmd, val):
    if cmd == 'push':
        push(val)
    elif cmd == 'rotate':
        rotate(val)
    elif cmd == 'pop':
        pop()
    else:
        count(val)

def apply_gravity():
    if c.direction not in [90, 270]: return
    popleft, idx = (False, -1) if c.direction == 90 else (True, 0)
    while dq and dq[idx] != 'w':
        pop(popleft)

for l in sys.stdin.read().strip().split('\n'):
    cmd, val = l.split() if l != 'pop' else ('pop', None)
    run(cmd, val)
    apply_gravity()
