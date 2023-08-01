import sys
from collections import deque
input = sys.stdin.readline

def solution(queries):
    global ball_cnt, wall_cnt
    if len(queries) == 1:
        pop()
    else:
        action, object = queries
        if action == "push":
            push(object)
        if action == "count":
            count(object)
        if action == "rotate":
            rotate(object)
    apply_gravity()


def push(object):
    global ball_cnt, wall_cnt
    queue.append(object)
    if object == "b":
        ball_cnt += 1
    else:
        wall_cnt += 1


def count(object):
    if object == "b":
        print(ball_cnt)
    elif object == "w":
        print(wall_cnt)


def pop():
    global ball_cnt, wall_cnt
    if queue:
        checking = queue.popleft()
        if checking == "b":
            ball_cnt -= 1
        elif checking == "w":
            wall_cnt -= 1


def apply_gravity():
    global ball_cnt
    if angle == 90:
        while queue:
            if queue[0] == "w":
                break
            queue.popleft()
            ball_cnt -= 1
    if angle == 270:
        while queue:
            if queue[-1] == "w":
                break
            queue.pop()
            ball_cnt -= 1


def rotate(direction):
    global angle
    if direction == "r":
        angle += 90
    else:
        angle -= 90
    if angle < 0:
        angle += 360
    elif angle > 270:
        angle -= 360

q = int(input())
queue = deque([])
angle = 0
ball_cnt = 0
wall_cnt = 0

for _ in range(q):
    query = list(input().strip().split())
    solution(query)

