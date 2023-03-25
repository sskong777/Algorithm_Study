# [17252] 삼삼한수


num = int(input())

verify = True
if num == 0:        # 입력이 0인 경우 verify를 False로 설정
    verify = False

while num > 0:
    if num % 3 == 2:      # 나머지가 2인 경우 verify를 False로 설정하고 반복문 종료
        verify = False
    num //= 3    # 다음 자리 수를 확인하기 위해 입력 값을 3으로 나누기


if verify:          # while문이 종료 후 verify 값에 따라 print 된다.
    print("YES")    # 모든 자리 수를 확인한 후 verify가 여전히 True인 경우 "YES"를 출력합니다
else:
    print("NO")

# print("YES" if verify else "NO")
