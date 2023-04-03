
# def isPrime(n):
#     sieve = [True] * n
#
#     m = int(n ** 0.5)
#     for i in range(2,m+1):
#         if sieve[i] == True:    # i가 소수인 경우
#             for j in range(i+i,n,i):    # i 이후의 배수들을 False로 변환
#                 sieve[j] = False
#
#     return [i for i in range(2,n) if sieve[i] == True]  # sieve리스트에서 True(소수)인 i값만 리스트에 담아서 반환

import math

def isPrime(n):
    if n < 2:  # 0, 1은 소수가 아님
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:  # 나누어 떨어지면 소수가 아님
            return False
    return True

def sol(N):
    num_list = [0,1,2,-1,-1,5,9,-1,8,6]

    reversed_N = N[::-1]

    ans = "no"
    new_num = []
    for i in reversed_N:
        if num_list[int(i)] < 0:
            ans = "no"
            return ans
        else:
            new_num.append(str(num_list[int(i)]))

    new_num = "".join(new_num)
    if isPrime(int(N)) and isPrime(int(new_num)):
        ans = "yes"
    else:
        ans = "no"
    return ans

N = input()
ans = sol(N)

print(ans)

