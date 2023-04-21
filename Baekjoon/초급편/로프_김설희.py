n = int(input())
ropes = [int(input()) for _ in range(n)]

# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
# 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
# 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램

ropes.sort(reverse=True)

result = []
for i in range(n):
    result.append(ropes[i]*(i+1))

print(max(result))