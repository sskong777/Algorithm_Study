def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    c = -30001
    for s, e in routes:
        if c < s:
            c = e
            answer += 1
    return answer

print(solution(routes=[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))