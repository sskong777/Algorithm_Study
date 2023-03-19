'''
문제 : 방배정하기
'''

a, b, c , n = map(int, input().split())

for i in range((n//a)+1):
    for j in range((n//b)+1):
        for k in range((n//c)+1):
            if ( a*i + j*b + k*c )==n: 
                print(1)
                exit()
print(0)


''' 
think about
3중 for 문이 아닌 2중 for문으로 푼 결과는 부분 성공! why..?
for i in range((n//a)+1):
    for j in range((n//b)+1):
        if (n- (a*i + b*j)) % c ==0:
            print(1)
            exit()
print(0)
'''