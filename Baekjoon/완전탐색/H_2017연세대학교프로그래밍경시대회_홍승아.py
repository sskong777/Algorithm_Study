# [14568] 2017 연세대학교 프로그래밍 경시대회 (브론즈 3)

N = int(input())
cnt = 0

for a in range(N-1):
    for b in range(N-1):
        for c in range(N-1):
            if a+b+c == N:
                if a != 0 and b != 0 and c != 0 and c>=b+2 and a%2==0:
                    cnt+=1
print(cnt)