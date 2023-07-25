def solution(numbers):
    return "0" if (ans := "".join(str(n) for _, n in sorted([(str(n) * 5, n) for n in numbers], reverse=True))).startswith("0") else ans
