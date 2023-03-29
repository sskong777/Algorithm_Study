# [2839] 설탕배달

num = int(input())

count = 0   # 봉지 수
while num >= 0:
    if num % 5 == 0:       # 5로 나눈 나머지가 0인 경우에
        count += num // 5  # 5로 나눈 몫을 더해주고
        print(count)
        break
    num -= 3               # 더이상 5로 나누어 지지 않을때 5의 배수가 될 때까지 3씩 뺀다.
    count += 1
else:
    print(-1)
