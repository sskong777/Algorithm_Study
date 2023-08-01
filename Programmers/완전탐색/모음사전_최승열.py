
# 테스트 케이스 최대 1.62ms
import itertools
def solution(word):
    vowels = "AEIOU"
    D = []
    for n in range(1, 6):
        D.extend(["".join(s) for s in itertools.product(vowels, repeat=n)])
    D.sort()
    return D.index(word)+1

# 위 코드 숏코딩 버전
# 테스트 케이스 최대 1.41ms
import itertools
def solution(word):
    return sorted(["".join(s) for n in range(1, 6) for s in itertools.product("AEIOU", repeat=n)]).index(word)+1
