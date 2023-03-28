# [1712] 손익분기점
# A + Bx = Cx
# (C-B)x = A, x = A/(C-B) 일 떄 생산비용과 판매비용이 같아짐.
# 수익이 나는 손익분기점은  A/(C-B) + 1
# 분모(C-B)가 0이면 -1 출력

A, B, C = map(int, input().split())

if C - B <= 0:
    print(-1)
else:
    print(int(A/(C-B)+1))
