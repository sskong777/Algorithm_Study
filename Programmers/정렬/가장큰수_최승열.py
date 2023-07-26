# 기존 코드
# def solution(numbers):
#     return "0" if (ans := "".join(str(n) for _, n in sorted([(str(n) * 5, n) for n in numbers], reverse=True))).startswith("0") else ans

# 기존 코드 풀어쓴 코드
# def solution(numbers):
#     sorted_str = sorted([(str(n) * 5, n) for n in numbers], reverse=True)
#     item = [str(n) for _, n in sorted_str]
#     ans = "".join(item)
#     return "0" if ans.startswith("0") else ans

# 개선한 코드
def solution(numbers):
    return "0" if (ans := ''.join(sorted(list(map(str, numbers)), key=lambda x: x * 3, reverse=True))).startswith("0") else ans

# 개선한 코드 풀어쓴 코드
def solution(numbers):
    tmp = list(map(str, numbers))
    tmp = sorted(tmp, key=lambda x: x * 3, reverse=True)
    ans = ''.join(tmp)
    return "0" if ans.startswith("0") else ans