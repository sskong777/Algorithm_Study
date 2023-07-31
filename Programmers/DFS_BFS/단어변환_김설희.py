from collections import deque

def solution(begin, target, words):

    def diff_count(A, B):
        cnt = 0
        for a, b in zip(A, B):
            if a != b:
                cnt += 1
        return True if cnt == 1 else False

    visited = set()
    queue = deque([(0, begin)])

    while queue:
        v, word = queue.popleft()
        if word == target:
            return v

        visited.add(word)
        for next in words:
            if next not in visited and diff_count(word, next):
                queue.append((v + 1, next))
        visited.add(word)

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))