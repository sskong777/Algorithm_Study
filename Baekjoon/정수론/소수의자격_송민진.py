import math
a, b, d = map(int, input().strip().split())

prime_arr = [True for i in range(b + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(b)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if prime_arr[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= b:
            prime_arr[i * j] = False
            j += 1
# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True

cnt = 0
for num in range(a, b+1):
    if str(d) in str(num):
        if prime_arr[num]:
            cnt += 1

print(cnt)