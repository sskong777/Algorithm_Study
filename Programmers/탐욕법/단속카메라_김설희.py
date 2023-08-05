def solution(routes):
    ans = 0
    camera = -30001
    routes.sort(key=lambda x: x[1])

    for route in routes:
        in_, out_ = route
        if camera < in_:
            camera = out_
            ans += 1

    return ans

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))