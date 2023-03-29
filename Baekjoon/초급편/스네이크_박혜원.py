# [27512] 스네이크
# 가로 * 세로 : 짝 * 짝  or 홀 * 짝 or 짝 * 홀 이면 가장 긴 뱀의 길이는 가로 * 세로이다.
# 가로 * 세로 :  홀 * 홀  ->  가로 * 세로 - 1 이다.


n, m = map(int, input().split())

if n % 2 != 0 and m % 2 != 0:
    print(n * m - 1)
else:
    print(n * m)
