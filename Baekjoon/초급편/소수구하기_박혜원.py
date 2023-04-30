# [1929] 소수구하기


"""
for i in range(M, N+1):
    if i == 1:
        continue  # 1은 소수가 아니니까 넘어가기
    
    for j in range(2, int(i**0.5) + 1): 
        if i % j == 0:
            break
    else:
        print(i)
"""
# 인자로 들어온 수의 제곱근 까지만 확인하여 소수인지 아닌지를 검증

M, N = map(int, input().split())


def is_prime(num):
    if num == 1:
        return False

    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


for i in range(M, N+1):
    if is_prime(i) == True:
        print(i)
    else:
        pass
